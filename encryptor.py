import json

# texts
Welcome = "ナイスミールレストランへようこそ"


def log():
    global Welcome
    with open("language.json", 'r') as f:
        data = json.load(f)
        data["Japanese"]["Welcome"] = Welcome

    with open("language.json", 'w') as f:
        json.dump(data, f, indent=4)

def something():
    with open("language.json", 'r') as f:
        data = json.load(f)
        return data["Japanese"]["Welcome"]


x = input("are you sure? ")
if x == "y":
    print(Welcome)
    log()

if x == "x":
    print(something())  # prints out what's in the slot
