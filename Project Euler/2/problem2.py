def evenFib(n):
    sequence = [0,1,2]
    totalList = [2]
    currentChar = 0
    counter = 3
    while True:
        currentChar = sequence[counter-1]+sequence[counter-2]
        if currentChar>n: break
        if currentChar%2==0:
            totalList.append(currentChar)
        sequence.append(currentChar)
        counter+=1

    # print(sequence)   #Debugging
    return sum(totalList)

def main():
    print(evenFib(4000000))

if __name__ == '__main__':
    main()