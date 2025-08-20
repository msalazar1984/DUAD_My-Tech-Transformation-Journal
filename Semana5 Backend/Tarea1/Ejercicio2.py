import psycopg2

connection=psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="POSTGRES",
    dbname="postgres",
)

print("Connected to database!")

data_users=[
("Alejandro Gómez","alejandro.gomez@gmail.com","alejo123","T9$ks#8LdqwQ","12/4/1985","activo"),
("Lucía Martínez","lucia.martinez@yahoo.com","lucy_martinez","Xy#7P9%aWzL2","29/10/1992","suspendido"),
("Sergio Fernández","sergio.fernandez@hotmail.com","sergio_fer","Jw4!Vd*rPqMz","3/6/1979","pendiente"),
("Marta Ruiz","marta.ruiz@outlook.com","mruiz90","Pq8^Nb@aUeZ0","23/11/1990","verificado"),
("Andrés Torres","andres.torres@gmail.com","andrestorres","K#4Uy8B^JmPo","17/2/1988","activo"),
("Patricia Sánchez","patricia.sanchez@yahoo.com","psanchez88","H9!XqT*zFpLm","8/5/1995","bloqueado"),
("Juan Pérez","juan.perez@hotmail.com","jperez82","N7&fLp#XqZrW","1/12/1981","inactivo"),
("Isabel Díaz","isabel.diaz@outlook.com","idiaz23","Vy$T9Nz!QwAx","14/8/1983","activo"),
("Carlos Morales","carlos.morales@gmail.com","carlosm","Md2#KlPw7XoZ","30/1/1987","suspendido"),
("Laura Herrera","laura.herrera@yahoo.com","lauraherrera","Gk$7Qvx!TpRm","10/9/1991","pendiente"),
("Fernando Navarro","fernando.navarro@gmail.com","fernandn","Tp9#WqxYzL8A","24/7/1989","activo"),
("Andrea Morales","andrea.morales@yahoo.com","amorales15","Jx8!FpZ#vWo9","15/3/1993","verificado"),
("Jorge Castro","jorge.castro@hotmail.com","jcastro42","Nq#T92ZwLpRx","12/12/1986","suspendido"),
("Sonia Ortega","sonia.ortega@outlook.com","sortega","Vy@LpTw94Xq#","1/10/1990","activo"),
("Raúl Jiménez","raul.jimenez@gmail.com","rjimenez","Fx$7TPqLw9Vz","28/5/1984","bloqueado"),
("María Delgado","maria.delgado@yahoo.com","mdelgado88","QaX9#WyTzLp7","20/11/1992","pendiente"),
("Javier Ruiz","javier.ruiz@hotmail.com","jruiz53","Mq#TyX9VzLpW","6/4/1988","activo"),
("Sonia Vega","sonia.vega@outlook.com","sovega","Wx92#LpTvQAz","22/6/1994","inactivo"),
("Alberto Flores","alberto.flores@gmail.com","aflores","Ty#LpWqVzX9A","19/9/1987","activo"),
("Paula Reyes","paula.reyes@yahoo.com","preyes91","Zx9#WpTqLVyA","8/2/1983","verificado"),
("Diego Morales","diego.morales@hotmail.com","dmorales","Lp9#TqWxVzYA","5/8/1986","suspendido"),
("Claudia Herrera","claudia.herrera@outlook.com","cherrera","WqT9#LpVzXAy","14/12/1991","activo"),
("Andrés Castillo","andres.castillo@gmail.com","acastillo23","TyWpQz#LVx9A","20/3/1985","bloqueado"),
("Rosa González","rosa.gonzalez@yahoo.com","rgonzalez","Aq9TxLpWVzYA","29/7/1990","pendiente"),
("Hugo Navarro","hugo.navarro@hotmail.com","hnavarro","Qw9TpLzVXAY#","5/11/1989","activo"),
("Marta Vargas","marta.vargas@outlook.com","mvargas","YVzLp9WqTAX#","15/1/1987","inactivo"),
("Luis Romero","luis.romero@gmail.com","lromero","PxWt9LqVZAY#","31/10/1993","verificado"),
("Silvia Castro","silvia.castro@yahoo.com","scastro","ZyWVqLp9TAx#","9/6/1988","activo"),
("Ricardo Díaz","ricardo.diaz@hotmail.com","rdiaz","TpLWqVz9AY#x","12/12/1984","suspendido"),
("Carla Sánchez","carla.sanchez@outlook.com","csanchez","WqT9LpVzXAY#","21/5/1992","activo"),
("Jonathan Flores","jonathan.flores@gmail.com","jflores","VxLp9WqTAy#Z","16/9/1987","pendiente"),
("Elena Jiménez","elena.jimenez@yahoo.com","ejimenez","QWtLpVz9AYx#","4/3/1990","verificado"),
("Carlos Mendoza","carlos.mendoza@hotmail.com","cmendoza","TxLpWVq9AYZ#","12/11/1985","activo"),
("Diana Rivas","diana.rivas@outlook.com","drivas","ZyLp9WqTAx#V","20/8/1992","suspendido"),
("Mario Paredes","mario.paredes@gmail.com","mparedes","WxVqLp9TAZY#","3/1/1989","bloqueado"),
("Teresa Molina","teresa.molina@yahoo.com","tmolina","VqLpW9TxAYZ#","22/7/1994","pendiente"),
("Andrés Vargas","andres.vargas@hotmail.com","avargas","ZyLp9WqTAxV#","11/4/1986","activo"),
("Claudia Jiménez","claudia.jimenez@outlook.com","cjimenez","QLpWqVz9AYTx#","28/10/1991","inactivo"),
("Pablo Herrera","pablo.herrera@gmail.com","pHerrera","TxLpWVq9AYZ#x","15/2/1988","activo"),
("Lorena Ruiz","lorena.ruiz@yahoo.com","lruiz","ZyWVqLp9TAx#","30/6/1983","verificado"),
("Martín González","martin.gonzalez@hotmail.com","mgonzalez","TpLWqVz9AY#x","5/11/1987","activo"),
("Gabriela Ortiz","gabriela.ortiz@outlook.com","gortiz","WqT9LpVzXAY#","12/9/1990","suspendido"),
("Hugo Reyes","hugo.reyes@gmail.com","hreyes","VxLp9WqTAy#Z","19/2/1985","pendiente"),
("Sonia Rojas","sonia.rojas@yahoo.com","srojas","QWtLpVz9AYx#","23/4/1993","verificado"),
("Daniel Torres","daniel.torres@hotmail.com","dtorres","TxLpWVq9AYZ#","17/12/1989","activo"),
("Rosa Morales","rosa.morales@outlook.com","rmorales","ZyLp9WqTAx#V","14/7/1991","bloqueado"),
("Valeria Mendoza","valeria.mendoza@gmail.com","valemendo","Zk9@LwTpX8#Q","12/3/1986","activo"),
("Esteban Castillo","esteban.castillo@yahoo.com","estecast","Wp8#YqVzLX7!","25/7/1990","pendiente"),
("Camila Torres","camila.torres@hotmail.com","camitorres","TxVz9LpWA#Qx","5/10/1989","suspendido"),
("Nicolás Ramírez","nicolas.ramirez@outlook.com","nramirez","VqLpWTx9AYZ#","18/1/1992","bloqueado"),
("Juliana Herrera","juliana.herrera@gmail.com","jherrera","QLpWxVz9AYTx#","23/11/1987","verificado"),
]


cursor=connection.cursor()
cursor.execute("CREATE TABLE lyfter_car_rental.users(Id SERIAL PRIMARY KEY,Name VARCHAR(200),Useremail VARCHAR(254),Username VARCHAR(200),Password VARCHAR(30),Date_birth DATE, Accountstatus VARCHAR(100));")
cursor.executemany("""INSERT INTO lyfter_car_rental.users (Name,Useremail,Username,Password,Date_birth,Accountstatus) VALUES (%s, %s, %s,%s,%s,%s)""",data_users)
connection.commit()
cursor.close()
connection.close()
