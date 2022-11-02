import numpy as np
import math
from math import pow
import sys, os, time, datetime
In_Energy = 450  # incident photon energy (eV)
In_angle = 40  # incidence angle on the grating (degree)
Df_angle = 40  # diffracted beam angle (degree)
In_arm = 1200  # entrance arm (mm)
Ex_arm = 1800  # exit arm
# grating parameters
GR_a0 = 1200  # lines per mm of gratings 1200 lines/mm
GR_a1 = 0.9  # mm[-2]
GR_a2 = 1.2E-4  # mm[3]
R_Gr = 58550  # radius of curvature of the grating surface mm

# other constant parameters
k_order = 1  # diffraction order
K_Energy = 1.239843E-3  # energy to wavelength conversion, 1.239843E-3 mm eV
PI = math.pi


def get_df_angle(in_angle, Energy, line_density):
    dft_angle = 180.0 / PI * math.asin(math.sin(in_angle / 180.0 * PI) - k_order * K_Energy * line_density / Energy)
    print(f'get diffracted angle:{dft_angle:.4f}')
    return dft_angle


def get_ex_arm(in_angle, df_angle, radius_GR, in_arm, Energy, Gr_a1):
    ex_arm = pow(math.cos(df_angle * PI / 180), 2) / (
                (math.cos(in_angle * PI / 180) + math.cos(df_angle * PI / 180)) / radius_GR - pow(
            math.cos(in_angle * PI / 180), 2) / in_arm + k_order * K_Energy * Gr_a1 / Energy)
    print(f'get exit arm length={ex_arm:.4f}')
    return ex_arm


def get_grazing_angle_CCD(df_angle, exit_arm, radius_GR, Gr_a0, Gr_a1):
    grazing_angle_CCD = math.atan(math.cos(df_angle * PI / 180) / (2 * math.sin(df_angle * PI / 180) - exit_arm * (
                math.tan(df_angle * PI / 180) / radius_GR + Gr_a1 / Gr_a0)))
    print(f'get grazing incidence angle on the CCD:{grazing_angle_CCD * 180 / PI:.2f}')
    return grazing_angle_CCD * 180 / PI


if __name__ == "__main__":
    df_beta = get_df_angle(In_angle, In_Energy, GR_a0)
    print(df_beta)
    exit_arm = get_ex_arm(In_angle, df_beta, R_Gr, In_arm, In_Energy, GR_a1)
    grazing_angle_ccd = get_grazing_angle_CCD(df_beta, exit_arm, R_Gr, GR_a0, GR_a1)
