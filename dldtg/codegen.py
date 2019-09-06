for i in range(0,8):
    iostring = "INST MUX{}".format(i)
    for j in range(0,8):
        iostring += " I{}<{}>".format(j, i)
    print(iostring)