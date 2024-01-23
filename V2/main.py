import cv2
from GenerateCode import *
from ReadCode import *
import requests
import time
import sys

def main():
    print("What do you want to do?")
    print("1. Encrypt a Message")
    print("2. Decrypt a Code")
    print("3. Exit the Program")
    UserInput = input()
    if UserInput == "1":
        UserInput = input("What do you want to encrypt? ")
        DisplayInformation(PrepareInformation(UserInput))
        
    elif UserInput == "2":
        Link = input("Please paste the Image link... ")
        img_data = requests.get(Link).content
        with open('IMG/Code.png', 'wb') as handler:
            handler.write(img_data)
        CropFromPhoto()
        print(BinaryToText(ReadFromImage()))

    elif UserInput == "3":
        sys.exit()
    


    time.sleep(1)
    main()

main()
