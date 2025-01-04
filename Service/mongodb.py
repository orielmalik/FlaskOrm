from pymongo import MongoClient
from Utils.converter import buildMongoDBQuery
from Utils.log.logg import printer


class MongoDBError(Exception):
    """Custom exception for MongoDB-related errors."""
    pass


def raiseError(data, collection_name):
    if not isinstance(data, dict) or not isinstance(collection_name, str):
        printer("Data must be a dictionary and collection name must be a string.", "ERROR")
        raise MongoDBError("Invalid data or collection name.")


class myMongoDB:
    def __init__(self):
        self.client = MongoClient("mongodb://root:secret@mongodb:27017")
        self.server = self.client['dbplayer']

    def test_connection(self):
        """Test connection to MongoDB."""
        try:
            self.client.admin.command('ping')
            printer("MongoDB connection established successfully.", "INFO")
        except Exception as e:
            printer(f"Failed to connect to MongoDB: {e}", "ERROR")
            raise MongoDBError("Failed to connect to MongoDB.")

    def close_connection(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()  # Correct: MongoClient uses sync close method
            self.client = None
            printer("MongoDB connection closed.", "INFO")

    def insert_one(self, collection_name, data):
        """Insert one document into a collection."""
        raiseError(data, collection_name)
        collection = self.server[collection_name]
        result = collection.insert_one(data)
        printer(result.inserted_id, "INFO")
        return result.inserted_id

    def update_one(self, collection_name, data, opt, fields, values):
        """Update a single document in a collection."""
        raiseError(data, collection_name)
        if not isinstance(opt, int) or not isinstance(fields, dict):
            raise MongoDBError("Invalid options or fields.")
        collection = self.server[collection_name]
        query = buildMongoDBQuery((opt,), fields, values, "update")
        result = collection.update_one({"_id": data["_id"]}, query)
        return result.modified_count

    def find(self, collection_name, opt, fields, values, all=False):
        """Find documents in a collection."""
        collection = self.server[collection_name]
        query = buildMongoDBQuery((opt,), fields, values, "find")
        if not all:
            return collection.find_one(query)
        return list(collection.find(query))  # Get all documents synchronously