from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_triangle(x0,y0,x1,y1,x2,y2):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_TRIANGLES)
    glVertex2f(x0, y0)  # jekhane show korbe pixel
    glVertex2f(x1, y1)  # jekhane show korbe pixel
    glVertex2f(x2, y2)  # jekhane show korbe pixel

    glEnd()


def draw_Quads(x0,y0,x1,y1,x2,y2,x3,y3):
    glPointSize(5)  # pixel size. by default 1 thake
    glBegin(GL_QUADS)

    glVertex2f(x0, y0)  # jekhane show korbe pixel
    glVertex2f(x1, y1)  # jekhane show korbe pixel
    glVertex2f(x2, y2)  # jekhane show korbe pixel
    glVertex2f(x3, y3)  # jekhane show korbe pixel

    glEnd()
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_Quads(0,0,200,0,200,200,0,200)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()