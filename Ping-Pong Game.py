import turtle as t 
playerAscore=0
playerbscore=0

window=t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

#creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid= 5 ,stretch_len= 1 )
leftpaddle.penup()
leftpaddle.goto(-350,0)

#creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid= 5 ,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.5
ballydirection=0.5

#craeting pen for scorecard updata
pen=t.Turtle()
pen.speed(0)
pen.color("Yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center",font=('Arial',36,'normal'))

#moving the leftpaddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+30
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-30
    leftpaddle.sety(y)

#moving the rightpaddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+30
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-30
    rightpaddle.sety(y)

#assign keys to play

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'i')
window.onkeypress(rightpaddledown,'k')

#Main Game Loop
while True:
    window.update()
    #moving the ball
    ball.setx(ball.xcor()+ ballxdirection)
    ball.sety(ball.ycor()+ ballydirection)

    #seetingup bprder
    if ball.ycor()> 290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("player A:{}          player B: {}".format(playerAscore,playerbscore),align='center',font=('Arial',24,'normal'))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerbscore=playerbscore+1
        pen.clear()
        pen.write("player A:{}          player B: {}".format(playerAscore,playerbscore),align='center',font=('Arial',24,'normal'))

    if(ball.xcor()>345)and(ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(345)
        ballxdirection=ballxdirection * -1
    

    
    if(ball.xcor()<-345) and (ball.xcor()>-350) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-345)
        ballxdirection=ballxdirection * -1

        