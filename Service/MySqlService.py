from Data.mySql import *
from Entity import Player
from Utils.FileUtils import *
from Utils.Validation import *


class MySqlService():
    def __init__(self):

        self.server = mysqldb()
        self.server.ensure_connection()

    def createPlayeTBL(self):
        self.server.ensure_connection()
        try:
            create_table_query = readTextFile('Create.txt', "Queries").split("|")[0]
            print(create_table_query)
            self.server.exec(create_table_query)
            self.server.commit()

        except Exception as e:
            print(f"Error creating Players table: {e}")
            raise

    def insert_player(self, tuple):
        if not validate_email(tuple[0]):
            raise TypeError("Invalid email")
        try:
            print("Checking if player exists...")
            b = self.getplayersByOptions(1, tuple[0])
            if b is None:
                raise TypeError("Invalid email")

            conn = create_connection()  # ensure connection
            cursor = conn.cursor()

            insert_query = readTextFile("insert.txt", "Queries").split("|")[0]

            cursor.execute(insert_query, tuple)
            conn.commit()
            return cursor.fetchone()

        except pymysql.MySQLError as e:
            print(f"Error inserting player: {e}")
            import traceback
            traceback.print_exc()

        return False

    def getplayersByOptions(self, opt, value):
        try:
            res = self.server.exec(readTextFile("select.txt", "Queries").split('\n')[opt], value)
            return res
        except Exception as e:
            raise e

    def update_player(self, player,):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            target = self.getplayersByOptions(1, player.__email)
            if target is None or not isinstance(target,tuple) or not len(target) == 1:
                raise ValueError("Invalid email")
            update_query = readTextFile("Update.txt", "Queries").split("|")[0]
            cursor.execute(update_query, (target["position"], target["speed"],
                                          target["birth"], target["type"], target["email"]))
            conn.commit()

            cursor.close()
            conn.close()
        except pymysql.MySQLError as e:
            print(f"Error updating player: {e}")

    def delete_player(self, condition='', email=''):
        try:
            self.server.exec(readTextFile('Delete.txt', 'Queries').split('\n')[0] + "  " + condition, params=email)
        except Exception as e:
            raise e
