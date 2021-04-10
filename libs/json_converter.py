import json, datetime

def json_convert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def json_dump_function(o):
    return json.dumps(o, default=json_convert)