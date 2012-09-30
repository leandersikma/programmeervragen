dictionary = open("../../dictionary.txt", "r")

tupleWithWords = tuple(dictionary)

alphabeticalWords = 0
for line in tupleWithWords:
    wordCount = 0
    while True:
        if wordCount < len(line[:-2]):
            if ord(line[wordCount]) > ord(line[wordCount + 1]):
                break
            wordCount = wordCount + 1
        else:
            alphabeticalWords = alphabeticalWords + 1
            
            break
            
print(alphabeticalWords)   

