req_fields=['email', 'position', 'speed', 'birth', 'type']
column_order = [3, 0, 2, 1]
key = bytes("46tpQ1JEdwR6owoQ0Sbp065ypr2BM43OobXf4SVsdlk=",encoding="utf-8")

mongodb_commands = {
    "update": ("$set", "$unset", "$inc", "$mul", "$rename", "$min", "$max", "$currentDate"),
    "array": ("$push", "$pop", "$pull", "$pullAll", "$addToSet", "$each", "$slice", "$sort"),
    "aggregation": ("$match", "$group", "$sort", "$project", "$limit", "$skip", "$unwind", "$lookup"),
    "find": ("$eq", "$ne", "$gt", "$gte", "$lt", "$lte", "$in", "$nin"),
    "logical": ("$and", "$or", "$not", "$nor"),
    "element": ("$exists", "$type"),
    "evaluation": ("$regex", "$text", "$where"),
    "bitwise": ("$bitsAllSet", "$bitsAnySet", "$bitsAllClear", "$bitsAnyClear"),
    "geospatial": ("$geoWithin", "$geoIntersects", "$near", "$nearSphere")
}