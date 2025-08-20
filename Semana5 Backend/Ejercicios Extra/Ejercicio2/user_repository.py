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