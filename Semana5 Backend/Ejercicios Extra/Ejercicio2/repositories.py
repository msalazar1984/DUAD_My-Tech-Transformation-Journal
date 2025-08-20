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


    def checks_table_exists(self):
        try:
            query="SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema= 'lyfter_car_rental' AND table_name= 'users');"
        
            results=self.db_manager.execute_query(query)
            if results and results[0]:
                return "Users table exists!!!"
            else:
                raise ValueError
        except ValueError as err:
            return "Users table does not exist!!!"



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
    

    def checks_table_exists(self):
        try:
            query="SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema= 'lyfter_car_rental' AND table_name= 'vehicule');"
        
            results=self.db_manager.execute_query(query)
            if results and results[0]:
                return "Vehicule table exists!!!"
            else:
                raise ValueError
        except ValueError as err:
            return "Vehicule table does not exist!!!"
            


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
    

    def checks_table_exists(self):
        try:
            query="SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_schema= 'lyfter_car_rental' AND table_name= 'rentals');"
        
            results=self.db_manager.execute_query(query)
            if results and results[0]:
                return "Rentals table exists!!!"
            else:
                raise ValueError
        except ValueError as err:
            return "Rentals table does not exist!!!"