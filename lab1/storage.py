from argparse import ArgumentParser
import json


def saveToFile(key, value):
    with open("tempfile", 'r') as f:
        # print("file opened")
        jsonStr = f.readlines()
    
    f.close()
    
    if (len(jsonStr) == 0):
        return
    # print(jsonStr)
    jsonStr = ' '.join(jsonStr)
    # print(jsonStr)
    print(f"old json {jsonStr}")
    jsonObject = json.loads(jsonStr)
    jsonObject[key] = value
    # print(jsonObject)
    jsonStr = json.dumps(jsonObject)
 
    f = open("tempfile", "w")
    f.write(jsonStr)
    print(f"saved: key = {key}, value = {value}")
    print(f"new json {jsonStr}")


def readFromFile(key):
    with open("tempfile", 'r') as f:
        # print("file opened")
        jsonStr = f.readlines()

    f.close()

    if (len(jsonStr) == 0):
        return
    # print(jsonStr)
    jsonStr = ' '.join(jsonStr)
    jsonObject = json.loads(jsonStr)
    print(f"value {jsonObject[key]}")





parser = ArgumentParser()
parser.add_argument("-k", "--key", type=str, dest="key", help="key for access in storage")
parser.add_argument("-v", "--value", type=str, dest="value", help="value found by key in storage")
args = parser.parse_args()

key: str = args.key
value: str = args.value
if (key is not None):
    if (value is not None):
        saveToFile(args.key, args.value)
if (key is not None):
    if (value is None):
        readFromFile(args.key)