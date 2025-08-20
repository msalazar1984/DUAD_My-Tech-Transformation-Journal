from db import PgManager

class UserRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager
    

    def _format_user(self,user_record):
        return {
            "Id": user_record[0],
            "Name": user_record[1],
            "Useremail": user_record[2],
            "Username": user_record[3],
            "Password": user_record[4],
            "Date_birth": user_record[5],
            "Accountstatus": user_record[6],
        } 
    

    def create(self,name,useremail,username,password,date_birth,accountstatus):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (name,useremail,username,password,date_birth,accountstatus) VALUES (%s,%s,%s,%s,%s,%s)",
                (name,useremail,username,password,date_birth,accountstatus),
            )
            print("User inserted succesfully")
            return True
        except Exception as error:
            print("Error getting all users from the database: ",error)
            return False
    

    def count_by_email(self, useremail):
        try:
            results = self.db_manager.execute_query(
                "SELECT COUNT(*) FROM lyfter_car_rental.users WHERE Useremail = %s;",
                (useremail,),
            )
            count=results[0][0]
            return count
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
    

    def get_all(self,id_filter=None,name_filter=None,email_filter=None,username_filter=None,password_filter=None,date_birth_filter=None,accountstatus_filter=None):
        try:
            query="Select * FROM lyfter_car_rental.users WHERE 1=1"
            params=[]
            if id_filter is not None:
                query+= " AND Id = %s"
                params.append(id_filter)
            if name_filter is not None:
                query+= " AND Name = %s"
                params.append(name_filter)
            if email_filter is not None:
                query+= " AND Useremail = %s"
                params.append(email_filter)
            if username_filter is not None:
                query+= " AND Username = %s"
                params.append(username_filter)
            if password_filter is not None:
                query+= " AND Password = %s"
                params.append(password_filter)
            if date_birth_filter is not None:
                query+= " AND Date_birth = %s"
                params.append(date_birth_filter)
            if accountstatus_filter is not None:
                query+= " AND Accountstatus = %s"
                params.append(accountstatus_filter)
            results=self.db_manager.execute_query(query,params)

            formatted_results=[self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []
    

    def count_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT COUNT(*) FROM lyfter_car_rental.users WHERE Id = %s;",
                (id,),
            )
            count=results[0][0]
            return count
        except Exception as error:
            print(f'Error getting an user from the database, user {id} does not exist: ', error)
            return False
        
    def update_user(self,accountstatus,id):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental.users SET Accountstatus = %s WHERE Id = %s',
                (accountstatus,id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating an user from the database: ", error)
            return False


class VehiculeRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    
    def _format_vehicule(self,vehicule_record):
        return{
            "Id": vehicule_record[0],
            "Brand_name": vehicule_record[1],
            "Model": vehicule_record[2],
            "Year": vehicule_record[3],
            "Condition": vehicule_record[4],
        }
    

    def get_all(self,id_filter=None,brandname_filter=None,model_filter=None,year_filter=None,condition_filter=None):
        try:
            query="Select * FROM lyfter_car_rental.vehicules WHERE 1=1"
            params=[]
            if id_filter is not None:
                query+= " AND Id = %s"
                params.append(id_filter)
            if brandname_filter is not None:
                query+= " AND Brand_name = %s"
                params.append(brandname_filter)
            if model_filter is not None:
                query+= " AND Model = %s"
                params.append(model_filter)
            if year_filter is not None:
                query+= " AND Year = %s"
                params.append(year_filter)
            if condition_filter is not None:
                query+= " AND Condition = %s"
                params.append(condition_filter)
            print(query)
            results=self.db_manager.execute_query(query,params)

            formatted_results=[self._format_vehicule(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []


    def create(self,brandname,model,year,condition):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.vehicules (Brand_name,Model,Year,Condition) VALUES (%s,%s,%s,%s)",
                (brandname,model,year,condition),
            )
            print("Vehicule inserted succesfully")
            return True
        except Exception as error:
            print("Error getting all Vehicules from the database: ",error)
            return False
    

    def count_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT COUNT(*) FROM lyfter_car_rental.vehicules WHERE Id = %s;",
                (id,),
            )
            count=results[0][0]
            return count
        except Exception as error:
            print(f'Error getting a vehicule from the database, the vehicule {id} does not exist: ', error)
            return False
    

    def get_by_status(self,id):
        try:
            results=self.db_manager.execute_query(
                "Select Condition FROM lyfter_car_rental.vehicules WHERE Id = %s;",
                (id,),
            )
            return results[0][0]
        except Exception as error:
            print (f'Error getting condition from the database, the vehicule {id} does not exist: ', error)
            return False


    def update(self, condition,id):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental.vehicules SET condition = %s WHERE Id = %s',
                (condition,id),
            )
            print("Vehicule updated successfully")
            return True
        except Exception as error:
            print("Error updating a user from the database: ", error)
            return False
    

class RentalRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager

    
    def _format_rental(self,rental_record):
        return{
            "Id": rental_record[0],
            "User_ID": rental_record[1],
            "Vehicule_ID": rental_record[2],
            "Start_rental": rental_record[3],
            "End_rental": rental_record[4],
            "Status_rental": rental_record[5],
            "Pickup_location": rental_record[6],
            "Delivery_location": rental_record[7],
        }
    

    def get_all(self,id_filter=None,userid_filter=None,vehiculeid_filter=None,startrental_filter=None,endrental_filter=None,statusrental_filter=None,pickuplocation_filter=None,deliverylocation_filter=None):
        try:
            query="Select * FROM lyfter_car_rental.rentals WHERE 1=1"
            params=[]
            if id_filter is not None:
                query+= " AND Id = %s"
                params.append(id_filter)
            if userid_filter is not None:
                query+= " AND User_ID = %s"
                params.append(userid_filter)
            if vehiculeid_filter is not None:
                query+= " AND Vehicule_ID = %s"
                params.append(vehiculeid_filter)
            if startrental_filter is not None:
                query+= " AND Start_rental = %s"
                params.append(startrental_filter)
            if endrental_filter is not None:
                query+= " AND End_rental = %s"
                params.append(endrental_filter)
            if statusrental_filter is not None:
                query+= " AND Status_rental = %s"
                params.append(statusrental_filter)
            if pickuplocation_filter is not None:
                query+= " AND Pickup_location = %s"
                params.append(pickuplocation_filter)
            if deliverylocation_filter is not None:
                query+= " AND Delivery_location = %s"
                params.append(deliverylocation_filter)
            print(query)
            results=self.db_manager.execute_query(query,params)
            formatted_results=[self._format_rental(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []


    def create(self,user_id,vehicule_id,start_rental,end_rental,status_rental,pickup_location,delivery_location):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.rentals (User_ID,Vehicule_ID,Start_rental,End_rental,Status_rental, Pickup_location,Delivery_location) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                (user_id,vehicule_id,start_rental,end_rental,status_rental,pickup_location,delivery_location),
            )
            print("Rental inserted succesfully")
            return True
        except Exception as error:
            print("Error getting all rentals from the database: ",error)
            return False
    

    def update_rental(self,status_rental,end_date,id):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental.rentals SET Status_rental = %s,End_rental=%s WHERE Id = %s',
                (status_rental,end_date,id),
            )
            print("Rental updated successfully")
            return True
        except Exception as error:
            print("Error updating a rental from the database: ", error)
            return False
    

    def get_by_id(self,id):
        try:
            results=self.db_manager.execute_query(
                "Select Vehicule_ID FROM lyfter_car_rental.rentals WHERE Id = %s;",
                (id,),
            )
            return results[0][0]
        except Exception as error:
            print (f'Error getting condition from the database, the rental {id} does not exist: ', error)
            return False
    

    def get_by_status(self,id):
        try:
            results=self.db_manager.execute_query(
                "Select Status_rental FROM lyfter_car_rental.rentals WHERE Id = %s;",
                (id,),
            )
            return results[0][0]
        except Exception as error:
            print (f'Error getting condition from the database, the rental {id} does not exist: ', error)
            return False
    


