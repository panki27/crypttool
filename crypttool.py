#!/usr/bin/env python
import sys, string, types, hashlib

LOWER_LETTERS = [chr(x) for x in range(97, 123)]
UPPER_LETTERS = [chr(x) for x in range(65, 91)]

def rot(inputString, amount):
	outputString = "" 
	for char in inputString:
		resultChar = ""
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
	result = ""
	if(inputType == outputType):
		result = inputString
		return result
		
	if (inputType == 5):
		for char in inputString:
			if(outputType == 1):
				result += str(bin(ord(char))) + " "
			elif(outputType == 2):
				result += str(ord(char)) + " "
			elif(outputType == 3):
				result += str(oct(ord(char))) + " "
			elif(outputType == 4):
				result += str(hex(ord(char))) + " "
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

def rotPrompt():
	choice = input("What kind of ROT do you want to perform? 1-25, or all: ")
	userInput = raw_input("Please insert a string: ")
	if type(choice) is types.IntType:
		print(rot(userInput, choice))
	else:
		for i in range(0, 26):
			print(rot(userInput, i))

def translatePrompt():
	print("1: Binary")
	print("2: Decimal")
	print("3: Octal")
	print("4: Hexadecimal")
	print("5: ASCII")
	inputType = input("Please specify input type: ")
	outputType = input("Please specify output type: ")
	if (inputType == 5):
		inputString = raw_input("Please input your strings, seperated by semicolon: ")
	else:
		inputString = raw_input("Please input your values, seperated by semicolon: ")

	inputList = inputString.split(";")
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
		print("That's no algorithm!")
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

print("Welcome aboard PankiCrypt Airlines!")
print("How may we serve you today?")
print("1: ROT/Ceasar Encryption")
print("2: Hashing functions")
print("3: Translation")

choice = input("Please make a selection: ")

if (choice == 1):
	rotPrompt()
elif (choice == 2):
	hashPrompt()
elif (choice == 3):
	translatePrompt()
print("Thank you for flying with PankiCrypt Airlines!")

