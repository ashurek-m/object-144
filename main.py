import functions.preparation as pr
import functions.support as sr


def open_df():
    number_order = input('Введите номер заказа: ')
    way = f'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\{number_order}\\**\\*xls'
    list_address = sr.file_search(way)
    if len(list_address) == 1:
        df_pay = pr.open_file(list_address[0][0],
                              list_address[0][1])
        return df_pay
    else:
        for i in range(len(list_address)):
            print(f'{i}, {list_address[i][0]}')
        number_file = int(input('Введите номер файла,\n который желаете загрузить: '))
        df_pay = pr.open_file(list_address[number_file][0],
                                  list_address[number_file][1])
        return df_pay


if __name__ in '__main__':
    df = open_df()
    df.info()
