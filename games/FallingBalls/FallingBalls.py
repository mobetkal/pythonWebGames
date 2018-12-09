from browser import window, document, timer, html, ajax
import javascript, random, math

gameFPS = 35
canvas = document["stage"]
ctx = canvas.getContext("2d")
canvas1 = document["score"]
ctx1 = canvas1.getContext("2d")
imgBack = document["background"]
imgBall = document["ball"]
imgOpp =  document["opponent"]

counter=0
opponents=[]
points=0
pointsBest=0
user = "user"

class Ball:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.dx=0
        self.speed=10

    def moveLeft(self):
            self.dx=self.speed

    def moveRight(self):
            self.dx=-self.speed

    def move(self):
        self.x+=self.dx
        if self.x < 0 or self.x > 470:
            self.dx=-self.dx

class Opponent:
    def __init__(self, ball):
        self.x=random.randint(0,470)
        self.y=-15
        self.speed=random.randint(15,25)
        self.ball=ball

    def move(self):
        self.y+=self.speed


def updateGame():
    global counter, points
    if counter == 10:
        opponents.append(Opponent(ball))
        counter=0
        points+=1
    else:
        counter+=1
    for o in opponents:
        o.move()
        if (distance(ball.x+15, ball.y+15, o.x+15, o.y+15)<(50)):
            resetGame()
        if o.y > 420:
            opponents.remove(o) 
    ball.move()
    drawPoints()
    drawElements()

def resetGame():
    global points, pointsBest, opponents
    sendRequest()
    ball.x=235
    ball.y=322
    ball.dx=0
    if points>pointsBest:
        pointsBest=points
    points=0
    opponents=[]

def drawElements():
    drawBackground()
    for o in opponents:
        drawOpponent(o)
    drawBall()

def drawBackground():
    ctx.clearRect(0,0, canvas.width, canvas.height)
    ctx.drawImage(imgBack, 0, 0)

def drawOpponent(opponent):
    ctx.save()
    ctx.translate(opponent.x, opponent.y)
    ctx.drawImage(imgOpp, 0, 0)
    ctx.restore()

def drawBall():
    ctx.save()
    ctx.translate(ball.x, ball.y)
    ctx.drawImage(imgBall, 0, 0)
    ctx.restore()

def drawPoints():
    global points, pointsBest
    firstLine = "Current score: " + str(points)
    secondLine = "Best score: " + str(pointsBest)
    ctx1.font = "14px Arial"
    ctx1.fillStyle = "black"
    ctx1.clearRect(0,0, canvas1.width, canvas1.height)
    ctx1.fillText(firstLine,0,30)
    ctx1.fillText(secondLine,0,60)

def sendRequest():
    score = { "user": user, "score": points }
    req = ajax.ajax()
    req.open('POST', "http://localhost:5000/score", True)
    req.send(score)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))

def process_keyDown(ev):
    if(ev.keyCode == 37):
        ball.moveRight()
    elif( ev.keyCode == 39):
        ball.moveLeft()     
    ev.preventDefault()
    
document.bind("keydown", process_keyDown)
    
ball = Ball(235, 322)

timer.set_interval(updateGame, 1000/gameFPS)