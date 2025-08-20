import psycopg2

connection=psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="POSTGRES",
    dbname="postgres",
)

print("Connected to database!")

data_vehicules=[
("Toyota","Corolla","2021","Disponible"),
("Ford","Focus","2022","Alquilado"),
("Honda","Civic","2020","En mantenimiento"),
("Toyota","Corolla","2019","Disponible"),
("Ford","Focus","2023","Alquilado"),
("Honda","Civic","2021","Reservado"),
("Toyota","Corolla","2022","En limpieza"),
("Ford","Focus","2020","Deshabilitado"),
("Honda","Civic","2023","Alquilado"),
("Toyota","Corolla","2019","En mantenimiento"),
("Ford","Focus","2019","Reservado"),
("Honda","Civic","2020","Disponible"),
("Toyota","Corolla","2022","En limpieza"),
("Ford","Focus","2023","Alquilado"),
("Honda","Civic","2019","Disponible"),
("Toyota","Corolla","2021","En mantenimiento"),
("Ford","Focus","2020","Deshabilitado"),
("Honda","Civic","2023","Reservado"),
("Toyota","Corolla","2022","Disponible"),
("Ford","Focus","2019","En limpieza"),
("Honda","Civic","2020","Alquilado"),
("Toyota","Corolla","2021","Disponible"),
("Ford","Focus","2023","Reservado"),
("Honda","Civic","2019","Disponible"),
("Toyota","Corolla","2022","En mantenimiento"),
("Ford","Focus","2020","En limpieza"),
("Honda","Civic","2021","Disponible"),
("Toyota","Corolla","2019","Alquilado"),
("Ford","Focus","2023","En mantenimiento"),
("Honda","Civic","2022","Deshabilitado"),
("Toyota","Corolla","2019","Reservado"),
("Ford","Focus","2021","Disponible"),
("Honda","Civic","2023","Alquilado"),
("Toyota","Corolla","2020","En limpieza"),
("Ford","Focus","2019","En mantenimiento"),
("Honda","Civic","2022","Disponible"),
("Toyota","Corolla","2021","Alquilado"),
("Ford","Focus","2020","En limpieza"),
("Honda","Civic","2020","Disponible"),
("Toyota","Corolla","2023","Deshabilitado"),
("Ford","Focus","2021","Reservado"),
("Honda","Civic","2022","Disponible"),
("Toyota","Corolla","2020","En limpieza"),
("Ford","Focus","2019","Disponible"),
("Honda","Civic","2021","Alquilado"),
("Toyota","Corolla","2023","Disponible"),
("Ford","Focus","2022","En mantenimiento"),
("Honda","Civic","2020","Disponible"),
("Toyota","Corolla","2019","Reservado"),
("Ford","Focus","2021","Deshabilitado"),
]


cursor=connection.cursor()
cursor.execute("CREATE TABLE lyfter_car_rental.vehicules(Id SERIAL PRIMARY KEY,Brand_name VARCHAR(100),Model VARCHAR(100),Year INTEGER,Condition VARCHAR(75));")
cursor.executemany("""INSERT INTO lyfter_car_rental.vehicules (Brand_name,Model,Year,Condition) VALUES (%s, %s, %s,%s)""",data_vehicules)
connection.commit()
cursor.close()
connection.close()
