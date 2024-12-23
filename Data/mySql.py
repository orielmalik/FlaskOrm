import pymysql


def create_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="navigator",
            port=3307,
            db='player_db',
            ssl_disabled=True,
            connect_timeout=78787
        )
        return conn
    except pymysql.err.OperationalError as e:
        print(f"Error connecting to database: {e}")
        raise

class mysqldb:

    def __init__(self):
        self.conn = create_connection()
        self.cursor = self.conn.cursor()

    def ensure_connection(self):
        try:
            self.conn.ping(reconnect=True)  # בודק אם החיבור פעיל ואם לא, מחבר מחדש
        except pymysql.MySQLError:
            print("Lost connection, reconnecting...")
            self.conn = create_connection()
            self.cursor = self.conn.cursor()

    def exec(self, query, params=None):
        self.ensure_connection()
        self.cursor.execute(query, params)

    def commit(self):
        self.ensure_connection()
        self.conn.commit()

    def fetch(self, selector, size=0):
        self.ensure_connection()
        if selector.lower() == 'all':
            return self.cursor.fetchall()
        elif selector.lower() == 'one':
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchmany(size)

    def close(self):
        self.cursor.close()
        self.conn.close()