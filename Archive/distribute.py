"""
Testing a distribution of numbers with names attatched.
This program takes a csv of values in the format [NAME, LENGTH] and attempts to
create a random list of total LENGTHS as close to a target value as reasonable.
"""

from random import choice

class distList:
    def __init__(self):
        self.data = []

    def load(self, filename='distribute.csv'):
#        import os.path
#        if not os.path.isfile(filename):   
#            with open(filename+'1', 'w+'): pass
        import csv.reader
        with open(filename,'w+', newline="") as f:
            filereader = csv.reader(f, delimiter=',', quotechar='|')
            for row in filereader:
                self.data.append(row)

def main():
    d = distList()
    d.load()
    print(d.data)

if __name__=='__main__':
    main()

