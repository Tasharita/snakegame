import turtle
import time
import random

delay= 0.1

score=0
high_score=0

#screen
window=turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0) #turns off the screen updates

#snake head
head=turtle.Turtle()
head.speed(0)#animation speed
head.shape("square")
head.color("green")
head.penup() #denies access to draw which was purpose of turtle
head.goto(0,0)#centre of screen
head.direction="stop"

#food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup() #denies access to draw which was purpose of turtle
food.goto(0,100)#centre of screen

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup() #denies access to draw which was purpose of turtle
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High score 0", align="center", font=("Courier", 24, "normal"))



#functions
def move():
    if head.direction=="up":
        y= head.ycor()
        head.sety(y+20)#move up by 20

    if head.direction=="down":
        y= head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x= head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x= head.xcor()
        head.setx(x+20)

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_up():
    if head.direction != "down":
        head.direction="up"

def go_right():
    if head.direction != "left":
        head.direction="right"


def go_left():
    if head.direction != "right":
        head.direction="left"


#keyboard bindings - sensitivity
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")

#main game loop
while True: #repeats over and over again
    window.update()
    #check collision with border
    if head.ycor()>290 or head.ycor()<-290 or head.xcor()>290 or head.xcor()<-290:
        time.sleep(1)
        pen.write("GAME OVER")
        head.goto(0,0)
        head.direction="stop"
        #hide segments after end of game
        for segment in segments:
            segment.goto(1000,1000) #moves it off the screen


        #clear the segment list
        segments.clear()

        #reset score
        score = 0

        #reset delay
        delay=0.1

    #moving food to random places due to collision
    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        #shorten delay
        delay -=0.001


        #increase score
        score+=10

    if score>high_score:
        high_score=score

        pen.clear()
        pen.write( "Score: {} High score {}" .format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #move end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where head is
    if len(segments) > 0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)




    move()

    #colisions of head and segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)

            #reset delay
            delay = 0.1
            score = 0


    time.sleep(delay)#delays screen





