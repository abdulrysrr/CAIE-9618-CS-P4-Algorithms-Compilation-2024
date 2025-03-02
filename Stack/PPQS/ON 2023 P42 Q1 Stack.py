def PushData(Letter):
    global VowelTop
    global ConsonantTop
    if Letter in ['a','e','i','o','u']:
        if VowelTop == 100:
            print("Vowel stack full")
        else:
            StackVowel[VowelTop] = Letter
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print("Consonant stack full")
        else:
            StackConsonant[ConsonantTop] = Letter
            ConsonantTop += 1

def PopVowel():
    global VowelTop
    global ConsonantTop
    if VowelTop - 1:
        VowelTop -= 1
        DataToReturn = StackVowel[VowelTop]
        return DataToReturn
    else:
        return "No data"

def PopConsonant():
    global VowelTop
    global ConsonantTop
    if ConsonantTop - 1:
        ConsonantTop -= 1
        DataToReturn = StackConsonant[ConsonantTop]
        return DataToReturn
    else:
        return "No data"

def ReadData():
    try:
        File = open("StackData.txt")
        for Line in File:
            PushData(Line.strip())
        File.close()    
    except:
        print("Sorry, File not found")

StackVowel = ["" for _ in range(100)]
StackConsonant = ["" for _ in range(100)]

VowelTop = 0
ConsonantTop = 0

ReadData()
Letters = ""
Flag = False
for x in range(0, 5):
    Flag = False
    while Flag == False:
        Choice = input("Pop Vowel or Consonant: ").lower()
        if Choice == "vowel":
            DataAccessed = PopVowel()
            if DataAccessed != "No data":
                Letters += DataAccessed
                Flag = True
            else:
                print("No vowels left")
        elif Choice == "consonant":
            DataAccessed = PopConsonant()
            if DataAccessed != "No data":
                Letters += DataAccessed
                Flag = True
        else:
            print("No consonants left")
print(Letters)