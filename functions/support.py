import csv
import glob


def csv_writer_spisok(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()


def file_search(way):
    way_list_xls = glob.glob(way, recursive=True)
    address_file_client = []
    for i in range(len(way_list_xls)):
        file_adrress_client = []
        name_file = way_list_xls[i].split("\\")
        try:
            if not 'рхив' in name_file[-2]:
                num_order = int(name_file[-1][:5])
                file_adrress_client.append(way_list_xls[i])
                file_adrress_client.append(num_order)
                address_file_client.append(file_adrress_client)
        except ValueError:
            continue
        print(address_file_client)
        return address_file_client


def search_by_client(address_file, year):
    file_csv = pd.read_csv(address_file, names=['path'])
    address_file_client = []
    file = file_csv.loc[:, 'path']
    for i in range(len(file)):
        file_adrress_client = []
        name_file = file[i].split("\\")
        try:
            if not 'рхив' in name_file[-2]:
                num_order = int(name_file[-1][:5])
                file_adrress_client.append(file[i])
                file_adrress_client.append(num_order)
                address_file_client.append(file_adrress_client)
        except ValueError:
            continue
    name = 'address_and_order_' + str(year) + '.csv'
    csv_writer(address_file_client, name)
    return name