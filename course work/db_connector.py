import mysql.connector


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

    def select_data(self, list_data=None):
        try:
            self.mycursor = self.connection_db.cursor()
            if list_data is None:
                self.mycursor.execute(f'''SELECT * FROM {self.table_name}''')
                return self.mycursor.fetchall()
            elif len(list_data) == 0:
                return []
            else:
                res_str = ""
                for i in range(len(list_data)):
                    res_str += list_data[i]
                    if i != (len(list_data) - 1):
                        res_str += ", "
                self.mycursor.execute(f'''SELECT {res_str} FROM {self.table_name}''')
                return self.mycursor.fetchall()
            # for i in self.mycursor.fetchall():
            #     print("-/: ", i)
            # return self.mycursor.fetchall()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error: ", end=" ")
            print(ex)
        finally:
            self.mycursor.close()
            print("cursor closed")

    def insert_data(self, student_ext, **kwargs):
        try:
            columns_str = ""
            values_str = ""
            counter = 1
            for key in kwargs.keys():
                columns_str += key
                if counter != len(kwargs):
                    columns_str += ", "
                counter += 1

            counter = 1
            for key in kwargs.keys():
                values_str += '"' + kwargs[key] + '"'
                if counter != len(kwargs):
                    values_str += ", "
                counter += 1

            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''INSERT INTO {self.table_name} ({columns_str}) VALUES ({values_str});''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error(connector): ", ex)
            student_ext.error = ex

    def update_data(self, student_ext, dict_changed):
        try:
            columns_str = ""
            values_str = ""
            counter = 1
            for key in kwargs.keys():
                columns_str += key
                if counter != len(kwargs):
                    columns_str += ", "
                counter += 1

            counter = 1
            for key in kwargs.keys():
                values_str += '"' + kwargs[key] + '"'
                if counter != len(kwargs):
                    values_str += ", "
                counter += 1

            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''UPDATE {self.table_name} SET ({columns_str}) VALUES ({values_str}) WHERE ;''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error(connector): ", ex)
            student_ext.error = ex

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
