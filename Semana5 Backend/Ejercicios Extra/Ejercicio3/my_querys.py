from repositories import UserRepository
from repositories import VehiculeRepository
from repositories import RentalRepository
from db import PgManager
from faker import Faker
import random
from datetime import timedelta
from datetime import datetime

fake=Faker()

db_manager=PgManager(
    db_name="postgres",
    user="postgres",
    password="POSTGRES",
    host="localhost"
    )

def generate_fake_user_data():
    return {
                "Name": fake.name(),
                "Useremail": fake.email(),
                "Username": fake.user_name(),
                "Password": fake.password(length=10),
                "Date_birth": fake.date_of_birth(minimum_age=18, maximum_age=75),
                "Accountstatus": fake.random_element(['activo','pendiente','verificado','pendiente','bloqueado'])
    }


def inserting_fake_users():
    users_repo=UserRepository(db_manager)
    users_repo.insert_fake_users()


def generate_fake_vehicule_data():
    brand_model_map={
        "Toyota":["Corolla","RAV4"],
        "Ford":  ["Ranger","Fiesta","Focus"],
        "Honda": ["Civic","Accord"]
    }
    brand=random.choice(list(brand_model_map.keys()))
    model=random.choice(brand_model_map[brand])
    year=random.randint(2018,2024)
    condition=fake.random_element(['Reservado','Entregado','En Mantenimiento','Reservado','Alquilado','En limpieza','Deshabilitado'])

    return {
                "Brand_name": brand,
                "Model": model,
                "Year": year,
                "Condition": condition
    }


def inserting_fake_vehicules():
    vehicule_repo=VehiculeRepository(db_manager)
    vehicule_repo.insert_fake_vehicules()


def generate_fake_rentals_data():
    users_repo=UserRepository(db_manager)
    vehicules_repo=VehiculeRepository(db_manager)
    min_user=users_repo.get_min_id()
    max_user=users_repo.get_max_id()
    min_vehicule=vehicules_repo.get_min_id()
    max_vehicule=vehicules_repo.get_max_id()

    starting_date=fake.date_between(start_date=datetime.strptime('2018-01-01', '%Y-%m-%d').date(),end_date=datetime.strptime('2024-12-31', '%Y-%m-%d').date())
    ending_date=starting_date + timedelta(days=random.randint(1,22))
    north_american_cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix","Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose","Toronto", "Montreal", "Vancouver", "Calgary", "Ottawa","Edmonton", "Quebec City", "Winnipeg", "Hamilton", "Victoria","Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Tijuana","León", "Juárez", "Toluca", "Querétaro", "Mérida"]


    return {
                "User_ID": random.randint(min_user,max_user),
                "Vehicule_ID": random.randint(min_vehicule,max_vehicule),
                "Start_rental": starting_date,
                "End_rental":ending_date,
                "Status_rental": fake.random_element(['Completado','Cancelado']),
                "Pickup_location": fake.random_element(north_american_cities),
                "Delivery_location": fake.random_element(north_american_cities)
    }


def inserting_fake_rentals():
    rental_repo=RentalRepository(db_manager)
    rental_repo.insert_fake_rentals()


