import subprocess
import time


def start_docker():
    print("Starting Docker containers...")
    subprocess.run(["docker-compose", "up", "--build", "-d"])


def stop_docker():
    print("Stopping Docker containers...")
    subprocess.run(["docker-compose", "down"])


def run_flask():
    print("Starting Flask app...")
    subprocess.run(["python", "app.py"])



