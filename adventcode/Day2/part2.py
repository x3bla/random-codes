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
    ranges, letter = range_and_key.split(" ")  # y = ["10-18", "l"]
    range1, range2 = ranges.split("-")  # [10, 18]

    if pw[int(range1)-1] == letter or pw[int(range2)-1] == letter:  # if 10 <= amount of letter <= 18
        finalNum += 1

print(finalNum)
