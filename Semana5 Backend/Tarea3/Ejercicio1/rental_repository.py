from db import PgManager


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
    


