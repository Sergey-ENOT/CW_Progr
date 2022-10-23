import mysql.connector
from config import host, user, password, db_name
from mysql.connector import Error


class CreatingDB:
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name
        self.connection_db = None
        self.mycursor = None

    def create_connection_host(self):
        try:
            self.connection_db = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
            )
            print("success")
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def create_connection_db(self):
        try:
            self.connection_db = mysql.connector.connect(
                host=self.host,
                port=3306,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )
            print("success")
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def create_database_student(self):
        self.mycursor = self.connection_db.cursor()
        self.mycursor.execute('''CREATE DATABASE IF NOT EXISTS student;''')
        self.connection_db.commit()
        self.mycursor.close()
        self.mycursor = None

    def create_tables(self):
        self.mycursor = self.connection_db.cursor()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS study_group(
                group_id VARCHAR(15) NOT NULL,
                direction_of_training VARCHAR(15),
                course INT NOT NULL,
                PRIMARY KEY(group_id)
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS student(
                gradebook VARCHAR(15) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                name VARCHAR(50) NOT NULL,
                patronymic VARCHAR(50),
                study_group VARCHAR(15) NOT NULL,
                date_of_birth DATE,
                town VARCHAR(30),
                street VARCHAR(40),
                house INT,
                PRIMARY KEY(gradebook),
                FOREIGN KEY(study_group) REFERENCES study_group(group_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS subject(
                id INT NOT NULL,
                name VARCHAR(50),
                PRIMARY KEY(id)
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS debt(
                id INT NOT NULL AUTO_INCREMENT,
                student_id VARCHAR(15) NOT NULL,
                subject_id INT NOT NULL,
                semester INT NOT NULL,
                date DATE,
                PRIMARY KEY(id), 
                FOREIGN KEY(student_id) REFERENCES student(gradebook)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY(subject_id) REFERENCES subject(id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS scholarship(
                id INT NOT NULL,
                name VARCHAR(50) NOT NULL,
                amount INT,
                PRIMARY KEY(id)
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.execute('''
            CREATE TABLE IF NOT EXISTS student_scholarship(
                id INT NOT NULL AUTO_INCREMENT,
                student_id VARCHAR(15) NOT NULL,
                scholarship_id INT NOT NULL,
                PRIMARY KEY(id),
                FOREIGN KEY(student_id) REFERENCES student(gradebook)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY(scholarship_id) REFERENCES scholarship(id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            ) ENGINE=INNODB;''')
        self.connection_db.commit()

        self.mycursor.close()
        self.mycursor = None

    def add_study_groups(self):
        try:
            self.mycursor = self.connection_db.cursor()

            self.mycursor.execute(f'''INSERT INTO study_group (group_id, direction_of_training, course) VALUES 
                                ("bi-20i1", "Специалитет", "3"),
                                ("pib-20i1", "Бакалавриат", "2");''')
            self.connection_db.commit()
            self.mycursor.close()
        except Exception as error:
            print("Error: ", error)
        finally:
            self.mycursor.close()
            self.connection_db.close()

    def add_students(self):
        try:
            self.mycursor = self.connection_db.cursor()

            self.mycursor.execute(f'''INSERT INTO student (gradebook, surname, name, patronymic, study_group,
                                    date_of_birth, town, street, house) VALUES 
                        ("bi-20i1-16", "Ivanov", "Oleg", "Ivanovich", "bi-20i1", "2001-04-18", "Omsk", "Mira", "5"),
                        ("pib-20i1-19", "Рассказов", "Дмитрий", "Олегович", "pib-20i1", "1999-04-18", "Moscow", "Mira", "6");''')
            self.connection_db.commit()
            self.mycursor.close()
        except Exception as error:
            print("Error: ", error)
        finally:
            self.mycursor.close()
            self.connection_db.close()

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except Exception as ex:
            print(ex)


test = CreatingDB(host, user, password, db_name)

test.create_connection_host()
test.create_database_student()
test.close_connection()

test.create_connection_db()
test.create_tables()
test.close_connection()


test.create_connection_db()
test.add_study_groups()
test.close_connection()

test.create_connection_db()
test.add_students()
test.close_connection()
