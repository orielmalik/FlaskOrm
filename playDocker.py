import subprocess
import time

import pymysql
from sqlalchemy.orm import Session

from Data import mySql


def start_docker():
    print("Starting Docker containers...")
    subprocess.run(["docker-compose", "up", "--build", "-d"])



def stop_docker(conn=None, alch=None):
    print("Stopping Docker containers...")
    if isinstance(conn, pymysql.connect) and is_connection_active(conn) :
        conn.close()
    if isinstance(alch, Session):
        alch.close()
        print("Stopping")
    subprocess.run(["docker-compose", "down"])


def is_connection_active(conn):
  """
  Checks if the provided pymysql connection object is active.

  Args:
    conn: The pymysql connection object.

  Returns:
    True if the connection is active, False otherwise.
  """
  try:
    # Attempt a simple query to check connectivity
    with conn.cursor() as cursor:
      cursor.execute("SELECT 1")
      cursor.fetchone()
      return True
  except pymysql.Error as e:
    print(f"Connection error: {e}")
    return False
def run_flask():
    print("Starting Flask app...")
    subprocess.run(["python", "app.py"])
