#!/usr/bin/env python
import sys, string, types, hashlib, base64, re, urllib, binascii
import operator
from collections import Counter

LOWER_LETTERS = [chr(x) for x in range(97, 123)]
UPPER_LETTERS = [chr(x) for x in range(65, 91)]
COMMON_LETTERS = 'ETAOIN SHRDLU'

def xorRepeating():
    plain = raw_input('Please input your Plaintext: ')
    key = raw_input('Key: ')
    hexkey = list()
    i = 0
    for c in key:
        print(i)
        hexkey.append(ord(c))
        i += 1
    resultString = ''
    i = 0
    for char in plain:
        resultString += str(hex(ord(char) ^ hexkey[i]))[2:]
        i += 1
        if i == len(key):
            i = 0
    print(resultString)

def xorBrutePrompt():
    isfile = (raw_input('f for file; for string:') == 'f')
    maxresults = input('How many top hits? ')
    keylength = input('Maximum key length in bytes: ')
    if isfile:
        path = raw_input('path: ')
        path = path.strip()
        results = list()
        with open(path, 'r') as file:
            contents = file.readlines()
            contents = [line.strip() for line in contents]
            for code in contents:
                recursiveResult = xorSingleBrute(code, maxresults, keylength)
                #nach Punkten aufsteigend sortieren:
                sortedList = sorted(recursiveResult.items(), key=operator.itemgetter(1))[-maxresults:]
                #Liste in maximalwert dieser als Tupel anhaengen:
                results.append((sortedList, max(recursiveResult.iteritems(), key=operator.itemgetter(1))[1]))
        #sortieren nach MaxWert:
        sortedResults = sorted(results, key=operator.itemgetter(1))
        for item in sortedResults:
            #da tupel muss so iteriert werden:
            for tupel in item[::2]:
                for i in tupel:
                    print(i[0])
    else:
        encoded = raw_input('Input your Hex String: ')
        result = xorSingleBrute(encoded, maxresults, keylength)
        sortedResults = sorted(result.items(), key=operator.itemgetter(1))[-maxresults:]
        for i, j in sortedResults:
            print(i)


def xorSingleBrute(encoded='', maxresults=20, keybytes=1):
    resultDict = dict()
    if(encoded == ''):
        isfile = (raw_input('f for file; for string:') == 'f')
    for xor_key in range(0, 2**(keybytes*8)):
        decoded = '';
        for i, j in zip(encoded[::2], encoded[1::2]):
            decoded += ''.join(chr(int(i+j, 16) ^ xor_key))
        resultDict[decoded] = commonCounter(decoded)
    return resultDict

def commonCounter(inputString, limit=7):
    countObj = Counter(inputString.upper())
    common = countObj & Counter(COMMON_LETTERS)
    return sum(common.values())

def fixedxor(string1 = '', string2 = ''):
    if(string1 == ''):
        string1 = raw_input('Please input your first hex string: ')
        string2 = raw_input('Please input your second hex string: ')
    hex1 = int(string1, 16)
    hex2 = int(string2, 16)
    result = hex1 ^ hex2
    print(hex(result))

def rot(inputString, amount):
    outputString = '' 
    for char in inputString:
        resultChar = ''
        if char.isupper():
            index = UPPER_LETTERS.index(char)
            resultChar = UPPER_LETTERS[(index + amount)%len(UPPER_LETTERS)]
        elif char.islower():
            index = LOWER_LETTERS.index(char)
            resultChar = LOWER_LETTERS[(index + amount) % len(LOWER_LETTERS)]
        else:
            resultChar = char    
        outputString += resultChar
    return outputString

def translate(inputString, inputType, outputType):
    result = ''
    if(inputType == outputType):
        result = inputString
        return result
        
    if (inputType == 5):
        for char in inputString:
            if(outputType == 1):
                result += str(bin(ord(char))) + ' '
            elif(outputType == 2):
                result += str(ord(char)) + ' '
            elif(outputType == 3):
                result += str(oct(ord(char))) + ' '
            elif(outputType == 4):
                result += str(hex(ord(char))) + ' '
            else:
                result = inputString
                break
        return result
        
    elif(inputType == 1):
        inputString = int(inputString, 2)
    elif(inputType == 2):
        inputString = int(inputString)
    elif(inputType == 3):
        inputString = int(inputString, 8)
    elif(inputType == 4):
        inputString = int(inputString, 16)
    
    if(outputType == 1):
        result = bin(inputString)
    elif(outputType == 2):
        result = inputString
    elif(outputType == 3):
        result = oct(inputString)
    elif(outputType == 4):
        result = hex(inputString)
    elif(outputType == 5):
        result = chr(inputString)
    return result

def string2bin(input):
	return ''.join(format(ord(x), 'b').zfill(8) for x in input)

def hammingDistance(string1, string2):
    diffs = 0
    bin1 = string2bin(string1)
    bin2 = string2bin(string2)
    for b1, b2 in zip(bin1, bin2):
        if b1 != b2:
            diffs += 1
    return diffs

def urlEncoder():
    input = raw_input('Pleae input your String: ')
    print(urllib.quote_plus(input))

def reverser():
    string = raw_input('Please input your string to reverse:')
    print(string[::-1]) 

def base64prompt():
    b64regex = '^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    isfile = (raw_input('f for file, s for string: ') == 'f')
    if isfile:
        path = raw_input('Path: ')
        path = path.strip()
        outputPath = raw_input('Output file: ')
        with open(path, 'r') as file:
            contents = file.read()
            file.close()
            #contents = [line.strip() for line in contents]
        decoded = base64.b64decode(contents)
        with open(outputPath, 'w') as outfile:
            #for line in contents:
            outfile.write(decoded)
            outfile.close()
    else:
        inputString = raw_input('Please input your string: ')
        if (re.match(b64regex, inputString)):
            print(base64.b64decode(inputString))
        else:
            print(base64.b64encode(inputString))


def rotPrompt():
    choice = input('What kind of ROT do you want to perform? 1-25, or all: ')
    userInput = raw_input('Please insert a string: ')
    if type(choice) is types.IntType:
        print(rot(userInput, choice))
    else:
        for i in range(0, 26):
            print(rot(userInput, i))

def translatePrompt():
    print('1: Binary')
    print('2: Decimal')
    print('3: Octal')
    print('4: Hexadecimal')
    print('5: ASCII')
    inputType = input('Please specify input type: ')
    outputType = input('Please specify output type: ')
    if (inputType == 5):
        inputString = raw_input('Please input your strings, seperated by semicolon: ')
    else:
        inputString = raw_input('Please input your values, seperated by semicolon: ')

    inputList = inputString.split(';')
    for entry in inputList:
        print(translate(entry, inputType, outputType))

def hashPrompt():
    typeChoice = raw_input('Would you like to hash a file or a String? f for file, s for string: ')
    algoList = hashlib.algorithms_available
    for word in algoList:
        print(word)
    algoChoice = raw_input('Which hashing algorithm? ')
    if algoChoice in algoList:
        hasher = hashlib.new(algoChoice)
    else:
        print('That\'s no algorithm!')
        sys.exit(0)

    if (typeChoice == 'f'):
        filePath = raw_input('Please input a fully qualified path: ')
        filePath = filePath.strip()
        with open(filePath, 'rb') as hashFile:
            content = hashFile.read()
            hasher.update(content)
    else:
        inputString = raw_input('Please input a string: ')
        hasher.update(inputString)    
    print(hasher.hexdigest())

print('Welcome aboard PankiCrypt Airlines!')
print('How may we serve you today?')
print('1: ROT/Ceasar Encryption')
print('2: Hashing functions')
print('3: Translation')
print('4: Base64 Encoder/Decoder')
print('5: String Reverser')
print('6: URL Encoder')
print('7: Fixed XOR')
print('8: XOR Bruteforce Single Byte ')
print('9: XOR Repeating Key')
choice = raw_input('Please make a selection: ')
if (choice == '1'):
    rotPrompt()
elif (choice == '2'):
    hashPrompt()
elif (choice == '3'):
    translatePrompt()
elif(choice == '4'):
    base64prompt()
elif(choice == '5'):
    reverser()
elif(choice == '6'):
    urlEncoder()
elif(choice[0] == '7'):
    if(len(choice) > 1):
        argList = choice.split(' ')
        fixedxor(argList[1], argList[2])
    else:
        fixedxor()
elif(choice == '8'):
    #xorSingleBrute()
    xorBrutePrompt()
elif(choice == '9'):
    xorRepeating()
print('Thank you for flying with PankiCrypt Airlines!')

