import turtle

# window setup part

window = turtle.Screen()
window.title = "Pong for AI"
window.bgcolor('#09001C')
window.setup(width=600, height=480)
window.tracer(0)

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
    y = playerPaddle.ycor()
    y += 10
    playerPaddle.sety(y)

def paddleDown():
    y = playerPaddle.ycor()
    y -= 10
    playerPaddle.sety(y)

def resetGame():
    ball.goto(0,0)
    playerPaddle.goto(-250,0)
    machinePaddle.goto(250,0)

window.listen()
window.onkeypress(paddleUp, "w")
window.onkeypress(paddleDown, "s")
window.onkeypress(resetGame, "r")

# main game area

while(True):
    window.update()
# ball movement
    ball.setx(ball.xcor() + ball.speedInXAxis)
    ball.sety(ball.ycor() + ball.speedInYAxis)
    
    if ball.ycor() >= 240 or ball.ycor() <= -240:
        ball.speedInYAxis = - ball.speedInYAxis
    
# collision
    if ball.ycor() <= playerPaddle.ycor()+40 and ball.ycor() >= playerPaddle.ycor()-40 and ball.xcor() >= playerPaddle.xcor()-5 and ball.xcor() <= playerPaddle.xcor()+5:
        ball.speedInXAxis = - ball.speedInXAxis
    
    if ball.xcor() <= machinePaddle.xcor()+1.5 and ball.xcor() >= machinePaddle.xcor()-1.5:
        ball.speedInXAxis = - ball.speedInXAxis

# points rules
    if ball.xcor() <= -300:
        ball.goto(0,0)
