import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
coord = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (x,y) in coord:
    alex.right(x)
    alex.forward(y)
             
wn = turtle.Screen()
alex.pensize(10)
coord_house = [(270,50), (30, 50), (120,50), (120,50), (225,70.1), (225,50), (225,70.1), (225,50) ]

for (x,y) in coord_house:
    alex.right(x)
    alex.forward(y) 

                     