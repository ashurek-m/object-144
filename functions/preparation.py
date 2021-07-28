import pandas as pd
import database.constant as const


def open_file(path, order):
    df = pd.read_excel(path, sheet_name='бланк для запуска', header=13)
    df = df.loc[:, 'Unnamed: 1': 'час']
    df.dropna(subset=['Unnamed: 1'], inplace=True)
    df = df.assign(order=order)
    df.set_axis(const.columns_for_excel, axis='columns', inplace=True)
    return df

'''
df = open_file('E:/new_project/object-144/database/39589 - Пеленг (7616).xls', 39589)
df.info()
print(df.tail(10))
'''