# variables
checkNumbers = []
tempNum = 0
finalNum = 0

# unloading the txt file into a list
with open("inputDay2.txt", 'r') as f:
    for line in f:
        checkNumbers.append(line)

for number in checkNumbers:
    number = number.strip()  # removing empty line  10-18 l: gllpmlgtrmnllhllrlll
    range_and_key, pw = number.split(": ")  # splitString = ["10-18 l", "gllpmlgtrmnllhllrlll"]
    ranges, key = range_and_key.split(" ")  # y = ["10-18", "l"]
    range1, range2 = ranges.split("-")  # [10, 18]

    if int(range1) <= pw.count(key) <= int(range2):  # if 10 <= amount of letter <= 18
        finalNum += 1

print(finalNum)
