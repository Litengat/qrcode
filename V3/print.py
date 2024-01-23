from Encrypt import *
import math
from svg_turtle import SvgTurtle
t = SvgTurtle()
#import turtle as t
r = 10 

Binary = TextToBinary("UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
print(Binary)


def draw(Binary):
    for i in range(8):
        number = 2 ** i
        for x in range(number):
            if Binary[i + x] == '1':
                t.down()
            else:
                t.up()
            t.circle(r * i, 360 / number, 100)
        t.up() 
        t.sety((r * i)*(-1)) 
        t.down()
    t.pensize(3)
    t.circle(r * (i + 1), 350, 100)
            
draw(Binary)

# with open('V3/example.svg') as f:
#     svg_code = f.read(17)

#t.save_as('V3/example.svg')