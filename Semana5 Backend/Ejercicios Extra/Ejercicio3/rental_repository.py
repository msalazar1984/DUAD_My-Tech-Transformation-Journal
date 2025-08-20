import my_querys

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