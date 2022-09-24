import sys
import argparse
from itertools import zip_longest

replaceSymbols = {
    'А': 'A',
    'а': 'a',
    'В': 'B',
    'Е': 'E',
    'е': 'e',
    'Х': 'X',
    'х': 'x',
    'Т': 'T',
    'Н': 'H',
    'у': 'y',
    'М': 'M',
    'К': 'K',
    'О': 'O',
    'о': 'o',
    'С': 'C',
    'с': 'c'
}

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', action='store', help="decoded message path")
parser.add_argument('-s', '--stego', action='store', help="stego container path")
args = parser.parse_args()

decodeMessage = ""
stegoContainer = ""

if (args.message):
    decodeMessage = open(str(args.message), 'w+', encoding='utf-8')
else:
    decodeMessage = sys.stdout

if (args.stego):
    stegoContainer = open("stegoContainer.txt", 'r+', encoding='utf-8')
else:
    stegoContainer = sys.stdin

resList = []

for text in stegoContainer:
    text = list(text)
    for t in text:
        if t in replaceSymbols:
            resList.append('1')
        elif t in replaceSymbols.values():
            resList.append('0')

it = iter(map(str, resList))
bytesArray = [int("".join(chunck), 2) for chunck in zip_longest(*iter([it] * 8), fillvalue="")]
for byteChar in bytesArray:
    decodeMessage.write(chr(byteChar))