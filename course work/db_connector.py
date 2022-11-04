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

    def create_connection(self, student_ext):
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
            print("Error(connection):", ex)
            student_ext.error = ex
            raise Exception

    def select_data(self, student_ext, list_data=None):
        try:
            self.mycursor = self.connection_db.cursor()
            if list_data is None:
                self.mycursor.execute(f'''SELECT * FROM {self.table_name};''')
                return self.mycursor.fetchall()
            elif len(list_data) == 0:
                return []
            else:
                self.mycursor.execute(f'''SELECT {", ".join(list_data)} FROM {self.table_name};''')
                return self.mycursor.fetchall()
        except Exception as ex:
            student_ext.error = ex
            self.mycursor.close()
            self.connection_db.close()
            print("Error(select_data): ", end=" ")
            print(ex)
        finally:
            self.mycursor.close()
            print("cursor closed")

    def select_filtered_data(self, student_ext, column, value, list_data=None):
        try:
            self.mycursor = self.connection_db.cursor()
            if list_data is None:
                self.mycursor.execute(f'''SELECT * FROM {self.table_name} WHERE {column} LIKE "%{value}%";''')
                return self.mycursor.fetchall()

            elif len(list_data) == 0:
                return []
            else:
                self.mycursor.execute(f'''SELECT {", ".join(list_data)} FROM {self.table_name} 
                                            WHERE {column} LIKE "%{value}%";''')
                return self.mycursor.fetchall()
        except Exception as ex:
            student_ext.error = ex
            self.mycursor.close()
            self.connection_db.close()
            print("Error(filtered_data): ", ex)
            return []
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
            print("Error(insert_data): ", ex)
            student_ext.error = ex

    def update_data(self, student_ext, pk_ext, dict_changed):
        try:
            set_str = ""
            keys = list(dict_changed.keys())
            pk = list(pk_ext.keys())[0]
            for key in keys:
                set_str += key + "=" + "'" + dict_changed[key] + "'"
                if key != keys[-1]:
                    set_str += ", "

            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''UPDATE {self.table_name} SET {set_str} WHERE {pk}="{pk_ext[pk]}";''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error(update_data): ", ex)
            student_ext.error = ex

    def delete_data(self, student_ext, pk, value):
        try:
            self.mycursor = self.connection_db.cursor()
            self.mycursor.execute(f'''DELETE FROM {self.table_name} WHERE {pk}="{value}";''')
            self.mycursor.close()
            self.connection_db.commit()
        except Exception as ex:
            self.mycursor.close()
            self.connection_db.close()
            print("Error(delete_data): ", ex)
            student_ext.error = ex

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except Exception as ex:
            print(ex)
