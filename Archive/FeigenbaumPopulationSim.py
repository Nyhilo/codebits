# 

def ferteq (x,lamb):
    return (lamb*x*(1-x))

def fbaum (fert, pop, gen, verb=True):
    for i in range(1,gen):
        if verb:
            # print(round(pop,4))
            print(pop)
        pop = ferteq(pop,fert)
    return pop

def main ():
    fertility = 4.00000001 # Should be between 1 and 4
    startingPop = .4999750000001 # Should be >0
    generations = 50
    verbose = True
    x=fbaum(fertility,startingPop,generations,verbose)
    print(round(x,4))

if __name__ == '__main__':
    main()