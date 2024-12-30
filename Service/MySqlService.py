from Data.mySql import *
from Utils.Validation import *
from Utils.FileUtils import *
from Utils.log.logg import printer


class MySqlService():
    def __init__(self):

        self.server = mysqldb()
        self.server.ensure_connection()

    def createPlayeTBL(self):
        self.server.ensure_connection()
        try:
            create_table_query = (readTextFile('Create.txt', "Queries")).split("|")[0]
            print(create_table_query)
            self.server.exec(create_table_query)
            self.server.commit()

        except Exception as e:
            print(f"Error creating Players table: {e}")
            raise

    def insert_player(self, player_data):
        self.server.ensure_connection()
        """
        data=( self.__email, self.__position, self.__speed, self.__birth, self.__type)
        """
        if not validate_email(player_data[0]) or not isinstance(player_data,tuple):
            raise TypeError("Invalid email")

        self.raiseGet(1, player_data[0])
        try:
            insert_query = readTextFile("insert.txt", "Queries").split("|")[0].strip()
            printer(insert_query)

            self.server.exec(insert_query, player_data)
            # Commit the transaction
            self.server.conn.commit()

            # Fetch the inserted player for confirmation
            select_query = readTextFile("select.txt").split('\n')[1].strip()
            self.server.exec(select_query, player_data[0])
            return self.server.cursor.fetchone()
        except Exception as e:
            printer(f"Error occurred: {e}")
            raise

    def getplayersByOptions(self, opt, value):
        try:
            res = self.server.exec((readTextFile("select.txt", "Queries")).split('\n')[opt], value)
            return res
        except Exception as e:
            raise e

    def update_player(self, player, ):
        try:
            conn = self.server.conn()
            cursor = conn.cursor()
            target = self.getplayersByOptions(1, player.__email)
            if target is None or not isinstance(target, tuple) or not len(target) == 1:
                raise ValueError("Invalid email")
            update_query = (readTextFile("Update.txt", "Queries")).split("|")[0]
            cursor.execute(update_query, (target["position"], target["speed"],
                                          target["birth"], target["type"], target["email"]))
            conn.commit()
            printer(update_query)
            cursor.close()
            conn.close()
            printer("closed", "INFO")

        except pymysql.MySQLError as e:
            printer(f"Error updating player: {e}", "ERROR")

    def delete_player(self, condition='', email=''):
        try:
            self.server.exec((readTextFile('Delete.txt', 'Queries')).split('\n')[0] + "  " + condition, params=email)
        except pymysql.MySQLError as e:
            printer(f"Error deleting player: {e}", "ERROR")
            raise TypeError("err")

    def raiseGet(self, opt, val):
        try:
            printer("Checking if player exists...")
            existing_player = self.getplayersByOptions(opt, val)
            if existing_player is not None:
                print("ok")
                raise TypeError("err")
        except pymysql.MySQLError as es:
            printer(f"Error create player: {es}", "ERROR")
            raise TypeError("err")
