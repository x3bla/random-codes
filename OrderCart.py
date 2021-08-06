import json


def logOrder():
    global OrderNumber
    OrderNumber += 1
    with open("log.json", 'r') as f:
        data = json.load(f)
        data["OrderNum"] = OrderNumber

    with open("log.json", 'w') as f:
        json.dump(data, f, indent=2)
