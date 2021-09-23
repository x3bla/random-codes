# by x3bla
# Project Ozone 2 latest update

import math


def ControlRods(x):
    ans = 2.5 - (2 * x) + (0.5 * math.pow(x, 2))
    return int(ans)


def Casing(x):
    X = x * x * x
    Y = (x - 2) * (x - 2) * (x - 2)
    return X - Y


def ConvertToStack(x):
    stack = x // 64
    remainder = x % 64
    return stack, remainder


# declaring materials
reactorCasing = 0
graphite = 0
yellorium = 0
redstone = 0
piston = 0
chest = 0
diamond = 0
steel = 0

# declaring upgrade materials
newReactorCasing = 0
newGraphite = 0
newYellorium = 0
newRedstone = 0
newPiston = 0
newChest = 0
newDiamond = 0
newSteel = 0

# note
print("Note that i'm using a checkered pattern for the rods so the reactor size only works with odd numbers\n\n")

# upgrading current or making new reactor
upgradeCheck = False
if input("input 1 if you're making a new reactor, input 2 if you are upgrading your reactor to a larger size\n") == '1':
    upgradeCheck = False
else:
    upgradeCheck = True

# size of the reactor
if upgradeCheck:
    size = int(input("How big is your current reactor size? (input '5' for 5x5x5, etc)\n"))
else:
    size = int(input("How big do you want the reactor to be? (input '5' for 5x5x5, etc, select an odd number)\n"))

# need main blocks or no
if not upgradeCheck:
    mainBlockCheck = input("Do you already have the essential components? Y/N (Controller, power tap, 2 access port)\n")
    if mainBlockCheck.lower() == 'n':
        # controller block
        yellorium += 2
        diamond += 1
        redstone += 1
        reactorCasing += 4

        # power tap
        redstone += 4
        reactorCasing += 4

        # access port x2
        reactorCasing += 8
        chest += 2
        piston += 2

# control rods needed and materials
for x in range(ControlRods(size)):
    reactorCasing += 4
    redstone += 1
    yellorium += 1
    graphite += 3

# because 4 blocks are taken by the main blocks
reactorCasing -= 4

# casings needed and materials
totalCasing = Casing(size) + reactorCasing
for x in range(totalCasing):
    yellorium += 1
    steel += 4
    graphite += 4

# fuel rods needed and materials
fuelRod = ControlRods(size) * (size - 2)
for x in range(fuelRod):
    steel += 6
    graphite += 2
    yellorium += 1

# Reactor upgrade calculation (basically a copy paste, how do i make this more efficient)

# new size of the reactor
if upgradeCheck:
    newSize = int(
        input("How big do you want the new reactor to be? (input '5' for 5x5x5, etc. select an odd number)\n"))

    # control rods and materials needed for upgrade
    for x in range(ControlRods(newSize)):
        newReactorCasing += 4
        newRedstone += 1
        newYellorium += 1
        newGraphite += 3

    # because 4 blocks are taken by the main blocks
    newReactorCasing -= 4

    # casings needed and materials
    newTotalCasing = Casing(newSize) + newReactorCasing
    for x in range(newTotalCasing):
        newYellorium += 1
        newSteel += 4
        newGraphite += 4

    # fuel rods needed and materials
    newFuelRod = ControlRods(newSize) * (newSize - 2)
    for x in range(newFuelRod):
        newSteel += 6
        newGraphite += 2
        newYellorium += 1

# for the upgrade
if upgradeCheck:
    graphite = newGraphite - graphite
    yellorium = newYellorium - yellorium
    redstone = newRedstone - redstone
    piston = newPiston - piston
    steel = newSteel - steel
    totalCasing = newTotalCasing - totalCasing

# displaying the info

print("\nGraphite:", graphite, ConvertToStack(graphite))
print("Yellorium:", yellorium, ConvertToStack(yellorium))
print("Redstone:", redstone, ConvertToStack(redstone))
print("Piston:", piston, ConvertToStack(piston))
print("Chest:", chest)
print("Diamond:", diamond)
print("Steel:", steel, ConvertToStack(steel))
print("\nTotal Reactor Casing for reference:", totalCasing, ConvertToStack(totalCasing))
