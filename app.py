import asyncio
import uuid

from flask import Flask, request, jsonify

from Service.mongodb import myMongoDB
from Utils.const import *
from playDocker import *
from Service.MySqlService import *
import atexit
from Service.AlchemyService import from_json, AlchemyService, to_dict

app = Flask(__name__)

start_docker()
alchemy = AlchemyService()
cl = MySqlService()
cl.createPlayeTBL()
mongo = myMongoDB()


@app.route('/mongo', methods=['POST', 'PUT', 'GET', 'DELETE'])
def nosqlmongo():
    if not checkRequest(request.get_json()):
        return jsonify({'error': 'unauthorized'}), 401

    data = request.get_json()

    if request.method == 'POST':
        data["_id"] = str(uuid.uuid4().hex)
        res = mongo.insert_one("gaya", data)
        inserted_doc = mongo.find("gaya", opt=0, fields=("_id",), values=(data["_id"],))
        return jsonify({"ok": True, "data": inserted_doc})

    elif request.method == 'PUT':
        if "_id" not in data:
            return jsonify({'error': '_id is required for update'}), 400

        res = mongo.update_one(
            "gaya", opt=0, fields=tuple(data.keys()), values=tuple(data.values())
        )
        updated_doc = mongo.find("gaya", opt=0, fields=("_id",), values=(data["_id"],))
        return jsonify({"ok": True, "data": updated_doc})

    elif request.method == 'GET':
        all_docs = mongo.find("gaya", opt=0, fields=(), values=(), all=True)
        return jsonify({"ok": True, "data": all_docs})




@app.route('/mysql', methods=['POST', 'DELETE', 'GET', 'PUT'])
def reguler():
    if request.method == 'POST':
        json_data = request.get_json()
        printer(json_data, "INFO")
        if not validate_email(json_data['email']):
            return jsonify({"error": "Invalid email address"}), 401
        player = from_json(json_data, req_fields)
        try:
            k = cl.insert_player(player_data=player.to_tuple())
            return jsonify({"ok:": k}), 200
        except Exception as e:
            return jsonify({"error": "err"}), 404

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
            return jsonify({"ok": (alchemy.create_player(target))}), 200
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
            return jsonify({"success": to_dict(alchemy.updatePlayer(request.get_json()))}), 200
        except Exception as ex:
            return jsonify({"success": str(ex)}), 400


def checkRequest(data):
    """Validate incoming request and data."""
    if request.method in ['POST', 'PUT']:
        try:
            player = from_json(data, req_fields)
            res = mongo.find("gaya", opt=0, fields=("email",), values=(data['email'],))
            return (request.method == 'POST' and res is None) or (request.method == 'PUT' and res is not None)
        except Exception as e:
            printer(str(e), "ERROR")
            return jsonify({'error': str(e)}), 400
    return True


atexit.register(stop_docker, cl.server.conn, alchemy.getServer())

if __name__ == '__main__':
    app.run(debug=True)
    printer(mongo.server.get_collection('gaya'))
    asyncio.run(mongo.test_connection())
