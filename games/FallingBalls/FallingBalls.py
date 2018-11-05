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
        self.resize(self.width, self.height)
        self.fillRect(0,0,self.width,self.height)
    
if __name__ == '__main__':
    pyjd.setup("public/FallingBalls.html")
    c = GameCanvas(800, 600)
    panel = FocusPanel(Widget=c)
    RootPanel().add(panel)
    panel.addKeyboardListener(c)
    panel.setFocus(True)

pyjd.run()
