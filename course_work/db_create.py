import mysql.connector
from mysql.connector import Error


class ConnectorDB:
    def __init__(self, host, user, password, db_name, table_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.table_name = table_name
        self.connection_db = None
        self.mycursor = None

    def create_connection(self):
        try:
            self.connection_db = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def select_data(self, *args):
        try:
            self.mycursor = self.connection_db.cursor()
            if len(args) == 0:
                self.mycursor.execute(f'''SELECT * FROM {self.table_name}''')
                for i in self.mycursor.fetchall():
                    print(i)
            else:
                res_str = ""
                for i in range(len(args)):
                    res_str += args[i]
                    if i != (len(args) - 1):
                        res_str += ", "
                self.mycursor.execute(f'''SELECT {res_str} FROM {self.table_name}''')
                for i in self.mycursor.fetchall():
                    print(i)
            self.mycursor.close()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error: ", end=" ")
            print(ex)

    def insert_data(self, **kwargs):
        try:
            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''INSERT INTO {self.table_name} (name, age, gender, nationally)
                    VALUES ("{kwargs["name"]}", "{kwargs["age"]}", "{kwargs["gender"]}", "{kwargs["nationally"]}");''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error: ", end=" ")
            print(ex)

    def delete_data(self, pk, value):
        try:
            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''DELETE FROM {self.table_name} WHERE {pk}="{value}";''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error: ", end=" ")
            print(ex)

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except Exception as ex:
            print(ex)
