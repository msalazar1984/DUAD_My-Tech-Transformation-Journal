import psycopg2

connection=psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="POSTGRES",
    dbname="postgres",
)

print("Connected to database!")

data_rentals=[
("1","1","18/7/2025  10:00:00","22/7/2025  10:00:00","En proceso","Los Angeles","Miami"),
("2","2","1/7/2025  14:00:00","10/7/2025  14:00:00","Completado","Toronto","Montreal"),
("3","3","15/7/2025  09:30:00","21/7/2025  09:30:00","En proceso","Ciudad de México","Guadalajara"),
("4","1","10/6/2025  12:00:00","15/6/2025  12:00:00","Completado","Vancouver","Vancouver"),
("5","2","12/7/2025  08:00:00","18/7/2025  08:00:00","Retrasado","Miami","New York"),
("6","5","20/7/2025  13:00:00","26/7/2025  13:00:00","En proceso","Cancún","Monterrey"),
("1","6","25/5/2025  10:00:00","30/5/2025  10:00:00","Completado","Ottawa","Toronto"),
("2","7","18/6/2025  15:00:00","23/6/2025  15:00:00","Cancelado","Houston","Houston"),
("3","4","2/7/2025  11:00:00","5/7/2025  11:00:00","Completado","Tijuana","Ciudad de México"),
("7","8","19/7/2025  09:00:00","24/7/2025  09:00:00","En proceso","New York","Chicago"),
("8","9","1/6/2025  10:00:00","6/6/2025  10:00:00","Completado","Montreal","Ottawa"),
("9","10","17/7/2025  17:00:00","21/7/2025  17:00:00","En proceso","Guadalajara","Cancún"),
("10","11","10/7/2025  09:00:00","14/7/2025  09:00:00","Completado","Chicago","Chicago"),
("11","12","6/7/2025  16:00:00","10/7/2025  16:00:00","Completado","Los Angeles","Tijuana"),
("12","3","15/7/2025  08:30:00","20/7/2025  08:30:00","En proceso","Calgary","Vancouver"),
("13","13","25/6/2025  10:00:00","30/6/2025  10:00:00","Cancelado","Ciudad de México","Guadalajara"),
("14","16","3/7/2025  13:00:00","8/7/2025  13:00:00","Completado","Vancouver","Montreal"),
("1","17","16/7/2025  12:00:00","23/7/2025  12:00:00","En proceso","Miami","Miami"),
("2","20","4/7/2025  11:30:00","10/7/2025  11:30:00","Completado","Monterrey","Monterrey"),
("15","21","8/7/2025  14:00:00","14/7/2025  14:00:00","Retrasado","Houston","Los Angeles"),
("5","22","18/7/2025  10:30:00","25/7/2025  10:30:00","En proceso","Guadalajara","Ciudad de México"),
("6","23","15/6/2025  10:00:00","20/6/2025  10:00:00","Completado","Toronto","Ottawa"),
("7","24","1/7/2025  09:00:00","6/7/2025  09:00:00","Completado","Calgary","Calgary"),
("16","2","13/7/2025  08:00:00","20/7/2025  08:00:00","En proceso","Cancún","Tijuana"),
("17","4","5/7/2025  12:00:00","11/7/2025  12:00:00","Completado","Chicago","New York"),
("18","5","17/7/2025  10:00:00","22/7/2025  10:00:00","En proceso","Vancouver","Ottawa"),
("19","6","20/6/2025  14:00:00","25/6/2025  14:00:00","Cancelado","Miami","Houston"),
("2","25","10/7/2025  16:00:00","14/7/2025  16:00:00","Completado","Tijuana","Tijuana"),
("4","26","7/7/2025  09:00:00","13/7/2025  09:00:00","Retrasado","Montreal","Toronto"),
("5","27","19/7/2025  11:00:00","24/7/2025  11:00:00","En proceso","New York","New York"),
("7","28","1/6/2025  08:00:00","5/6/2025  08:00:00","Completado","Ciudad de México","Cancún"),
("8","29","2/7/2025  15:00:00","6/7/2025  15:00:00","Completado","Los Angeles","San Diego"),
("20","30","14/7/2025  12:00:00","20/7/2025  12:00:00","En proceso","Ottawa","Toronto"),
("21","31","9/7/2025  13:00:00","12/7/2025  13:00:00","Completado","Houston","Chicago"),
("22","32","5/7/2025  10:00:00","11/7/2025  10:00:00","Retrasado","Vancouver","Calgary"),
("23","4","20/7/2025  09:00:00","26/7/2025  09:00:00","En proceso","Guadalajara","Monterrey"),
("25","5","5/6/2025  13:00:00","10/6/2025  13:00:00","Completado","Chicago","Chicago"),
("26","6","15/6/2025  14:00:00","18/6/2025  14:00:00","Cancelado","Tijuana","Los Angeles"),
("27","7","3/7/2025  10:00:00","8/7/2025  10:00:00","Completado","New York","Miami"),
("28","50","17/7/2025  09:00:00","22/7/2025  09:00:00","En proceso","Toronto","Vancouver"),
("29","48","10/6/2025  12:00:00","15/6/2025  12:00:00","Completado","Monterrey","Ciudad de México"),
("30","49","13/7/2025  11:00:00","20/7/2025  11:00:00","En proceso","Calgary","Ottawa"),
("31","50","4/7/2025  08:00:00","9/7/2025  08:00:00","Completado","Miami","Houston"),
("2","5","15/7/2025  15:00:00","21/7/2025  15:00:00","En proceso","Vancouver","Montreal"),
("3","4","8/7/2025  14:30:00","13/7/2025  14:30:00","Completado","Los Angeles","San Diego"),
("4","10","18/7/2025  16:00:00","23/7/2025  16:00:00","En proceso","Ottawa","Ottawa"),
("50","11","6/7/2025  09:00:00","12/7/2025  09:00:00","Retrasado","Cancún","Guadalajara"),
("49","12","11/7/2025  12:00:00","16/7/2025  12:00:00","Completado","Toronto","Toronto"),
("48","20","19/7/2025  10:00:00","25/7/2025  10:00:00","En proceso","Tijuana","Tijuana"),
("47","21","12/7/2025  09:00:00","18/7/2025  09:00:00","Retrasado","Montreal","Calgary"),
]


cursor=connection.cursor()
cursor.execute("CREATE TABLE lyfter_car_rental.rentals(Id SERIAL PRIMARY KEY,User_ID INTEGER REFERENCES lyfter_car_rental.users(id),Vehicule_ID INTEGER REFERENCES lyfter_car_rental.vehicules(Id),Start_rental TIMESTAMP DEFAULT CURRENT_TIMESTAMP,End_rental DATE,Status_rental VARCHAR(100),Pickup_Location VARCHAR(100),Delivery_Location VARCHAR(100));")
cursor.executemany("""INSERT INTO lyfter_car_rental.rentals (User_ID,Vehicule_ID,Start_rental,End_rental,Status_rental,Pickup_Location,Delivery_Location) VALUES (%s, %s, %s,%s,%s,%s,%s)""",data_rentals)
connection.commit()
cursor.close()
connection.close()