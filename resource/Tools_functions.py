import os, datetime, time
import logging, math, traceback
from functools import wraps
import pandas as pd

"""
Notes:
    Some nice functions/packages for usage  
"""


def get_datetime():
    """ get current date time, as accurate as milliseconds

        Args: None

        Returns:
            str type
            eg: "2018-10-01 00:32:39.993176"

    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(timestamp)
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


def creatPath(file_path):
    """
    create a given path if not exist and return it
    :param file_path:
    :return: file_path
    """
    if os.path.exists(file_path) is False:
        os.makedirs(file_path)
    return file_path
    # os.chdir(file_path)


def my_logger(log_file: str = 'output.log', logger_name: str = 'usr_test'):
    """
    return a logger for logging
    :return:
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def to_log(text, filename='my_log.log', path=os.getcwd()):
    """
    save  data to log file
    :param text:str  write str
    :param filename: filename end with .text .dat .log
    :param path: path to file
    :return: None
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_info = f'\n{timestamp:>>25}:{text}\n'
    filepath = os.path.join(path, filename)
    with open(filepath, 'a') as f:
        f.write(log_info)
        f.close()


# decorator functions
# log txt when function called
def deco_log_text(text: str, logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            filepath = os.path.join(os.getcwd(), logfile)
            print(filepath)
            with open(filepath, 'a+') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n' + text + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


# decorator functions
def log_exception(func=None, log_func=None, **kw):
    """
    suppress error and log any Exceptions that occurred  within the called function,
    log function is used when provide
    :param func:
    :param log_func: example: logger = my_logger()
    :return:
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if log_func is not None:
                    error_info = traceback.format_exc() + str(e) + '\n'
                    log_func(f'\n>>>>>Exception in function <{func.__name__}> with description:\n' + error_info, **kw)

        return wrapper

    if func is None:
        return decorator
    else:
        return decorator(func)


# example use to log
@log_exception(log_func=to_log, filename='output.log', path=os.getcwd())
def example3_error(a):
    return a / 3


# decorator function for creating decorator
def decorator(declared_decorator):
    """
    create a decorator out of a function,which will be used as a wrapper.
    :param declared_decorator:
    :return:
    """

    @wraps(declared_decorator)
    def final_decorator(func=None, **kwargs):
        def decorated(func):
            @wraps(func)
            def wrapper(*a, **kw):
                return declared_decorator(func, a, kw, **kwargs)

            return wrapper

        if func is None:
            return decorated
        else:
            return decorated(func)

    return final_decorator


@decorator
def log_exceptions(func, args, kwargs, log_func=None):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        if log_func is not None:
            error_info = traceback.format_exc() + str(e) + '\n'
            log_func(f'\n>>>>>Exception in function <{func.__name__}> with description:\n' + error_info)


@decorator
def suppress_error(func, args, kwargs, log_func=None):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        error_info = traceback.format_exc() + str(e) + '\n'
        print(error_info)
        if log_func is not None:
            log_func(error_info)


# test_log_file = f'{time.strftime("%Y-%m-%d", time.localtime())}.log'
# test_logger = my_logger(log_file=test_log_file)


# example use my_logger
# @log_exceptions(log_func=test_logger.error)
def error_example(a):
    return a / 2


# count time
def deco_count_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_elapse = end_time - start_time
        print(f'Function {func.__name__:*^20} cost: {time_elapse:.4f} s')
        return result

    return wrapper


@deco_log_text(text='count prime', logfile='test.log')
# @deco_count_time
def get_prime(n: int = 100):
    """
    get all primes within n
    :param n:default n=100
    :return:
    """
    return [x for x in range(2, n + 1) if not [y for y in range(2, int(math.sqrt(x)) + 1) if x % y == 0]]


# find first 100 prime num
@deco_count_time
def find_n_prime(n: int = 100):
    x = 2
    num = 0
    prime_list = list()
    while True:
        x += 1
        for y in range(2, int(math.sqrt(x)) + 1):
            if x % y == 0:
                break
            else:
                if y == int(math.sqrt(x)):
                    # print(f'find a prime: {x}')
                    prime_list.append(x)
                    num += 1

        # print(f'now check: {x}')
        if num == n:
            # print(prime_list,len(prime_list))
            break
    return prime_list


# list to file with pandas
def list_to_csv(data: list, path, filename: str = 'test'):
    # check path
    if os.path.isdir(path):
        new_path = path
    else:
        new_path = os.getcwd()
    file_name = filename
    csvfile_in_path = os.path.join(new_path, file_name + '.csv')
    if data:
        pd_data = pd.Series(data)
        # print(pd_data)
        # write to csv
        pd_data.to_csv(csvfile_in_path)
        print('save to csv file successfully')
        # excel writer
        excelfile_in_path = os.path.join(new_path, file_name + '.xlsx')
        excel_writer = pd.ExcelWriter(excelfile_in_path)
        pd_data.to_excel(excel_writer)
        excel_writer.save()
        print('save to excel xlsx file successfully')


def get_time_interval(x: int = 1000):
    """
    x should be integer and x%100=0 \n
    find M,N,P when x==MN*10^P,X is the input time interval 100ms~100000ms with step of 100ms
    :param x:
    :return:command SET_COUNT_PRESET MN,P
    """
    SetInterval = 'SET_COUNT_PRESET'  # cmd <SET_COUNT_PRESET MN,P>
    x2 = int(x / 100)
    if x2 < 10:
        P = 1
        M = 0
        N = x2
    elif x2 > 10 or x2 == 10:
        P = int(math.log(x, 100))
        M = int(x / pow(10, P + 2))
        N = int((x / pow(10, P + 1)) % 10)
    command_str = SetInterval + ' %d%d,%d' % (M, N, P)
    return command_str


if __name__ == "__main__":
    pass
    # logger=my_logger()
    # prime_list = get_prime(2000)
    # print(len(prime_list))
    # n_prime = find_n_prime(20000)
    # print(n_prime)
    # print(f'last prime num: {n_prime[-1]}')
    # list_to_csv(n_prime,os.getcwd(),'prime20000')
    # logger = my_logger()
    # logger.info("get response %s", 'logging in')
    # print(get_time_interval(30000))
    b = error_example('9')
