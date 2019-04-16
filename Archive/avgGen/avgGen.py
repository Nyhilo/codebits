from mtranslate import translate
from romanizer import romanize
from random import seed, choice
from transliterate import translit, get_available_language_codes
import sys

def tokenize(filename):
    outlist = []
    with open(filename, 'r') as f:
        outlist = f.read().lower().split()
    return outlist


USAGE=("""Name: avgGen
Usage:
py avgGen.py inputFile langCode1 langCode2 langCode3 ...

Translates and averaged word for word. Using only one langCode will result in a
list of translated words to that language.

Using non latin alphebet laguages will probably result in nothing useful.
""")

def main():
    if (len(sys.argv) < 3):
        print(USAGE)
        return (1)
    filename = sys.argv[1]
    langcodes = sys.argv[2:] 
    tokens = tokenize(filename)
    langlist = []
    for lang in langcodes:
        templist = []
        for token in tokens:
            word = translate(token, lang, 'en').lower()
            if lang in get_available_language_codes():
                word = translit(word, lang, reversed=True)
            templist.append(word)
        langlist.append(templist)
    print(langlist)

    lettergroups = []
    

if __name__ == '__main__':
    main()
