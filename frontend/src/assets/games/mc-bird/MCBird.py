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
level=0

cookie = document.cookie.split("; ")
dict = {}
for item in cookie:
  k, v = item.split("=")
  dict[k]=v
user = dict["ng-security-user"]
tim = None

class Ball:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.dx=0
        self.dy=0
        self.speed=10 

    def moveUp(self):
        self.dy = -self.speed

    def moveDown(self):
        self.dy = self.speed

    def moveUpAndDown(self):
        self.y += self.dy

        if self.y < 210:
            self.moveDown()
        if self.y >= 322:
            self.y = 322

    def move(self):
        self.x+=self.dx
        if self.x < 0 or self.x > 470:
            self.dx=-self.dx

class Opponent:
    def __init__(self, ball):
        self.x = 470

        randomHeight = random.randint(0,3)
        self.y = Helper.getElevation(randomHeight)


        # self.y = random.randint(280, 322)
        self.speed = 10
        self.ball = ball

    def move(self):
        # self.y+=self.speed
        self.x -= self.speed

    def getElevation(randomNumber):
        out = 0
        if randomNumber == 0:
            out = 322
        if randomNumber == 1:
            out = 280
        if randomNumber == 2:
            out = 200

        return out

        # switcher = {
        #     0: 322,
        #     1: 280,
        #     2: 200,
        # }
        # return switcher.get(randomNumber, 322)

class Helper:
    def getElevation(randomNumber):
        switcher = {
            0: 322,
            1: 280,
            2: 250,
            3: 322,     #to make it more difficult
        }
        return switcher.get(randomNumber, 0)


def updateGame():
    global counter, points, level
    if counter == 50-level:
        opponents.append(Opponent(ball))                                  # UNCOMMENT
        counter=0
        points+=1
        if level < 30:
            level+=1 
    else:
        counter+=1
    for o in opponents:
        o.move()
        if (distance(ball.x+15, ball.y+15, o.x+15, o.y+15)<(50)):
            resetGame()
        if o.x < 0:
            opponents.remove(o) 
    ball.moveUpAndDown()
    drawPoints()
    drawElements()

def resetGame():
    global points, pointsBest, opponents, level, tim
    sendRequest()
    timer.clear_interval(tim)
    ball.x=100
    ball.y=322
    ball.dy=0
    if points>pointsBest:
        pointsBest=points
    points=0
    level=0
    counter=0
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

def drawStartInfo():
    firstLine = "To play, press ENTER..."
    ctx1.font = "14px Arial"
    ctx1.fillStyle = "black"
    ctx1.clearRect(0,0, canvas1.width, canvas1.height)
    ctx1.fillText(firstLine,0,30)
    ctx1.fillText('',0,60)

def sendRequest():
    score = { 'login': user, 'game_name': "MCBird", 'points': points }
    req = ajax.ajax()
    req.open('POST', "http://localhost:5000/score", True)
    req.set_header('Content-Type', 'application/json')
    req.send(score)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2)) + ((y1 - y2) * (y1 - y2))

def process_keyDown(ev):
    global tim
    if(ev.keyCode == 38): # key up
        ball.moveUp()
    elif( ev.keyCode == 40): # key down
        ball.moveDown()   
    elif( ev.keyCode == 13):
        tim = timer.set_interval(updateGame, 1000/gameFPS)  
    ev.preventDefault()
    
document.bind("keydown", process_keyDown)
    
ball = Ball(100, 322)
drawElements()
drawStartInfo()

