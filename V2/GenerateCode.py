from Encrypt import *
import random

HTML_FORMAT = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ENCRYPTION</title>
        <link rel="stylesheet" href="main.css">
    </head>
    """

def PrepareInformation(message):
    length = len(message)
    if length > 80:
        print("your message is too long! (max 80 chars)")
        return 
    if length < 10:
        length = "0" + str(length)
    else:
        length = str(length)

    length = TextToBinary(length)
    message = TextToBinary(message)

    return [length, message]

def DisplayInformation(List):
    length = List[0]
    message = List[1]
    UsedBits = len(length) + len(message)
    RemaindingBits = 800 - UsedBits

    output = HTML_FORMAT +  '<div class="Frame">'
    for i in length:
        if i == "0":
            output += '<div class="Tile Black"></div>'
        if i == "1": 
            output += '<div class="Tile White"></div>'
    

    for i in message:
        if i == "0":
            output += '<div class="Tile Black"></div>'
        if i == "1": 
            output += '<div class="Tile White"></div>'
    
    for i in range(RemaindingBits):
        if random.random() > 0.5:
            output += '<div class="Tile Black"></div>'
        else:
            output += '<div class="Tile White"></div>'

    output += """</div>
    </body>
    </html>"""

    f = open("WEB/Generator.html", "w")
    f.write(output)
    f.close()


    
if __name__ == '__main__': 
    DisplayInformation(PrepareInformation("Hallo"))