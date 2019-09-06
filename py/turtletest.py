        # This script is to attempt to simulate
        # a stochiastic "random walk" with the python-turtle

from turtle import Turtle
import random
import colorsys


t=Turtle()
t.screen.bgcolor("black")
t.color("purple")
t.setheading(90)
t.shape("classic")
t.speed(10)

compass = [0,90,180,270]

# north = "t.setheading(90)"
# east = "t.setheading(0)"
# south = "t.setheading(270)"
# west = "t.setheading(180)"


def graph():
    direction = random.choice(compass)
    t.setheading(direction)
    walk_dist = random.randint(1,11)
    t.fd(walk_dist * 40)


def rand_direct(turns,distance):
    direc = 0
    rotation = 360
    for x in range(turns):
        ## Calculating rotation
        # rotation = random.choice([0,60,120,240,300])
        # rotation = random.randint(1,360)
        rotation = roatation * .98

        ## Calculating current facing direction
        direc += rotation
        if direc >= 360:
            direc -= 360


        ## Calculating color

        # hue = (direc%180)/180
        hue = direc/360

        r,g,b = colorsys.hsv_to_rgb(hue,1,1)
        r,g,b = int(r*255), int(g*255), int(b*255)
        color = "#" + hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

        # color = random.choice(["red","green","blue","orange","purple","pink","yellow"])

        t.color(color)
        t.left(rotation)
        t.fd(distance)



def main():
    rand_direct(1000,10)
    t.screen.exitonclick()
    t.screen.mainloop()


if __name__ == '__main__':
    main()
