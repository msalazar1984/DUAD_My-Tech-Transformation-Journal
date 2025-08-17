
import my_querys

class UserRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager
    

    def insert_fake_users(self,n=200):
        try:
            for _ in range(n):
                user=my_querys.generate_fake_user_data()
                query="""INSERT INTO lyfter_car_rental.users (name, useremail, username,password, date_birth, accountstatus) VALUES (%s,%s,%s,%s,%s,%s)"""
                params=(
                    user['Name'],
                    user['Useremail'],
                    user['Username'],
                    user['Password'],
                    user['Date_birth'],
                    user['Accountstatus'],
                )
                
                results=self.db_manager.execute_query(query,params)
            print("Users inserted succesfully!!!")
        except ValueError as err:
            return "Error inserting values in table Users"
    

    def get_min_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MIN(Id) FROM lyfter_car_rental.users;"
            )
            min_value=results[0][0]
            return min_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False


    def get_max_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MAX(Id) FROM lyfter_car_rental.users;"
            )
            max_value=results[0][0]
            return max_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False


class VehiculeRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    
    def insert_fake_vehicules(self,n=100):
        try:
            for _ in range(n):
                vehicule=my_querys.generate_fake_vehicule_data()
                query="""INSERT INTO lyfter_car_rental.vehicules (brand_name,model,year,condition) VALUES (%s,%s,%s,%s)"""
                params=(
                    vehicule['Brand_name'],
                    vehicule['Model'],
                    vehicule['Year'],
                    vehicule['Condition'],
                )
                
                results=self.db_manager.execute_query(query,params)
            print("Vehicules inserted succesfully!!!")
        except ValueError as err:
            return "Error inserting values in table Vehicules"
        
    
    def get_min_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MIN(Id) FROM lyfter_car_rental.vehicules;"
            )
            min_value=results[0][0]
            return min_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False


    def get_max_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MAX(Id) FROM lyfter_car_rental.vehicules;"
            )
            max_value=results[0][0]
            return max_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False
        

class RentalRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager


    def insert_fake_rentals(self,n=150):
        try:
            for _ in range(n):
                rental=my_querys.generate_fake_rentals_data()
                query="""INSERT INTO lyfter_car_rental.rentals (user_id,vehicule_id,start_rental,end_rental,status_rental,pickup_location,delivery_location) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                params=(
                    rental['User_ID'],
                    rental['Vehicule_ID'],
                    rental['Start_rental'],
                    rental['End_rental'],
                    rental['Status_rental'],
                    rental['Pickup_location'],
                    rental['Delivery_location'],
                )
                
                results=self.db_manager.execute_query(query,params)
                if results is None:
                    pass
            print("Rentals inserted succesfully!!!")
        except Exception as err:
            print(f'Error inserting values in table Rentals:{err}')
            return "Error inserting values in table Rentals"