from collections import deque

###Code for Encryption of Text

alphaKey = ["0","1","2","3","4","5","6","7","8","9"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
shiftKey = int(input("Input Random Number: "))#The number to rotate for the cipherr

cipherKey = deque(alphaKey) #convert to a deque to use easy rotation
cipherKey.rotate(shiftKey) #rotate the list
cipherKey = list(cipherKey) #convert back to list



rawText = input("Input Text to Convert in Alpha Numeric Characters Only & Space: ").upper()
rawText = list(rawText) #convert the raw text to a list

encodedText = ""

for letter in rawText: #iterate through the list and find the corresponding letter in the cipherKey list
	encodedText = encodedText + cipherKey[alphaKey.index(letter)]


print (encodedText)
