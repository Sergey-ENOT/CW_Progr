from db_connector import ConnectorDB
from config import host, user, password, db_name


connection_test_db = ConnectorDB(host, user, password, db_name, "users")

connection_test_db.create_connection()
# connection_test_db.insert_data(name="Evgen", age=45, gender="male", nationally="rus")
# connection_test_db.delete_data("name", "Igor")
connection_test_db.select_data()
# connection_test_db.select_data("id", "name", "age", "gender", "nationally")
connection_test_db.close_connection()
