from motor.motor_asyncio import AsyncIOMotorClient
from flask import Flask
from Utils.converter import buildMongoDBQuery
from Utils.log.logg import printer


class MongoDBError(Exception):
    """Custom exception for MongoDB-related errors."""
    pass


def raiseError(data, collection_name):
    if not isinstance(data, dict) or not isinstance(collection_name, str):
        printer("Data must be a dictionary.", "ERROR")
        raise MongoDBError("Invalid data or collection name.")

class AsyncMongoDB:
    def __init__(self):
        self.client = None
        self.server = None

    def initlz(self, app: Flask):
        app.config["MONGO_URI"] = "mongodb://root:secret@mongodb:27017/dbplayer"
        self.client = AsyncIOMotorClient(app.config["MONGO_URI"])
        self.server = self.client.dbplayer

    async def close_connection(self):
        if self.client:
            await self.client.close()  # Use async close method
            self.client = None

    async def insert_one(self, collection_name, data):
        raiseError(data, collection_name)
        collection = self.server[collection_name]
        result = await collection.insert_one(data)
        return result.inserted_id

    async def update_one(self, collection_name, data, opt, fields, values):
        raiseError(data, collection_name)
        if not isinstance(opt, int) or not isinstance(fields, dict):
            raise MongoDBError("Invalid options or fields.")
        collection = self.server[collection_name]
        query = buildMongoDBQuery((opt,), fields, values, "update")
        result = await collection.update_one({"_id": data["_id"]}, query)
        return result.modified_count

    async def find(self, collection_name, opts, fields, values, all=False):
        collection = self.server[collection_name]
        query = buildMongoDBQuery(opts, fields, values, "find")
        if not all:
            return await collection.find_one(query)
        else:
            cursor = collection.find(query)
            return [doc async for doc in cursor]  # Efficiently get all documents

