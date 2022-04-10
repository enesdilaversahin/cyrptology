MAX_KEY_VALUE=26
def getType():
    while True:
        type = input("Encyrpt or decrypt ? (e or d): ")
        if(type=="e" or type=="d"):
            return type
        else:
            print("Enter e to encrypt or d to decrypt: ")
def getKey():
    while True:
        key = int(input("enter a key value 1-{}: ".format(MAX_KEY_VALUE)))
        if(key>=1 and key<=26):
            return key
        else:
            print("enter a  key value  1-{}: ".format(MAX_KEY_VALUE))
def getMessage(message,key,type):
    if type == "d":
        key = -key
    translated = ""
    for letter in message:
        if letter.isalpha():
            newLetter = ord(letter)
            newLetter += key
            if letter.isupper():
                if newLetter > ord("Z"):
                    newLetter -= 26
                elif newLetter < ord("A"):
                    newLetter += 26
            elif letter.islower():
                if newLetter > ord("z"):
                    newLetter -= 26
                elif newLetter < ord("a"):
                    newLetter += 26
            translated +=chr(newLetter)
        else:
            translated+=letter
    return translated


type = getType()
key = getKey()
message = input("enter message : ")

print("decrypt message: {}".format(getMessage(message,key,type)))
