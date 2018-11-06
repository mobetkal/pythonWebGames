import pyjd
from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.Canvas import Color
from pyjamas.Canvas.ImageLoader import loadImages

class GameCanvas(GWTCanvas):
    def __init__(self, width, height):
        GWTCanvas.__init__(self, width, height)
        self.width = width
        self.height = height
        self.background = ''
        # self.ball = ''
        # self.game = Game(width, height)
        # self.controller = Controller(self.game)
        self.resize(self.width, self.height)
        self.fillRect(0,0,self.width,self.height)
        images = ['./images/background.bmp']#,
                    #'./images/ball.bmp']
        loadImages(images, self)

    def onImagesLoaded(self, imagesHandles):
        self.background = imagesHandles[0]
        # self.ball = imagesHandles[1]
        self.resize(self.width, self.height)
        self.drawImage(self.background, 0, 0)
        # self.controller.startGame(self)

#     def drawBall(self, ball):
#         self.translate(ball.x, ball.y)
#         self.drawImage(self.ball)

# class Ball:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=x

#     def startGame(self, game):
#         self.game = game
#         self.game.start_game(game)

# class Game:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.ball = Ball(250,200)
#         self.game =''

#     def startGame(self, game):
#         self.game = game

#     def update(self):
#         self.game.drawBall(self.ball)

# class Controller:
#     def __init__(self, game):
#         self.game=game

#     def startGame(self, game):
#         self.game = game
#         self.game.startGame(game)  

if __name__ == '__main__':
    pyjd.setup("public/FallingBalls.html")
    c = GameCanvas(500, 400)
    panel = FocusPanel(Widget=c)
    RootPanel().add(panel)
    panel.addKeyboardListener(c)
    panel.setFocus(True)

pyjd.run()
