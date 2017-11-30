from __future__ import print_function

with open("mydata.txt", mode="w") as myFile:
    myFile.write("Some random test \nMore random text \nAdd some more")

with open("mydata.txt", mode="r") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:

            break

        print("Line ", lineNum)

        # Split ()

        wordList = line.split()

        # len()

        print("Number of Words :", len(wordList))

        # Loop count character in the word list

        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1

        # Divide Character count /len word list

        avgNumChars = charCount/len(wordList)

        print('Avg Word Length : {:.2f}'.format(avgNumChars))

        lineNum += 1
