import json

JSON_USER_PATH = "./json/user.json"


class MenuSauvegarde:

    def __init__(self):
        None


def checkSauvegarde():
    with open(JSON_USER_PATH) as jsonFile:
        data = json.load(jsonFile)
        if data["username"] != "":
            return True
        else:
            return False
