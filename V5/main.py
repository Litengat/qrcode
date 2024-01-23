from Encrypt import *
from Draw import *
from Read import *
import sys

# Binary = TextToBinary("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
# print(Binary)
# gernerate(Binary)


def main():
    print("What do you want to do?")
    print("1. Generate a Code")
    print("2. Read a Code")
    print("3. Exit the Program")
    UserInput = input()
    if UserInput == "1":
        message = input("What do you want to encrypt? ")
        Binary = TextToBinary(message)
        print(Binary)
        gernerate(Binary)
        
    elif UserInput == "2":
        path = input("Please paste the path... ")
        Binary = read(path)
        Binary.reverse()
        print(Binary)
        print(BinaryToText(Binary))
        

    elif UserInput == "3":
        sys.exit()
    

    main()

main()


