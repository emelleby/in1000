from ezgraphics import GraphicsWindow
win  = GraphicsWindow()
canvas = win.canvas()
canvas.drawRect(100,100,50,50)
canvas.drawRect(75,150,100,100)
win.wait()
