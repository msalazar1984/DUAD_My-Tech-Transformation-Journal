from repositories import UserRepository
from repositories import VehiculeRepository
from repositories import RentalRepository
from db import PgManager


def activate_users_repository():
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    users_repo=UserRepository(db_manager)
    return users_repo.checks_table_exists()


def activate_vehicule_repository():
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    vehicule_repo=VehiculeRepository(db_manager)
    return vehicule_repo.checks_table_exists()


def activate_rentals_repository():
    db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )
    
    rentals_repo=RentalRepository(db_manager)
    return rentals_repo.checks_table_exists()



    
