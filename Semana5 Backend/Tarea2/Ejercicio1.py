import psycopg2

connection=psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="POSTGRES",
    dbname="postgres",
)

print("Connected to database!")

cursor=connection.cursor()
#a
cursor.execute("INSERT INTO lyfter_car_rental.users (Name,Useremail,Username,Password,Date_birth,Accountstatus) VALUES ('Laura Gómez','laura.gomez@gmail.com','laurag','f3Pvmbsb1HGBPxADpm','1988-09-22','activo');")
#b
cursor.execute("INSERT INTO lyfter_car_rental.vehicules (Brand_name,Model,Year,Condition) VALUES ('Toyota','Corolla','2018','Regular');")
#c
cursor.execute("UPDATE lyfter_car_rental.users SET Accountstatus='activo' WHERE Id='23';")
#d
cursor.execute("UPDATE lyfter_car_rental.vehicules SET Condition='Alquilado' WHERE Id='6';")
#e
cursor.execute("INSERT INTO lyfter_car_rental.rentals (User_ID,Vehicule_ID,End_rental,Status_rental,Pickup_Location,Delivery_Location) VALUES (43,34,'2025-07-24','En proceso','Ciudad de Mexico','Cancun');")
#f
cursor.execute("UPDATE lyfter_car_rental.vehicules SET Condition='Disponible' WHERE Id='34';")
cursor.execute("UPDATE lyfter_car_rental.rentals SET Status_rental='Completado' WHERE Vehicule_ID='34';")
#g
cursor.execute("UPDATE lyfter_car_rental.vehicules SET Condition='Deshabilitado' WHERE Id='20';")
#h
cursor.execute("SELECT lyfter_car_rental.vehicules.Id,lyfter_car_rental.vehicules.Brand_name, lyfter_car_rental.vehicules.Model, lyfter_car_rental.vehicules.Year,lyfter_car_rental.vehicules.Condition,lyfter_car_rental.rentals.status_rental FROM lyfter_car_rental.vehicules INNER JOIN lyfter_car_rental.rentals ON lyfter_car_rental.vehicules.Id=lyfter_car_rental.rentals.Vehicule_ID WHERE lyfter_car_rental.rentals.status_rental='En proceso' OR lyfter_car_rental.rentals.status_rental='Retrasado';")
results=cursor.fetchall()
print (results)
cursor.execute("SELECT lyfter_car_rental.vehicules.Id,lyfter_car_rental.vehicules.Brand_name, lyfter_car_rental.vehicules.Model, lyfter_car_rental.vehicules.Year,lyfter_car_rental.vehicules.Condition,lyfter_car_rental.rentals.status_rental FROM lyfter_car_rental.vehicules INNER JOIN lyfter_car_rental.rentals ON lyfter_car_rental.vehicules.Id=lyfter_car_rental.rentals.Vehicule_ID WHERE lyfter_car_rental.rentals.status_rental='En proceso' OR lyfter_car_rental.rentals.status_rental='Retrasado';")
results=cursor.fetchall()
print (results)

connection.commit()
cursor.close()
connection.close()