import turtle
import random
from time import sleep

#Global variables for the stars cordinate
starNumOneX = 0
starNumOneY = 240
starNumTwoX = 150
starNumTwoY = 100
starNumThreeX = 120
starNumThreeY = -150
starNumFourX = -110
starNumFourY = -170
starNumFiveX = -130
starNumFiveY = -210
starNumSixX = -150
starNumSixY = 120
starNumSevenX = -250
starNumSevenY = 100
starNumEightX = 100
starNumEightY = 280

turtle.setup(width=1.0, height=1.0)
turtle.speed(30)
turtle.hideturtle()


def introOne(x):
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 100)
    turtle.write(
        "Midterm Project", font=("Arial", 24, "italic"), align="center")
    turtle.right(90)
    turtle.forward(100)
    turtle.write(
        "The Libra Constellation",
        font=("Arial", 24, "italic"),
        align="center")
    turtle.forward(100)
    turtle.write(
        "Asharaful Islam", font=("Arial", 24, "italic"), align="center")
    sleep(x)


def PicTwo(x):
    turtle.clearscreen()
    turtle.pu()
    turtle.setposition(0, 100)
    turtle.pd()
    turtle.bgcolor("black")
    turtle.bgpic("Asharaful_libra.gif")
    turtle.update()
    sleep(x)
    turtle.clearscreen()


def drawThree(x):
    #This will drow dots and name of the stars.
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(starNumOneX, starNumOneY)
    turtle.dot(20)
    turtle.write('Zuben Elschemali')
    turtle.goto(starNumTwoX, starNumTwoY)
    turtle.dot(20)
    turtle.write('Zuben Elgenubi')
    turtle.goto(starNumThreeX, starNumThreeY)
    turtle.dot(15)
    turtle.write('Brachium')
    turtle.goto(starNumFourX, starNumFourY)
    turtle.dot(10)
    turtle.write('Upsilon Librae')
    turtle.goto(starNumFiveX, starNumFiveY)
    turtle.dot(10)
    turtle.write('Tau Librae')
    turtle.goto(starNumSixX, starNumSixY)
    turtle.dot(10)
    turtle.write('Zuben Elakrab')
    turtle.goto(starNumSevenX, starNumSevenY)
    turtle.dot(10)
    turtle.write('Theta Librae')
    turtle.goto(starNumEightX, starNumEightY)
    turtle.dot(10)
    turtle.write('Zuben Elakribi')
    #drow line
    turtle.goto(starNumOneX, starNumOneY)
    turtle.pendown()
    turtle.goto(starNumTwoX, starNumTwoY)
    turtle.goto(starNumThreeX, starNumThreeY)
    turtle.penup()
    turtle.goto(starNumFourX, starNumFourY)
    turtle.pendown()
    turtle.goto(starNumFiveX, starNumFiveY)
    turtle.goto(starNumFourX, starNumFourY)
    turtle.goto(starNumSixX, starNumSixY)
    turtle.goto(starNumTwoX, starNumTwoY)
    turtle.goto(starNumSixX, starNumSixY)
    turtle.goto(starNumOneX, starNumOneY)
    sleep(x)


# This will move the turtle to different location


def moveToRandomLocation():
    turtle.penup()
    turtle.setpos(random.randint(-400, 400), random.randint(-400, 400))
    turtle.pendown()


#This function will draw a star of a particular size
def drawStar(starSize, starColour):
    turtle.color(starColour)
    turtle.pendown()
    turtle.begin_fill()
    for side in range(5):
        turtle.left(144)
        turtle.forward(starSize)
    turtle.end_fill()
    turtle.penup()


def drawGalaxy(numberOfStars):
    starColours = ["4B8BBE", "4B8BBE", "4B8BBE"]
    moveToRandomLocation()
    #draw lots of small coloured stars
    for star in range(numberOfStars):
        turtle.penup()
        turtle.left(random.randint(-180, 180))
        turtle.forward(random.randint(5, 20))
        turtle.pendown()
        #draw a small star in a random colour
        drawStar(2, random.choice(starColours))


def starFour(x):
    turtle.clearscreen()
    turtle.hideturtle()

    turtle.bgcolor("black")
    turtle.color("red")

    #This will drowing the polts and the names of the stars
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(starNumOneX, starNumOneY)
    drawStar(20, "orange")
    turtle.write('Zuben Elschemali')
    turtle.goto(starNumTwoX, starNumTwoY)
    drawStar(20, "skyblue")
    turtle.write('Zuben Elgenubi')
    turtle.goto(starNumThreeX, starNumThreeY)
    drawStar(15, "red")
    turtle.write('Brachium')
    turtle.goto(starNumFourX, starNumFourY)
    drawStar(10, "yellow")
    turtle.write('Upsilon Librae')
    turtle.goto(starNumFiveX, starNumFiveY)
    drawStar(10, "pink")
    turtle.write('Tau Librae')
    turtle.goto(starNumSixX, starNumSixY)
    drawStar(10, "skyblue")
    turtle.write('Zuben Elakrab')
    turtle.goto(starNumSevenX, starNumSevenY)
    drawStar(5, "gold")
    turtle.write('Theta Librae')
    turtle.goto(starNumEightX, starNumEightY)
    drawStar(5, "silver")
    turtle.write('Zuben Elakribi')
    #lines
    turtle.goto(starNumOneX, starNumOneY)
    turtle.pendown()
    turtle.goto(starNumTwoX, starNumTwoY)
    turtle.goto(starNumThreeX, starNumThreeY)
    turtle.penup()
    turtle.goto(starNumFourX, starNumFourY)
    turtle.pendown()
    turtle.goto(starNumFiveX, starNumFiveY)
    turtle.goto(starNumFourX, starNumFourY)
    turtle.goto(starNumSixX, starNumSixY)
    turtle.goto(starNumTwoX, starNumTwoY)
    turtle.goto(starNumSixX, starNumSixY)
    turtle.goto(starNumOneX, starNumOneY)
    turtle.speed(1050)
    #draw 30 stars (random sizes/locations)
    for star in range(30):
        moveToRandomLocation()
        drawStar(random.randint(5, 30), "White")

    turtle.speed(1050)
    turtle.update()


runTime = 4
introOne(runTime)
PicTwo(runTime)
drawThree(runTime)
starFour(runTime)
