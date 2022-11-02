# coding=utf-8
import os, sys, time
import math
from turtle import title
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
from scipy.misc import derivative
from scipy.signal import savgol_filter
from scipy.optimize import curve_fit
import pandas as pd
from numpy import exp, loadtxt, pi, sqrt
from lmfit import Model
sys.path.append('.')

def import_data(filename):
    """
    import data from files as pandas dataframe,
    support filetype:<.xlsx>,<.csv>,<.json>.
    :return: data in pandas dataframe form
    """
    pd_data = pd.DataFrame()
    # filename, filetype = QFileDialog.getOpenFileName(self, "read data file(supported filetype:xlsx/csv/json)",
    #                                                  './', '*.xlsx;;*.csv;;*.json')
    # print(filename, filetype)
    assert os.path.isfile(os.path.abspath(filename))
    if filename.endswith('.xlsx'):
        # add dtype={'time stamp': 'datetime64[ns]'} if have 'time stamp'
        pd_data = pd.read_excel(filename, index_col=0, na_values=["NA"], engine='openpyxl')
        # print(pd_data)
    if filename.endswith('.csv'):
        pd_data = pd.read_csv(filename, index_col=0)
    if filename.endswith('.json'):
        pd_data = pd.read_json(filename)
    # drop the row with NaN and return
    return pd_data.dropna()


def cal_deriv(x:list, y:list,x_label:str='x',y_label:str='y'):  # x, y的类型均为列表
    diff_x = []  # 用来存储x列表中的两数之差
    for i, j in zip(x[0::], x[1::]):
        diff_x.append(j - i)

    diff_y = []  # 用来存储y列表中的两数之差
    for i, j in zip(y[0::], y[1::]):
        diff_y.append(j - i)

    slopes = []  # 用来存储斜率
    for i in range(len(diff_y)):
        slopes.append(diff_y[i] / diff_x[i])

    deriv = []  # 用来存储一阶导数
    for i, j in zip(slopes[0::], slopes[1::]):
        deriv.append((0.5 * (i + j)))  # 根据离散点导数的定义，计算并存储结果
    deriv.insert(0, slopes[0])  # (左)端点的导数即为与其最近点的斜率
    deriv.append(slopes[-1])  # (右)端点的导数即为与其最近点的斜率

    # plot results
    fig1, ax = plt.subplots()
    axnew = ax.twinx()
    ax.set_title("direct derivative")
    lin0 = ax.plot(x, y, marker='o', markersize=3, markerfacecolor='#20B2AA',
                              markeredgecolor='#20B2AA', linestyle='-', color='#20B2AA', label='original')
    deriv_conv=convolve_1D(deriv,np.array([0.2,0.2,0.2,0.2,0.2]))
    linD = axnew.plot(x[1:-1], deriv_conv[1:-1],marker='o', markersize=3, linestyle='-', color='m', label='1st derivative')
    lins = lin0  + linD
    labels = [l.get_label() for l in lins]
    ax.legend(lins, labels, loc=0)
    axnew.grid(which='both')
    ax.set_ylabel(y_label, fontsize=16, color='#20B2AA')
    ax.set_xlabel(x_label, fontsize=16, color='#20B2AA')
    axnew.set_ylabel('1st derivative', fontsize=16, color='m')
    plt.show()
    #return deriv,x
    return deriv_conv[1:-1],x[1:-1]


def interp_derivative(x: list, y: list, n_interp: int = 10,x_label:str='x',y_label:str='y'):
    """
    interpolate the x,y list first, then calculate the derivative value at each points
    :param n_interp: total number of the interpolate values
    :param x:
    :param y:
    :return:
    """
    interp_quad = interp1d(x, y, kind='quadratic')
    rbf=Rbf(x,y,function='linear')
    ius=InterpolatedUnivariateSpline(x,y) 
    n_interp=len(x)+n_interp
    new_x = [min(x) + i * (max(x) - min(x)) / n_interp for i in range(n_interp - 1)]
    new_y=ius(new_x)
    #new_y = interp_quad(new_x)
    deriv_val = list()
    for x_val in new_x[1::]:
        deriv_val.append(derivative(interp_quad, x_val, dx=1e-6))
    # deal with the new_x[0]
    slope0 = (new_y[1] - new_y[0]) / (new_x[1] - new_x[0])
    deriv_val.insert(0, slope0)

    # plot results
    fig2,ax=plt.subplots()
    axnew=ax.twinx()
    ax.set_title("quadratic interpolate and derivative")
    lin0=ax.plot(x, y, 'or', markersize=3, label='original')
    lin1=ax.plot(new_x, new_y, '-xc', markersize=3, label='interpolate')
    deriv_val_conv=convolve_1D(deriv_val,np.array([0.2,0.2,0.2,0.2,0.2]))
    linD=axnew.plot(new_x[1:-1], deriv_val_conv[1:-1], '-om', markersize=3, label='1st derivative')
    lins=lin0+lin1+linD
    labels=[l.get_label() for l in lins]
    ax.legend(lins, labels, loc=0)
    axnew.grid(which='both')
    ax.set_ylabel(y_label, fontsize=16, color='#20B2AA')
    ax.set_xlabel(x_label, fontsize=16, color='#20B2AA')
    axnew.set_ylabel('1st derivative', fontsize=16, color='m')
    #plt.show()
    #return deriv_val,new_x
    return deriv_val_conv[1:-1],new_x[1:-1]

def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))


def GaussianFit(x,y,center=1200,info:str='GaussFit'):
    """find FWHM from the imported array data [x,y]

    Args:
        x: array
        y: array
        center: index(x) of peak
        info:data info
    Returns:
        fit_results(dict):{"cen":(value,value|None),"wid":(value,value|None),"FWHM":(value,value|None),"info":info}
    """
    Fit_results={}
    gmodel = Model(gaussian)
    result = gmodel.fit(y, x=x, amp=4006, cen=center, wid=2.6)
    #print(result.values)
    #print(result.fit_report())
    wid_fit=result.params['wid'].value
    wid_err=result.params['wid'].stderr
    cen_fit=result.params['cen'].value 
    cen_err=result.params['wid'].stderr
    Fit_results['wid']=(wid_fit,wid_err)
    Fit_results['cen']=(cen_fit,cen_err)
    Fit_results['info']=info
    if wid_err!= None:
        FWHM=wid_fit*2*np.sqrt(np.log(4))
        FWHM_err=wid_err*2*np.sqrt(np.log(4))
    else:
        FWHM=-1   # Gaussian fit failed
        FWHM_err=0
    Fit_results['FWHM']=(FWHM,FWHM_err)
    Fit_results['ini_fit']=(x,result.init_fit)
    Fit_results['best_fit']=(x,result.best_fit)
    Fit_results['origin_data']=(x,y)
    #print(f'get FWHM={FWHM:.4f} with error +/-{FWHM_err}')
    
    return Fit_results,FWHM

def plot_Gaussfit_line(Fit_result:dict,save_folder:str='./',filename:str='GaussFit_result',title:str='result'):
    """ Fit_result={"FWHM":(FWHM,FWHM_err)}

    Args:
        min_result (list): _description_
        index (int, optional): _description_. Defaults to 0.
    """
    fig=plt.figure(figsize =(16, 9))
    fig.canvas.manager.window.setWindowTitle(f"Gauss_Fit-FWHM")
    ax=plt.subplot()
    plt.plot(*Fit_result['origin_data'], '-o',markersize=3,color = "c")
    plt.plot(*Fit_result['ini_fit'], '--', label='initial fit')
    plt.plot(*Fit_result['best_fit'], '-', label='best fit')
    FWHM_text=f'FWHM={Fit_result["FWHM"][0]:.4f} +/-{Fit_result["FWHM"][1]}'
    cen_text=f'cen={Fit_result["cen"][0]:.4f} +/-{Fit_result["cen"][1]}'
    plt.text(0.5, 0.5, s=FWHM_text+'\n'+cen_text,color = "m", transform=ax.transAxes,fontsize=15)
    plt.title(f"Gaussfit FWHM-{title}")
    plt.legend()
    save_fig=os.path.join(save_folder,f'Gaussfit_fit_results_{filename}.jpg')
    plt.savefig(save_fig)
    plt.show()

import scipy.stats as sta


def gaussian_smooth_points(points, kernel_r, nsig=3):
    """ 将 points 进行高斯平滑 """
    print(f'origin points: \n{len(points)}')
    smoothed_points = points.copy()
    kernlen = kernel_r * 2 + 1
    x = np.linspace(-nsig, nsig, kernlen + 1)
    kern1d = np.diff(sta.norm.cdf(x))
    kern1d = kern1d / kern1d.sum()

    len_points = len(points)
    for j in range(len_points):
        if kernel_r < j < len_points - kernel_r:
            sum_data = np.array([0.0, 0.0, 0.0])
            for i in range(1, 2 * kernel_r + 1, 1):
                idx = j + i - kernel_r - 1
                sum_data += points[idx] * kern1d[i]
            smoothed_points[j] = sum_data.sum() / (2 * kernel_r + 1)
    return smoothed_points

def convolve_1D(data,core=np.array([0.35,0.3,0.35])):
    return np.convolve(data,core,mode='same')

def gaussian_fit(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / 4 / stddev)**2)

#popt, _ = curve_fit(gaussian_fit, x, data)

if __name__ == '__main__':
    #xlsxFile1 = './GE/BPM_Zsize_0125_01_save.xlsx'
    xlsxFile1 = './GE/04_Z_pA_BPM_Z_slit2-50_Size_SM6_pitch-1dot07.xlsx'
    
    xlsxFile2 = './2021-12-11/BeamSize_Z_pA_1211_M03_300um_save.xlsx'
    xlsxFile3 = './2021-12-11/BeamSize_Z_pA_1211_M04_300um_0.xlsx'
    xlsxFile4 = './2021-12-11/BeamSize_X_pA_1211_M02_1200um.xlsx'
    xlsxFile5 = './2021-12-11/BeamSize_X_pA_1211_M03_1200um_save.xlsx'
    xlsxFile6 = './2021-12-11/BeamSize_X_pA_1211_M04_1200um.xlsx'
    xlsxFile7 = './2021-12-11/BeamSize_X_pA_1211_M05_1200um.xlsx'

    print(os.path.abspath(xlsxFile1))
    pd_data=import_data(xlsxFile1)
    #print(pd_data)
    dict_data={}
    for label, content in pd_data.items():
        dict_data[str(label)] = content.tolist()
    print(dict_data['scan set'],dict_data['current(pA)'])
    x,y=dict_data['scan set'],dict_data['current(pA)']
    #y_convolve=gaussian_smooth_points(y,1,3)
    y_convolve=savgol_filter(y,30,3)
    #y_convolve=np.convolve(y,np.array([0.35,0.3,0.35]),mode='same')
    #print(f'smooth data:\n{len(y_smooth)}')
    plt.plot(x,y)
    plt.plot(x[1:],y_convolve[1:])
    interp_derivative(x[1:],y_convolve[1:],len(x)+50,x_label='BPM-X(um)',y_label='Current(pA)')
    #interp_derivative(x,y,len(x)+50,x_label='BPM-X(um)',y_label='Current(pA)')
    # method 2

    deriv_result = cal_deriv(x[1:],y_convolve[1:],x_label='BPM-X(um)',y_label='Current(pA)')
    plt.show()