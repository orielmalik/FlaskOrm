import json
from flask import Flask, request, jsonify, Response
from Utils.const import *
from Utils.Validation import *
from playDocker import *
from Service.MySqlService import *
import atexit
from Service.AlchemyService import from_json, AlchemyService, to_dict

app = Flask(__name__)

start_docker()
alchemy = AlchemyService()
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
                return jsonify({"succ": cl.getplayersByOptions(1, str(json_data['email']))}), 200
            else:
                return jsonify({"error": "error in"}), 404

        except Exception as e:
            return jsonify({"error": str(e)}), 404

    elif request.method == 'DELETE':
        try:
            if request.args.get('id'):
                cl.delete_player(condition='email = %s', email=request.args.get('id'))
            else:
                cl.server.exec("TRUNCATE TABLE Players")
            return jsonify({"deleted": True}), 200
        except Exception as e:
            return jsonify({"deleted", True}), 400


@app.route('/alchemy', methods=['POST', 'DELETE', 'GET', 'PUT'])
def orm():
    if request.method == 'POST':
        try:
            target = request.get_json()  # מקבל את הנתונים מה-Request
            return jsonify({"ok":(alchemy.create_player(target))}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        # return Response(alchemy.getPlayers(), mimetype="text/event-stream")
    elif request.method == 'DELETE':
        try:
            if request.args.get('id'):
                alchemy.deletePlayer(request.args.get('id'))
                return jsonify({"OK": True}), 200
            else:
                alchemy.deletePlayers("TRUNCATE TABLE player")
            return jsonify({"success": True}), 200
        except TypeError:
            return jsonify({"success": True}), 400

    elif request.method == 'PUT':
        try:
            return jsonify({"success":to_dict(alchemy.updatePlayer(request.get_json()))}), 200
        except Exception as ex:
            return jsonify({"success": str(ex)}), 400


atexit.register(stop_docker, cl.server.conn, alchemy.getServer())

if __name__ == '__main__':
    app.run()
    cl.server.ensure_connection()
