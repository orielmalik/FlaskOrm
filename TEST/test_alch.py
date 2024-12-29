import os

import pytest
import requests
from datetime import date

from Utils.FileUtils import insertJson


class TestAlchemy:
    counterSameObject = {"value", 0}
    res = requests.delete("http://localhost:5000/alchemy")

    json_cases = [lambda file_: insertJson(file_) for file_ in os.listdir(os.path.join(os.getcwd(), "jfiles"))]

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
