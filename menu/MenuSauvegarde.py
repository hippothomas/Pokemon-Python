import json

JSON_USER_PATH = "./json/user.json"


def checkSauvegarde():
    if getUsernameFromJson() != "":
        return True
    else:
        return False

def getUsernameFromJson():
    with open(JSON_USER_PATH) as jsonFile:
        data = json.load(jsonFile)
        username = data["username"]
        return username