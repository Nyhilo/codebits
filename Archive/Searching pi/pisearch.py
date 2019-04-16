def ConvertToString(num):
  if num < 10:
    return "0" + str(num)
  else: return str(num)

def GetCharacterValues(char):
  outputList = []
  baseValue = ord(char.lower())-97
  while(baseValue < 100):
      outputList.append(ConvertToString(baseValue))
      baseValue += 26
  return outputList
  
def NumberListFromWord(word):
  outputList = []
  for char in word:
    outputList.append(GetCharacterValues(char))
  return outputList

def JoinSublists(someList):
  wordValueList = []
  for sublist in someList:
    wordValueList.append("".join(sublist))
  return wordValueList

def LoadPi(filename='pi.txt'):
  with open(filename, 'r') as file:
    readData = file.read()
  file.close()
  return readData

def FindInPi(string, pi):
  successList = []
  for i in range(0,len(pi)):
    compareString = ""
    if i < len(pi)-len(string):
      for j in range(0,len(string)):
        compareString += pi[i+j]
    if compareString == string:
      successList.append([string,str(i+1)])
  if not successList:
    return ["None Found"]
  else: 
    return successList

def findWordFromList(wordlist, pi):
  successList = []
  for word in wordlist:
    print("Searching", word)
    foundlist = FindInPi(word, pi)
    if foundlist == ["None Found"]:
      print("None Found")
    else:
      print("Found: ",end='')
      for item in foundlist:
        if (item == foundlist[-1]):
          print(item)
        else:
          print(item, end=', ')
        successList.append(item)
  if not successList:
    return ["None Found"]
  else:
    return successList

def main():
  import itertools
  gWorkingWord = "jacob"
  letterlist = NumberListFromWord(gWorkingWord)
  unlinkedWords = list(itertools.product(*letterlist))
  valueList = JoinSublists(unlinkedWords)
  pi = LoadPi()
  shortpi = LoadPi("shortpi.txt")
  
  outputList = findWordFromList(valueList, pi)
  
  with open("output.txt", 'w') as file:
    file.write("String '" + gWorkingWord + "' found " + str(len(outputList))
      + " times at position(s):\n")
    for item in outputList:
      file.write(item[0] + " : " + item[1] + "\n")


if __name__ == '__main__':
  main()