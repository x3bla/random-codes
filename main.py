import json
# import OrderCart as o


# variables
Vouchers = []
OrderNumber = 0

# texts
Welcome = "welcome didn't work"
Menu = "Menu didn't work"
Rice = "Rice didn't work"
Noodles = "Noodles didn't work"
Bento = "Bento didn't work"

def selectEnglish():
    global Welcome, Menu, Rice, Noodles, Bento
    with open("language.json", "r") as f:
        lang = json.load(f)
        Welcome = lang["English"]["Welcome"]
        Menu = lang["English"]["Welcome"]
        Rice = lang["English"]["Food"]["Rice"]
        Noodles = lang["English"]["Food"]["Noodles"]
        Bento = lang["English"]["Food"]["Bento"]


def selectJapanese():
    global Welcome
    global Menu
    with open("language.json", "r") as f:
        lang = json.load(f)
        Welcome = lang["Japanese"]["Welcome"]


def unloadLog():
    global Vouchers
    global OrderNumber
    with open("log.json", "r") as f:
        data = json.load(f)
        Vouchers = data["VoucherCode"]
        OrderNumber = data["OrderNum"]


def logOrder():
    global OrderNumber
    OrderNumber += 1
    with open("log.json", 'r') as f:
        data = json.load(f)
        data["OrderNum"] = OrderNumber

    with open("log.json", 'w') as f:
        json.dump(data, f, indent=2)


def selectLanguage():
    while True:
        num = input("Select your language\n1. English\n2. Japanese\n>>> (1/2): ")
        if num == "1":
            selectEnglish()
            break
        elif num == "2":
            selectJapanese()
            break
        else:
            print("That is not a valid option, please try again")

def welcome():
    welcomeLoop = True
    while welcomeLoop:
        global Run
        num = input(Welcome)
        if num == "1":
            selectEnglish()
            break
        elif num == "2":
            selectJapanese()
            break
        elif num == "3":
            print("Exiting...")
            Run = False
            break
        else:
            print("That is not a valid option, please try again")

def menu():
    menuLoop = True
    while menuLoop:
        menuLoop = False
        num = input(Menu)
        if num == '1':
            rice()
        elif num == '2':
            noodles()
        elif num == '3':
            bento()
        else:
            print("That is not a valid option, please try again")
            menuLoop = True

def rice():
    riceLoop = True
    while riceLoop:
        riceLoop = False
        num = input(Rice)
        if num == '1':
            tempLoop = True
            while tempLoop:
                tempLoop = False


def noodles():
    noodlesLoop = True
    while noodlesLoop:
        noodlesLoop = False
        num = input(Noodles)

def bento():
    bentoLoop = True
    while bentoLoop:
        bentoLoop = False
        num = input(Bento)


unloadLog()
Run = True
while Run:
    selectLanguage()
    welcome()

