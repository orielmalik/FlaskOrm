import os

import pytest
import requests
from pymysql import Date
from datetime import datetime

from Entity.Player import Player
from Utils.FileUtils import insertJson


# GIVEN: SERVER RUN
class Testmysql:
    json_cases = [lambda file_: insertJson(file_) for file_ in os.listdir(os.path.join(os.getcwd(), "jfiles"))]
    res = requests.delete("http://localhost:5000/mysql")

    @pytest.mark.parametrize("data", json_cases)
    def test_post(self, data):
        r = requests.post("http://localhost:5000/mysql", json=data)
        assert r.status_code == 200
