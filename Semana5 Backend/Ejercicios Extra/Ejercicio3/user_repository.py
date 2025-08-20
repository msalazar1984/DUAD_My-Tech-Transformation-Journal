import my_querys

class UserRepository:
    def __init__(self,db_manager):
        self.db_manager=db_manager
    

    def insert_fake_users(self,n=200):
        try:
            for _ in range(n):
                user=my_querys.generate_fake_user_data()
                query="""INSERT INTO lyfter_car_rental.users (name, useremail, username,password, date_birth, accountstatus) VALUES (%s,%s,%s,%s,%s,%s)"""
                params=(
                    user['Name'],
                    user['Useremail'],
                    user['Username'],
                    user['Password'],
                    user['Date_birth'],
                    user['Accountstatus'],
                )
                
                results=self.db_manager.execute_query(query,params)
            print("Users inserted succesfully!!!")
        except ValueError as err:
            return "Error inserting values in table Users"
    

    def get_min_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MIN(Id) FROM lyfter_car_rental.users;"
            )
            min_value=results[0][0]
            return min_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False


    def get_max_id(self):
        try:
            results = self.db_manager.execute_query(
                "SELECT MAX(Id) FROM lyfter_car_rental.users;"
            )
            max_value=results[0][0]
            return max_value
        except Exception as error:
            print(f'Error getting min value from user table', error)
            return False
