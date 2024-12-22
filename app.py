from flask import Flask, request, jsonify

from Utils.converter import from_json
from Utils.Validation import *
from playDocker import *
from Service.MySqlService import *
import atexit

app = Flask(__name__)

start_docker()
cl = MySqlService()
cl.createPlayeTBL()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/mysql', methods=['POST', 'DELETE', 'GET', 'PUT'])
def reguler():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        if not validate_email(json_data['email']):
            return jsonify({"error": "Invalid email address"}), 401

        player = from_json(json_data, ['email', 'position', 'speed', 'birth', 'type'])

        cl.insert_player(tuple=player.to_tuple())
        # Fetch all players after successful insertion
        all_players = cl.server.fetch("all")
        return jsonify({"succ": all_players}), 200


atexit.register(stop_docker)

if __name__ == '__main__':
    app.run()
