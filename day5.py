import re
import itertools


def readFile(filepath: str):
    file = open(filepath, 'r')
    return file.read()

#format the input to rules and records
def formatInput(input: str):
    rules = re.findall("[0-9][0-9]\|[0-9][0-9]", input)

    #make dit of rules
    ruleDict = {}
    for i in range(0, len(rules)):
        key = int(rules[i].split("|")[0])
        value = int(rules[i].split("|")[1])
        addKeyToDict(ruleDict, key, value)
    
    #scuff records bc its easier
    input = input.split('\n')
    records = []
    for i in range(1177,1382): #hee hee hee haw
        strInts = input[i].split(',')
        toAdd = []
        for j in range(0, len(strInts)):
            toAdd.append(int(strInts[j]))
        records.append(toAdd)
    
    return ruleDict, records

#checks if a inputted record is valid
def checkRecordValid(rules: dict[int, list[int]], record: list[int]) -> bool:
    addedNums = [] #list of nums already checked

    #n! time because BUCKETSSSSSSSSSSSSSSSSSSSSSSSSSSS
    for i in range(0, len(record)):
        numLookingAt = record[i]
        if not checkIfNumLookingAtPrememptivelyPrinted(rules, numLookingAt, addedNums):
            return False
        addedNums.append(numLookingAt)
    
    return True

def getmiddleValue(input: list[int]) -> int:
    index = (len(input) - 1)
    index = int(index / 2)
    return input[index]

#checks if a num has been printed already
def checkIfNumLookingAtPrememptivelyPrinted(rules: dict[int, list[int]], num: int, printedAlready: list[int]) -> bool:
    afters = rules[num]

    #if num has been printed already return false
    for x in afters:
        if x in printedAlready:
            return False
    
    return True

#fixes a broken record
def fixRecord(rules: dict[int, list[int]], record: list[int]):
    #plan is to 'bubble sort' record
    #if a index needs to come after a different index swap it and go again
    
    for i in range(0, len(record)):
        for j in range(0, len(record) - 1):
            if not checkRecordValid(rules, record[j::]):
                swap(record, j, j + 1)

    if not checkRecordValid(rules, record):
        return -1000000

    return getmiddleValue(record)


def swap(input, start, dest):
    temp = input[start]
    input[start] = input[dest]
    input[dest] = temp


  

#checks all records
def checkAllRecords(rules: dict[int, list[int]], records: list[list[int]]) -> int:
    total = 0

    for x in records:
        if not checkRecordValid(rules, x):
            total += fixRecord(rules, x)

    return total


##add a key to the dictionary
def addKeyToDict(input: dict[int, list[int]], key: int, value: int):
    if key in input.keys():
        input[key].append(value)
    else:
        input[key] = [value]

if __name__ == '__main__':
    input = readFile("input.txt")
    rules, records = formatInput(input)
    print(checkAllRecords(rules, records))
    