from Data.mySql import *
from Entity import Player
from Utils.FileUtils import *

class MySqlService():
    def __init__(self):
        self.server = mysqldb()
        self.server.ensure_connection()


    def createPlayeTBL(self):
        self.server.ensure_connection()
        try:
            create_table_query = readTextFile('Create.txt',"Queries").split("|")[0]
            print(create_table_query)
            self.server.exec(create_table_query)
            self.server.commit()

        except Exception as e:
            print(f"Error creating Players table: {e}")
            raise

    def insert_player(self,tuple):
        try:
            conn = create_connection()
            cursor = conn.cursor()

            insert_query = readTextFile("insert.txt","Queries").split("|")[0]
            cursor.execute(insert_query, tuple)
            conn.commit()

            cursor.close()
            conn.close()
        except pymysql.MySQLError as e:
            print(f"Error inserting player: {e}")


        def update_player(player):
            try:
                conn = create_connection()
                cursor = conn.cursor()

                update_query = """
                UPDATE Players
                SET position = %s, speed = %s, birth = %s, type = %s
                WHERE email = %s
                """
                cursor.execute(update_query, (player._Player__position, player._Player__speed,
                                              player._Player__birth, player._Player__type, player._Player__email))
                conn.commit()

                cursor.close()
                conn.close()
            except pymysql.MySQLError as e:
                print(f"Error updating player: {e}")
