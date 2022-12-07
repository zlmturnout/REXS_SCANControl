import os
import sqlite3

import pandas as pd


def create_path(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    os.chdir(file_path)
    return file_path


# by pandas.to_sql
def dict_to_DataFrame(data_dict: dict):
    """
    Transform dict form data to dataframe form and return
    :param data_dict:
    :return:
    """
    new_dict = dict()
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    for key,value in data_dict.items():
        if isinstance(value,list):
            num = len(value)
            new_dict[key] = pd.Series(list(data_dict[key]), index=list(range(num)))
    return pd.DataFrame(new_dict)


def dict_to_excel(data_dict: dict, path, filename):
    """
    save dict data to txt file in path/filename
    :param data_dict:
    :param dic:
    :param path:
    :param filename:
    :return:
    """
    m = 1
    new_dict = {}
    file_in_path = os.path.join(path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    pd_data = dict_to_DataFrame(data_dict)
    # excel writer
    with pd.ExcelWriter(file_in_path) as writer:
        pd_data.to_excel(writer)
    print('save to excel xlsx file successfully')


def dict_to_csv(data_dict: dict, path, filename: str = 'test.csv'):
    """
    save dict data to txt file in path/filename
    :param data_dict:
    :param path:
    :param filename: default='test.xlsx'
    :return:
    """
    # check path
    if os.path.isdir(path):
        new_path = path
    else:
        new_path = os.getcwd()
    m = 1
    new_dict = {}
    file_in_path = os.path.join(new_path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    pd_data = dict_to_DataFrame(data_dict)
    # excel writer
    pd_data.to_csv(file_in_path)
    print('save to csv file successfully')


def dict_to_json(data_dict: dict, path, filename: str = 'test.json'):
    """
    save dict data to txt file in path/filename
    :param data_dict:
    :param path:
    :param filename: default='test.xlsx'
    :return:
    """
    # check path
    if os.path.isdir(path):
        new_path = path
    else:
        new_path = os.getcwd()
    m = 1
    new_dict = {}
    file_in_path = os.path.join(new_path, filename)
    # change to the data from to standard dict {'key': pd.Series([list],index=[index])}
    pd_data = dict_to_DataFrame(data_dict)
    # excel writer
    pd_data.to_json(file_in_path)
    print('save to csv file successfully')


def dict_to_SQLTable(data_dict: dict, table_name: str, db_path: os.getcwd(), db_name: str = 'data.db'):
    """
        create a table containing dict_data in database=[db_path/db_name]
        :param data_dict: dict form data
        :param db_path: path to sqlite3 database
        :param db_name: database name default='data.db
        :param table_name: sql table name for dave
        :return: true if success,else false
        """
    status = True
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    # change data to dict form
    pd_data = dict_to_DataFrame(data_dict)
    # connect to database
    try:
        cxn = sqlite3.connect(sql_db)
        # cursor = cxn.cursor()
    except Exception as e:
        print(e)
        status = False
    else:
        pd_data.to_sql(name=table_name, con=cxn, if_exists='replace', index_label='id')
        cxn.commit()
        cxn.close()
    return status


def get_sql_tables(db_path, db_name):
    """
    get all tables from sqlite database
    :param db_path:
    :param db_name:
    :return:
    """
    table_list = []
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    sql_list_tables = "SELECT name FROM sqlite_master WHERE type= 'table' order by name"
    try:
        cxn = sqlite3.connect(sql_db)
        cursor = cxn.cursor()
    except Exception as e:
        print(e)
    else:
        cursor.execute(sql_list_tables)
        resp = cursor.fetchall()
        if not resp:
            print(f'cannot find any tables in:{sql_db} ')
        else:
            print(f'find record: {resp}')
            table_list = [item[0] for item in resp]
        cxn.commit()
        cxn.close()
    return table_list


def SQLTable_to_DataFrame(table_name, db_path, db_name):
    f"""
    extract one table{table_name} from database into pandas dataframe
    :param table_name:
    :param db_path:
    :param db_name:
    :return: pd data_frame data
    """
    pd_data = pd.DataFrame()
    if not os.path.exists(db_path):
        db_path = os.getcwd()
    sql_db = os.path.join(db_path, db_name)
    try:
        cxn = sqlite3.connect(sql_db)
        # cursor = cxn.cursor()
    except Exception as e:
        print(e)
    else:
        sql_select_table = f"SELECT * From {table_name}"
        pd_data = pd.read_sql(sql=sql_select_table, con=cxn)
        if pd_data.empty:
            print(f'cannot find any tables name{table_name} in:{sql_db} ')
        else:
            print(f'find record,will return')
        cxn.commit()
        cxn.close()
    return pd_data


def save_pd_data(pd_data: pd.DataFrame, path, filename: str):
    """
    save pandas DataForm data to excel/csv/json file by path/filename
    :param pd_data: pandas dataFrame
    :param path:
    :param filename:
    :return:
    """
    save_path = path
    if not os.path.isdir(path):
        save_path = os.getcwd()
    excel_file_path = os.path.join(save_path, filename + '.xlsx')
    # excel writer
    excel_writer = pd.ExcelWriter(excel_file_path)
    pd_data.to_excel(excel_writer)
    excel_writer.save()
    print(f'save to excel xlsx file {excel_file_path} successfully')
    # csv file
    csv_file_path = os.path.join(save_path, filename + '.csv')
    pd_data.to_csv(csv_file_path)
    print(f'save to csv file {csv_file_path} successfully')
    # json file
    json_file_path = os.path.join(save_path, filename + '.json')
    pd_data.to_json(json_file_path)
    print(f'save to json file {json_file_path} successfully')
