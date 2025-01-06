import os

import pytest
import requests
from pymysql import Date
from datetime import datetime

from Entity.Player import Player
from Utils.FileUtils import insertJson
from Utils.log.logg import printer


# GIVEN: SERVER RUN
def create_insert_json(file_):
    return lambda: insertJson(file_)


class Testmysql:
    json_cases = [create_insert_json(file_) for file_ in os.listdir(os.path.join(os.getcwd(), "jfiles")) if
                  not file_.startswith('PL_R')]

    res = requests.delete("http://localhost:5000/mysql")

    # שינוי תיקיית העבודה לתיקיית jfiles
    os.chdir(r"C:\Users\User\PycharmProjects\bicycle\OrmProject1\TEST\jfiles")

    json_data = insertJson("PL_R.json")
    json_cases.append(insertJson("PL_R.json"))

    json_cases.extend([create_insert_json(file_) for file_ in os.listdir(os.getcwd()) if not file_.startswith('PL_R')])
    printer(len(json_cases), "WARNING")

    os.chdir(os.getcwd())
    printer(len(json_cases),"WARNING")
    os.chdir(os.getcwd())

    @pytest.mark.parametrize("data", json_cases)
    def test_post(self, data):
        r = requests.post("http://localhost:5000/mysql", json=data)
        assert r.status_code == 200
