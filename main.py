import random
from turtle import *
import colorsys
danielito={"daniel":"eso tilin"}
tilin= input("decime daniel")
if tilin in danielito.keys():
    print (danielito[tilin])
else:
    bgcolor("red")
    pencolor("black")
    print("maatate cabron")
    title ("no me dijiste daniel :(")
    texto=("matate cabron")
    color("black")
    penup()
    goto(0,0)
    pendown()
    write(texto,align="left",font=("calibri",12,"normal"))

    mainloop()

