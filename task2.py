vowels = ["а","о","у","е","и","і"]

N = int(input("count of strings: "))
stringList = []
for i in range(N):
    stringList.append(input("Input string " + str(i + 1) + " : "))

def countVowels(string):
    count = 0
    for c in string:
        if c in vowels:
            count += 1
    return count

totalVowels = 0
for string in stringList:
    totalVowels += countVowels(string)

print("Sum of vowels in all strings is: ", totalVowels)
