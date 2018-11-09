import pyjd
from pyjamas import DOM
from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.RootPanel import RootPanel, RootPanelCls
from pyjamas.Canvas import Color
from pyjamas.Canvas.ImageLoader import loadImages
from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.ui.KeyboardListener import KeyboardHandler
from pyjamas.ui import Event
from pyjamas.Timer import Timer
import random

class GameCanvas(GWTCanvas):
    def __init__(self, width, height):
        GWTCanvas.__init__(self, width, height)
        self.width = width
        self.height = height
        self.background = ''
        self.ball = ''
        self.game = Game(width, height)
        self.controller = Controller(self.game)
        # self.resize(self.width, self.height)
        # self.fillRect(0,0,self.width,self.height)       
        images = ['./images/background.png',
                    './images/ball.png',
                    './images/ball2.png']
        loadImages(images, self)
        self.sinkEvents(Event.KEYEVENTS)

    def onImagesLoaded(self, imagesHandles):
        self.background = imagesHandles[0]
        self.ball = imagesHandles[1]
        self.opponent = imagesHandles[2]
        self.resize(self.width, self.height)
        self.drawImage(self.background, 0, 0)
        self.controller.startGame(self)
        
    def addTo(self, panel):
        panel.add(self)
        self.top = DOM.getAbsoluteTop(self.getElement())
        self.left = DOM.getAbsoluteLeft(self.getElement())

    def setKey(self, k, set):
        DOM.eventPreventDefault(DOM.eventGetCurrentEvent())
        if k == 39:
            self.controller.keyLeft = set
        elif k == 37:
            self.controller.keyRight = set

    def onKeyDown(self, sender, keyCode, modifiers = None):
        self.setKey(keyCode, True)

    def onKeyUp(self, sender, keyCode, modifiers = None):
        self.setKey(keyCode, False)

    def drawBall(self, ball):
        self.saveContext()
        self.translate(ball.x, ball.y)
        self.drawImage(self.ball, 0, 0)
        self.restoreContext()

    def drawOpponent(self, opponent):
        self.saveContext()
        self.translate(opponent.x, opponent.y)
        self.drawImage(self.opponent, 0, 0)
        self.restoreContext()

    def drawElements(self):
        self.fillRect(0,0,self.width,self.height)
        self.drawImage(self.background, 0, 0)
        for o in self.game.opponents:
            self.drawOpponent(o)
        self.drawBall(self.game.ball)

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
        self.speed=random.randint(10,20)
        self.ball=ball

    def move(self):
        self.y+=self.speed

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball = Ball(235,322)
        self.canvas = ''
        self.counter=0
        self.opponents=[]

    def startGame(self, canvas):
        self.canvas = canvas

    def update(self):
        if self.counter == 10:
            self.opponents.append(Opponent(self.ball))
            self.counter=0
        else:
            self.counter+=1
        for o in self.opponents:
            o.move()
            if o.y > 420:
                self.opponents.remove(o) 
        self.ball.move()
        self.canvas.drawElements()

class Controller:
    def __init__(self, game):
        self.game=game
        self.keyLeft = False
        self.keyRight = False

    def startGame(self, canvas):
        self.canvas = canvas
        self.game.startGame(canvas)  
        self.timer = Timer(notify=self.update)
        self.timer.scheduleRepeating(35)

    def update(self):
        self.pressedKey()
        self.game.update()

    def pressedKey(self):
        ball = self.game.ball
        if self.keyLeft:
            ball.moveLeft()
        if self.keyRight:
            ball.moveRight()

class RootPanelListener(RootPanelCls, KeyboardHandler, ClickHandler):
    def __init__(self, Parent, *args, **kwargs):
        self.Parent = Parent
        self.focussed = False
        RootPanelCls.__init__(self, *args, **kwargs)
        ClickHandler.__init__(self)
        KeyboardHandler.__init__(self)
        self.addClickListener(self)

    def onClick(self, Sender):
        self.focussed = not self.focussed
        self.Parent.setFocus(self.focussed)

if __name__ == '__main__':
    pyjd.setup("public/FallingBalls.html")
    c = GameCanvas(500, 400)
    panel = FocusPanel(Widget=c)
    RootPanel().add(panel)
    panel.addKeyboardListener(c)
    panel.setFocus(True)
    pyjd.run()
