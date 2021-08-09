import pandas as pd
import database.constant as const
import datetime as dt
import time


def open_file_pay(path, order):
    df = pd.read_excel(path, sheet_name='бланк для запуска', header=13)
    df = df.loc[:, 'Unnamed: 1': 'час']
    df = df[df['Unnamed: 1'] != '0']
    df.dropna(subset=['Unnamed: 1'], inplace=True)
    df = df.assign(order=order)
    df.set_axis(const.columns_for_excel, axis='columns', inplace=True)
    data_fin_str = '2021-08-15'
    #data_fin_str = input('Введите дату отгрузки\n'
                         #'в формате гггг-мм-дд: ')
    data_fin = time.mktime(time.strptime(data_fin_str, '%Y-%m-%d'))
    df = df.assign(data_fin_timestamp=data_fin)
    df = df.assign(data_fin=data_fin_str)
    return df


def open_file_ocp(path, order):
    df = pd.read_excel(path, sheet_name='бланк заказа для ОЦП', header=10)
    # df = df.loc[:, 'Unnamed: 1': 'час']
    # df.dropna(subset=['Unnamed: 1'], inplace=True)
    # df = df.assign(order=order)
    # df.set_axis(const.columns_for_excel, axis='columns', inplace=True)
    return df

df = open_file_pay('E:/new_project/object-144/database/39589 - Пеленг (7616).xls', 39589)
df.info()
print(df.head(10))
print(const.operation['control'], const.operation['package'])
