def sum35(val):
    valuelist = []
    for i in range(1,val):
        if i%3 == 0 or i%5 == 0:
            valuelist.append(i)
    return sum(valuelist)

def main():
    print(sum35(1000))

if __name__ == '__main__':
    main()