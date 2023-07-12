from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def findZone(x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0

    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            return 0
        elif dx < 0 and dy > 0:
            return 3
        elif dx < 0 and dy < 0:
            return 4
        else:
            return 7

    else:
        if dx > 0 and dy > 0:
            return 1
        elif dx < 0 and dy > 0:
            return 2
        elif dx < 0 and dy < 0:
            return 5
        else:
            return 6
def zone0Cnvt(zone, x, y):

    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y
def zone02Orig(zone, x, y):

    if zone == 0:
        return x, y
    if zone == 1:
        return y, x
    if zone == 2:
        return -y, -x
    if zone == 3:
        return -x, y
    if zone == 4:
        return -x, -y
    if zone == 5:
        return -y, -x
    if zone == 6:
        return y, -x
    if zone == 7:
        return x, -y

def drawLine(zone, x0, y0, x1, y1):

    dy = y1-y0
    dx = x1-x0
    init = 2*dy - dx
    E = 2*dy
    NE = 2*(dy-dx)

    x = x0
    y = y0

    while x <= x1:

        a, b = zone02Orig(zone, x, y)
        draw_points(a, b)

        if init <= 0:
            x += 1
            init += E

        else:
            x += 1
            y += 1
            init += NE

def eightSym(x0, y0, x1, y1):
    zone = findZone(x0, y0, x1, y1)
    x00, y00 = zone0Cnvt(zone, x0, y0)
    x10, y10 = zone0Cnvt(zone, x1, y1)
    drawLine(zone, x00, y00, x10, y10)


def five():
    x0 = 10
    y0 = 400
    x1 = 100
    y1 = 400
    eightSym(x0, y0, x1, y1)
    x0 = 10
    y0 = 400
    x1 = 10
    y1 = 300
    eightSym(x0, y0, x1, y1)
    x0 = 10
    y0 = 300
    x1 = 100
    y1 = 300
    eightSym(x0, y0, x1, y1)
    x0 = 100
    y0 = 300
    x1 = 100
    y1 = 200
    eightSym(x0, y0, x1, y1)
    x0 = 10
    y0 = 200
    x1 = 100
    y1 = 200
    eightSym(x0, y0, x1, y1)
def zero():
    x0 = 200
    y0 = 400
    x1 = 300
    y1 = 400
    eightSym(x0, y0, x1, y1)
    x0 = 200
    y0 = 400
    x1 = 200
    y1 = 200
    eightSym(x0, y0, x1, y1)
    x0 = 300
    y0 = 400
    x1 = 300
    y1 = 200
    eightSym(x0, y0, x1, y1)
    x0 = 200
    y0 = 200
    x1 = 300
    y1 = 200
    eightSym(x0, y0, x1, y1)
def draw_points(x, y):
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
def iterate():
    glViewport(0, 0, 500, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    five()
    zero()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 600)
glutInitWindowPosition(0, 0)
# window name
wind = glutCreateWindow("LAb2:Brasenshams Line Algorithm")
glutDisplayFunc(showScreen)
glutMainLoop()