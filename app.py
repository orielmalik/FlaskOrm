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
        try:
            b = cl.insert_player(tuple=player.to_tuple())
            if b:
                return jsonify({"succ":cl.getplayersByOptions(1,str(json_data['email'])) }), 200
            else:
                return jsonify({"error": "error in"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}),404



atexit.register(stop_docker)

if __name__ == '__main__':
    app.run()
    cl.server.ensure_connection()
