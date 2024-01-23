from Dictionaries import *

def TextToBinary(text):
    result = ""
    for i in text:
        if i == "Ö" or i == "Ä" or i == "Ü":
            i = i.lower()
        result += TTB[i]
    return result

def BinaryToText(Binary):
    result = ""
    for i in range(int(len(Binary)/8)):
        result += BTT[Binary[:8]]
        Binary = Binary[8:]
    return result

def Test(text):
    result = ""
    for i in text:
        if i == "Ö":
            i = i.lower()
        result += i
    return result

