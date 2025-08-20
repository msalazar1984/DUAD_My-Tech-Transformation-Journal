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