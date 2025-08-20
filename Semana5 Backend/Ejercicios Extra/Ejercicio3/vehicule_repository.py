import my_querys


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