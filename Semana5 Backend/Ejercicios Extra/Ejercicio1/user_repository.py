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