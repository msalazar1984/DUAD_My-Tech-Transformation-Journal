import csv


def export_file(my_database,headers,file_path):
    with open(file_path,mode='w',encoding='utf-8') as file:
        writer=csv.DictWriter(file,headers)
        writer.writeheader()
        writer.writerows(my_database)


def read_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        first_row = next(reader, None)
        return first_row is None   