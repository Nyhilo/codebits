# Returns a unique list of what lines exist in both input files

def read(filename, strip=False):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("File " + filename + " not found.")
        return []
    except:
        print("An error has occured while reading file: " + filename)



def diff(array1, array2):
    diffed = []

    for left in array1:
        for right in array2:
            if left == right and left not in diffed:
                diffed.append(left)

    if strip:
        diffed = [x.strip() for x in diffed]
    
    return diffed


def main():
    import sys
    args = sys.argv

    usage = ("\n\tUsage: py [-s/-strip] diff.py file_1 file_2 \n")

    if len(args) != 3 and len(args) != 4:
        print(usage + "\tArguments given: " + str(len(args)) + " Expected: 3 or 4")
        return

    strip = False

    if args[1] == '-s'.lower() or args[1] == '-strip'.lower():
        files = (args[2], args[3])
        strip = True
    else:
        files = (args[1], args[2])


    if args[-1] == '-s'.lower() or args[-1] == '-strip'.lower():
        strip = True

    diffed = diff(
        read(files[0], strip),
        read(files[1], strip))

    for i in diffed:
        print(i)

if __name__ == '__main__':
    main()


