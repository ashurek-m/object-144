import functions.preparation as pr
import functions.support as sr


if __name__ in '__main__':
    numder_order = (input('Введите номер заказа: '))
    way = f'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\{numder_order}\\**\\*xls'
    list_address = sr.file_search(way)
    if len(list_address) == 1:
        df_pay = pr.open_file(list_address[0],
                          int(numder_order))
    else:
        for i in range(len(list_address)):
            print(f'{i}, {list_address[i, 0]}')
    #df_pay.info()
    #print(df_pay.head(10))
