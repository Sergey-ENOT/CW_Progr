import mysql.connector
from mysql.connector import Error
from config import host, user, password, db_name


def create_connection_mysql_db(host, user, password, db_name=None):
    connection_db = None
    try:
        connection_db = mysql.connector.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
        )
        print("Successfully connected...")
        print("#" * 20)
        mycursor = connection_db.cursor()
        # mycursor.execute('''SELECT * FROM actor WHERE first_name = "NICK";''')
        # for i in mycursor.fetchall():
        #     print(i)
        print("-" * 20)

        mycursor.execute("show tables;")
        for i in [tables[0] for tables in mycursor.fetchall()]:
            print(i)
        print("-" * 20)
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT,
            name TEXT NOT NULL,
            age INT,
            gender TEXT,
            nationally TEXT,
            PRIMARY KEY (id)
            ) ENGINE=INNODB;
            '''
        mycursor.execute(create_table_query)
        connection_db.commit()
        print("/" * 20)
        delete_usa_users_query = '''
            truncate users;
            '''
        mycursor.execute(delete_usa_users_query)
        connection_db.commit()
        print("/" * 20)
        insert_users_table_query = '''
            INSERT
            users (name, age, gender, nationally)
            VALUES
            ('James', 25, 'male', 'USA'),
            ('Leila', 32, 'female', 'France'),
            ('Brigitte', 35, 'female', 'England');
            '''
        mycursor.execute(insert_users_table_query)
        connection_db.commit()
        mycursor.close()
        print("/" * 20)
    except Exception as ex:
        print("Connection refused...")
        print(ex)
    finally:
        connection_db.close()


create_connection_mysql_db(host, user, password, db_name)


# def create_db(host, user, password, db_name):
#     conn = create_connection_mysql_db(host, user, password, db_name)
#     cursor = conn.cursor()
#     create_db_sql_query = 'CREATE DATABASE IF NOT EXISTS {}'.format('Test')
#     cursor.execute(create_db_sql_query)
#     cursor.close()
#     conn.close()
#
#
# create_db(host, user, password, db_name)
#
# try:
#     conn = create_connection_mysql_db(host, user, password, 'Test')
#     cursor = conn.cursor()
#     create_table_query = '''
#     CREATE TABLE IF NOT EXISTS users(
#     id INT AUTO_INCREMENT,
#     name TEXT NOT NULL,
#     age INT,
#     gender TEXT,
#     nationally TEXT,
#     PRIMARY KEY (id)
#     ) ENGINE = InnoDB
#     '''
#     cursor.execute(create_table_query)
#     conn.commit()
#
#     insert_users_table_query = '''
#     INSERT INTO
#     users (name, age, gender, nationally)
#     VALUES
#     ('James', 25, 'male', 'USA'),
#     ('Leila', 32, 'female', 'France'),
#     ('Brigitte', 35, 'female', 'England');
#     '''
#     cursor.execute(insert_users_table_query)
#     conn.commit()
#
#     select_users_female_query = '''
#     SELECT * FROM users;
#     '''
#     cursor.execute(select_users_female_query)
#     query_result = cursor.fetchall()
#     print(query_result)
#     for user in query_result:
#         print(user)
#
#     update_user_gender_query = '''
#     UPDATE users SET gender = 'deer' WHERE gender = 'male';
#     '''
#     cursor.execute(update_user_gender_query)
#     conn.commit()
#
#     delete_usa_users_query = '''
#     truncate users;
#     '''
#     cursor.execute(delete_usa_users_query)
#     conn.commit()
# except Error as error:
#     print(error)
# finally:
#     cursor.close()
#     conn.close()
