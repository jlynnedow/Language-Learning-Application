import random

pronombres = ["yo", "tú", "él/ella/ud.", "nosotros", "vosotros", "ellos/ellas/uds."]
words = {}
conj = {}
mode = input("Hello! Would you like to study vocab or conjugations? ")
file = input("Please enter the input file: ")
exit = False
if mode == "vocab" :
    with open(file, 'r', encoding="utf8") as file:
        for line in file:
            line = line.strip()
            words[line[:line.index(":")]] = line[line.index(":") + 1:]
    print("You have entered quiz mode")
    while not exit:
        keys = list(words.keys())
        currentKey = keys[int(random.random() * len(words))]
        ans = input(currentKey + ": ")
        if ans == words[currentKey]:
            print("Correct!")
        else:
            while not (ans == words[currentKey]):
                print("Incorrect. The correct answer is " + words[currentKey])
                ans = input("Please enter the correct answer: ")
        if input("Press e to exit and c to continue: ") == "e":
            exit = True
else:
    with open(file, 'r', encoding="utf8") as file:
        for line in file:
            line = line.strip()
            conj[line[:line.index(":")]] = line[line.index(":") + 1:].split(":")
    print(conj)
    print("You have entered quiz mode")
    while not exit:
        keys = list(conj.keys())
        currentKey = keys[int(random.random() * len(conj))]
        i = int(random.random() * 6)
        ans = input(currentKey + " (" + pronombres[i] + "): ")
        if ans == conj[currentKey][i]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is " + conj[currentKey][i])
            ans = input("Please enter the correct answer: ")
        if input("Press e to exit and c to continue: ") == "e":
            exit = True






