import random

def SerialNumberGroup():
    group = ""
    for i in range(4):
        group += chr(random.randint(ord("A"), ord("Z")))
    return group

def generateSerialNumber():
    return SerialNumberGroup() + "-" + SerialNumberGroup() + "-" + SerialNumberGroup()

def displayNSerialNumbers(n):
    for i in range(n):
        print(generateSerialNumber())

def changeFirstLetter(num, changeTo):
    newNum = "Q" + num[1:len(num)]
    return newNum

def displayNSerialNumbersWLetter(n, letter):
    for i in range(n):
        print(changeFirstLetter(generateSerialNumber(), letter))

print("\nSerial nunmbers")
displayNSerialNumbers(9)

print("\nSerial nunmbers that begin with Q")
displayNSerialNumbersWLetter(12, "Q")        
