from flask_pymongo import PyMongo


class MongoDB:
    def __init__(self):
        self.server = None

    def initlz(self, app):
        app.config["MONGO_URI"] = "mongodb://root:secret@mongodb:27017/dbplayer"
        self.server = PyMongo(app)

    def db(self):
        if self.server is not None and isinstance(self.server, PyMongo):
            return self.server.db
        else:
            raise Exception("exec run")

    def insertOne(self,data):
        _db = self.db()
        if not isinstance(data, dict):
            raise Exception("er")
        return self.server.db.insert_one(data)




