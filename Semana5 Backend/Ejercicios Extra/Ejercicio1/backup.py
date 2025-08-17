from repositories import UserRepository
from repositories import VehiculeRepository
from repositories import RentalRepository
from db import PgManager
import csv
from datetime import date
import os


def  backup_users():
    
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    users_repo=UserRepository(db_manager)
    return users_repo.get_all()


def  backup_vehicules():
    
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    vehicules_repo=VehiculeRepository(db_manager)
    return vehicules_repo.get_all()


def  backup_rentals():
    
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    rentals_repo=RentalRepository(db_manager)
    return rentals_repo.get_all()


def writting_to_csv_users():
    try:
        my_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/db_backups"
        my_users_values=backup_users()
        if len(my_users_values)>0:
            headers=my_users_values[0].keys()
            my_file_path=f'{my_path}/usersbackup_{date.today()}.csv'
            os.makedirs(my_path,exist_ok=True)
            with open(my_file_path,mode='w',encoding='utf-8') as file:
                writer=csv.DictWriter(file,headers)
                writer.writeheader()
                writer.writerows(my_users_values)
        else:
            raise ex
    except ValueError as ex:
        print("El archivo se encuentra vacio")


def writting_to_csv_vehicules():
    try:
        my_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/db_backups"
        my_vehicules_values=backup_vehicules()
        if len(my_vehicules_values)>0:
            headers=my_vehicules_values[0].keys()
            my_file_path=f'{my_path}/vehiculesbackup_{date.today()}.csv'
            os.makedirs(my_path,exist_ok=True)
            with open(my_file_path,mode='w',encoding='utf-8') as file:
                writer=csv.DictWriter(file,headers)
                writer.writeheader()
                writer.writerows(my_vehicules_values)
        else:
            raise ex
    except ValueError as ex:
        print("El archivo se encuentra vacio")

def writting_to_csv_rentals():
    try:
        my_path="C:/Users/default.LAPTOP-SHSSKNRP/OneDrive/INVERSIONES/Escritorio/db_backups"
        my_rentals_values=backup_rentals()
        if len(my_rentals_values)>0:
            headers=my_rentals_values[0].keys()
            my_file_path=f'{my_path}/rentalsbackup_{date.today()}.csv'
            os.makedirs(my_path,exist_ok=True)
            with open(my_file_path,mode='w',encoding='utf-8') as file:
                writer=csv.DictWriter(file,headers)
                writer.writeheader()
                writer.writerows(my_rentals_values)
        else:
            raise ex
    
    except ValueError as ex:
        print("El archivo se encuentra vacio")



