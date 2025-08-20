from db import PgManager

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
    

    def create(self,name,useremail,username,password,date_birth,accountstatus):
        try:
            self.db_manager.execute_query(
                "INSERT INTO lyfter_car_rental.users (name,useremail,username,password,date_birth,accountstatus) VALUES (%s,%s,%s,%s,%s,%s)",
                (name,useremail,username,password,date_birth,accountstatus),
            )
            print("User inserted succesfully")
            return True
        except Exception as error:
            print("Error getting all users from the database: ",error)
            return False
    

    def count_by_email(self, useremail):
        try:
            results = self.db_manager.execute_query(
                "SELECT COUNT(*) FROM lyfter_car_rental.users WHERE Useremail = %s;",
                (useremail,),
            )
            count=results[0][0]
            return count
        except Exception as error:
            print("Error getting a user from the database: ", error)
            return False
    

    def get_all(self,id_filter=None,name_filter=None,email_filter=None,username_filter=None,password_filter=None,date_birth_filter=None,accountstatus_filter=None):
        try:
            query="Select * FROM lyfter_car_rental.users WHERE 1=1"
            params=[]
            if id_filter is not None:
                query+= " AND Id = %s"
                params.append(id_filter)
            if name_filter is not None:
                query+= " AND Name = %s"
                params.append(name_filter)
            if email_filter is not None:
                query+= " AND Useremail = %s"
                params.append(email_filter)
            if username_filter is not None:
                query+= " AND Username = %s"
                params.append(username_filter)
            if password_filter is not None:
                query+= " AND Password = %s"
                params.append(password_filter)
            if date_birth_filter is not None:
                query+= " AND Date_birth = %s"
                params.append(date_birth_filter)
            if accountstatus_filter is not None:
                query+= " AND Accountstatus = %s"
                params.append(accountstatus_filter)
            results=self.db_manager.execute_query(query,params)

            formatted_results=[self._format_user(result) for result in results]
            return formatted_results
        except Exception as error:
            print("No se encontraron registros en la tabla especificada")
            return []
    

    def count_by_id(self, id):
        try:
            results = self.db_manager.execute_query(
                "SELECT COUNT(*) FROM lyfter_car_rental.users WHERE Id = %s;",
                (id,),
            )
            count=results[0][0]
            return count
        except Exception as error:
            print(f'Error getting an user from the database, user {id} does not exist: ', error)
            return False
        
    def update_user(self,accountstatus,id):
        try:
            self.db_manager.execute_query(
                'UPDATE lyfter_car_rental.users SET Accountstatus = %s WHERE Id = %s',
                (accountstatus,id),
            )
            print("User updated successfully")
            return True
        except Exception as error:
            print("Error updating an user from the database: ", error)
            return False