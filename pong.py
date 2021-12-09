import turtle
import time
import random

# window setup part

window = turtle.Screen()
window.title = "Pong for AI"
window.bgcolor('#09001C')
window.setup(width=600, height=480)
window.tracer(0)

# score
player = 0
computer = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("#C9C7B5")
pen.penup()
pen.hideturtle()
pen.goto(0,170)

# paddle area

playerPaddle = turtle.Turtle()
playerPaddle.speed(0)
playerPaddle.shape("square")
playerPaddle.color("#C9C7B5")
playerPaddle.penup()
playerPaddle.goto(-250,0)
playerPaddle.shapesize(stretch_wid=3, stretch_len=0.5)

machinePaddle = turtle.Turtle()
machinePaddle.speed(0)
machinePaddle.shape("square")
machinePaddle.color("#C9C7B5")
machinePaddle.penup()
machinePaddle.goto(250,0)
machinePaddle.shapesize(stretch_wid=3, stretch_len=0.5)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.speedInXAxis = 0.1
ball.speedInYAxis = 0.1

# player movement

def paddleUp():
    if (playerPaddle.ycor() >= 215):
        return

    y = playerPaddle.ycor()
    y += 10
    playerPaddle.sety(y)

def paddleDown():
    if (playerPaddle.ycor() <= -215):
        return

    y = playerPaddle.ycor()
    y -= 10
    playerPaddle.sety(y)

def resetGame():
    ball.goto(0,0)
    playerPaddle.goto(-250,0)
    machinePaddle.goto(250,0)
    computer = 0
    pen.clear()
    ball.speedInXAxis = 0.1
    ball.speedInYAxis = 0.1

window.listen()
window.onkeypress(paddleUp, "w")
window.onkeypress(paddleDown, "s")
window.onkeypress(resetGame, "r")

#invincible bot movement
def followBall():
    if ball.xcor() >= 0 and ball.speedInXAxis > 0:
        y = machinePaddle.ycor()
        if ball.ycor() < y:
            y -= 10
            machinePaddle.sety(y)
        if ball.ycor() > y:
            y += 10
            machinePaddle.sety(y)

# main game area

while(True):
    window.update()
# ball movement
    ball.setx(ball.xcor() + ball.speedInXAxis)
    ball.sety(ball.ycor() + ball.speedInYAxis)
    followBall()
    if ball.ycor() >= 240:
        ball.goto(ball.xcor(), ball.ycor() - 10)
        ball.speedInYAxis = - ball.speedInYAxis * random.randint(2,7) * 0.2
    if ball.ycor() <= -240:
        ball.goto(ball.xcor(), ball.ycor() + 10)
        ball.speedInYAxis = - ball.speedInYAxis * random.randint(2,7) * 0.2
# collision
    if ball.ycor() <= playerPaddle.ycor()+40 and ball.ycor() >= playerPaddle.ycor()-40 and ball.xcor() >= playerPaddle.xcor()-5 and ball.xcor() <= playerPaddle.xcor()+5:
        ball.speedInXAxis = - ball.speedInXAxis
    
    if ball.xcor() <= machinePaddle.xcor()+1.5 and ball.xcor() >= machinePaddle.xcor()-1.5:
        ball.speedInXAxis = - ball.speedInXAxis

# points rules
    if ball.xcor() <= -300:
        ball.goto(0,0)
        ball.speedInXAxis = 0.1
        ball.speedInYAxis = 0.1
        computer += 1
        pen.clear()
        pen.write("Player: {}    Computer: {}".format(player, computer) , align="center", font=("Times New Roman", 16, "normal"))

        


