import math

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np


def applyParameter(radius, u, v):
    return math.cos(u) * radius, math.sin(u) * radius, v


def createVertice(radius, u, v):
    vertices = []
    i = 0
    while i < len(v) - 1:
        j = 0
        while j < len(u) - 1:
            vertices.append(applyParameter(radius, u[j], v[i]))
            vertices.append(applyParameter(radius, u[j + 1], v[i]))
            vertices.append(applyParameter(radius, u[j + 1], v[i + 1]))
            vertices.append(applyParameter(radius, u[j], v[i]))
            vertices.append(applyParameter(radius, u[j], v[i + 1]))
            vertices.append(applyParameter(radius, u[j + 1], v[i + 1]))
            j += 1
        i += 1

    return vertices


def runEdges(vertices):
    for k in range(1, len(vertices) - 1):
        glVertex3fv(vertices[k - 1], vertices[k])
        glVertex3fv(vertices[k], vertices[k + 1])


def cylinder(vertices):
    glLineWidth(2)
    glBegin(GL_LINES)
    runEdges(vertices)

    glEnd()


def main():
    radius = 3.0
    height = 2.0

    face_p = np.arange(0.0, height + 0.3, 0.3)
    radius_p = np.arange(0.0, np.pi * 2 + np.pi / 10, np.pi / 10)
    vertices = createVertice(radius, radius_p, face_p)

    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(40, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -15)

    glRotatef(45, 45, 45, 45)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        cylinder(vertices)
        pygame.display.flip()
        pygame.time.wait(10)


main()
