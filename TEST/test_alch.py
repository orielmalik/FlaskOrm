import os

import pytest
import requests
from datetime import date

from Utils.FileUtils import insertJson
from Utils.log.logg import printer


def create_insert_json(file_):
    return lambda: insertJson(file_)
class TestAlchemy:
    counterSameObject = {"value", 0}
    res = requests.delete("http://localhost:5000/alchemy")

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
    printer(len(json_cases), "WARNING")
    os.chdir(os.getcwd())

    @pytest.mark.parametrize(
        "player_data", json_cases
    )
    def test_post(self, player_data):
        res = requests.post("http://localhost:5000/alchemy", json=player_data)
        assert res.status_code == 200
        res = requests.post("http://localhost:5000/alchemy", json=player_data)
        assert res.status_code == 400

    @pytest.mark.parametrize(
        "_id",["","player@example.com","plexapmple.com"]
    )
    def test_delete(self, _id):
        res = requests.delete("http://localhost:5000/alchemy?id=" + str(_id))
        assert res.status_code == 200
