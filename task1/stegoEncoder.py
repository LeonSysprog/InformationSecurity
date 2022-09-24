import sys
import argparse

replaceSymbols = {
    'A': 'А',
    'a': 'а',
    'B': 'В',
    'E': 'Е',
    'e': 'Е',
    'X': 'Х',
    'x': 'х',
    'T': 'Т',
    'H': 'Н',
    'y': 'у',
    'M': 'М',
    'K': 'К',
    'O': 'О',
    'o': 'о',
    'C': 'С',
    'c': 'с'
}

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--message', action='store', help="message path")
parser.add_argument('-c', '--container', action='store', help="container path")
parser.add_argument('-s', '--stego', action='store', help="stego container path")
args = parser.parse_args()

container = ""
message = ""
stegoContainer = ""

if (args.container):
    container = open(str(args.container), 'r+', encoding='utf-8')
else:
    print('Enter containerPath')
    exit(-1)

if (args.message):
    message = open(str(args.message), 'rb')
else:
    message = sys.stdin

if (args.stego):
    stegoContainer = open(str(args.stego), 'w+', encoding='utf-8')
else:
    stegoContainer = sys.stdout

lines = list(map(lambda x: list(x), message.readlines()))
joinLines = [j for i in lines for j in i]
resList = ['{:08b}'.format(l) for l in joinLines]
resString = ''.join(resList)
#print(resString)

index = 0
for text in container:
    text = list(text)
    for t in text:
        if t in replaceSymbols and index < len(resString):
            if resString[index] == '1': 
                stegoContainer.write(replaceSymbols[t])
            else:
                stegoContainer.write(t)
            index += 1
        else:
            stegoContainer.write(t)