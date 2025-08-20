from db import PgManager


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