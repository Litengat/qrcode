from Encrypt import *
from Draw import *
from Read import *
import argparse
import sys
import os

parser = argparse.ArgumentParser(description='Process some integers.')


def main():
    print("What do you want to do?")
    print("1. Generate a Code")
    print("2. Read a Code")
    print("3. Exit the Program")
    UserInput = input()
    if UserInput == "1":
        message = input("What do you want to encrypt? ")
        path = input("Filename:")
        if(path == ""):
            path = 'output'
        path += '.png'
        Binary = TextToBinary(message)

        gernerate(Binary,path)
        print("Finished!")
        
    elif UserInput == "2":
        path = input("Please paste the path... ")
        path += ".png"
        if(os.path.exists(path)):
            Binary = read(path)
            input(BinaryToText(Binary))
        else:
            print("Path dont exists")

    elif UserInput == "3":
        sys.exit()
    

    main()

if __name__ == '__main__':
    main()
