import pandas as pd


def open_file(path, order):
    df = pd.read_excel(path, sheet_name='бланк для запуска', header=13)
    df = df.loc[:, 'Unnamed: 1': 'час']
    df = df.assign(order=order)
    df.dropna(subset=['Unnamed: 1'], inplace=True)
    return df
