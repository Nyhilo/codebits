def calculate(n=1000):
    numlist = [1]
    for i in range(1,n):
        sub = numlist[-1]-i
        if sub < 1 or sub in numlist:
            numlist.append(numlist[-1]+i)
        else:
            numlist.append(sub)
        print("{:>5}: {}".format(i, numlist[-1]))

if __name__ == "__main__":
    calculate()
