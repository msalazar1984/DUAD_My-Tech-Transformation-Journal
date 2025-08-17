import psycopg2

class PgManager:
    def __init__(self,db_name,user,password,host,port=5432):
        self.db_name=db_name
        self.user=user
        self.password=password
        self.host=host
        self.port=port

        self.connection=self.create_connection(db_name,user,password,host,port)
        if self.connection:
            self.cursor=self.connection.cursor()
            print("Connection created succesfully")
    

    def create_connection(self,db_name,user,password,host,port):
        try:
            connection=psycopg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host,
                port=port,
            )
            return connection
        except Exception as error:
            print("Error connecting to the database:",error)
            return None
    

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed")
    
    
    def execute_query(self,query,params=None):
        try:
            if params is None:
                params=()
            self.cursor.execute(query,params)
    
            #Revisamos si el query devolvio algo
            if self.cursor.description:
                results=self.cursor.fetchall()
                return results
            else:
                self.connection.commit()
                return None
        except Exception as e:
            print(f'Error in execute_query:{e}')
            self.connection.rollback()
            return None