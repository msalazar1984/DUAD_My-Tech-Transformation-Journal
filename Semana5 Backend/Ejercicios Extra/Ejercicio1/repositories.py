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


    def get_all(self):
        try:
            query="Select * FROM lyfter_car_rental.users;"
        
            results=self.db_manager.execute_query(query)
            formatted_results=[self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []


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
    
    def get_all(self):
        try:
            query="Select * FROM lyfter_car_rental.vehicules"
        
            results=self.db_manager.execute_query(query)
            formatted_results=[self._format_rental(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []


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
    
    def get_all(self):
        try:
            query="Select * FROM lyfter_car_rental.rentals"
        
            results=self.db_manager.execute_query(query)
            formatted_results=[self._format_rental(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []