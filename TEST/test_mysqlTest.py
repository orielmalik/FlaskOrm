import pytest
import requests
from pymysql import Date
from datetime import datetime

from Entity.Player import Player

# GIVEN: SERVER RUN
class TestMysqlTest:
    @pytest.fixture(autouse=True)
    def setup_requester(self):
        """Fixture to ensure requester initialization for the test class."""
        self.requester = requests.get('http://localhost:5000/mysql')

    def test_post(self):
        try:
            # Convert Player object to JSON
            player_data = Player("s@gmail.com", "CENTER", speed=7.7, birth=datetime.now(), type='basketball')

            # Send POST request
            self.requester = requests.post('http://localhost:5000/mysql', json=player_data.to_json())

            # Assert response status code
            assert self.requester.status_code == 200

        except requests.exceptions.RequestException as e:
            pytest.fail(f"Request failed: {e}")

