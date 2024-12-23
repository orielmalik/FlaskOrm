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
            b = self.getplayersByOptions(1, tuple[0])
            if b != None:
                raise TypeError("Invalid email")

            conn = create_connection()
            cursor = conn.cursor()
            insert_query = readTextFile("insert.txt", "Queries").split("|")[0]
            cursor.execute(insert_query, tuple)
            conn.commit()

            return True

        except Exception as e:
            print(f"Error inserting player: {e}")
        return False

    def getplayersByOptions(self, opt, value):
        try:
            res = self.server.exec(readTextFile("select.txt", "Queries").split('|')[opt], value)
            return res
        except Exception as e:
            raise e

    def update_player(player):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            update_query = readTextFile("Update.txt", "Queries").split("|")[0]
            cursor.execute(update_query, (player.__position, player.__speed,
                                          player.__birth, player.___type, player.__email))
            conn.commit()

            cursor.close()
            conn.close()
        except pymysql.MySQLError as e:
            print(f"Error updating player: {e}")
