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