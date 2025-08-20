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