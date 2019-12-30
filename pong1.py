import turtle

nameA = input("Please input player A name: ")
nameB = input("Please input player B name: ")

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stop window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation, set speed to max possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0) # start in the middle, left side of screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation, set speed to max possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0) # start in the middle, right side of screen

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation, set speed to max possible speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0) # start in the middle of the screen
ball.dx = 2 # everytime the ball moves, it moves by 2 pixels
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write((nameA + " : 0" + " " + nameB +  " : 0").format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() # from turtle module, returns y coordinate
    y += 20 # add 20 to the "y" coordinate
    paddle_a.sety(y) # set "y" to the new "y" position

def paddle_a_down():
    y = paddle_a.ycor() # from turtle module, returns y coordinate
    y -= 20 # subtract 20 to the "y" coordinate
    paddle_a.sety(y) # set "y" to the new "y" position

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() # everytime the loop runs, update screen

    # Move the Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # reverse ball's direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # reverse ball's direction

    if ball.xcor() > 390:
        ball.goto(0, 0) # reset ball's position if it goes off the screen
        ball.dx *= -1
        ball.dx = 2
        ball.dy = 2
        score_a += 1
        pen.clear()
        pen.write((nameA + " : {} " + nameB +  " : {}").format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0) # reset ball's position if it goes off the screen
        ball.dx = 2
        ball.dy = 2
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write((nameA + " : {}" + " " + nameB +  " : {}").format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx += 0.5
        ball.dy += 0.5
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        ball.dx += 0.5
        ball.dy += 0.5