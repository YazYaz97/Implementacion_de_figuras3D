import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import cubo
import piramide
import esfera
import cilindro
import superelipsoide

ancho, alto = 500, 500

def init_opengl():
    glClearColor(0.1, 0.1, 0.1, 1)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, ancho / alto, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0, 0, -6)

def mostrar_menu_visual(pantalla):
    pantalla.fill((160, 195, 234))
    fuente = pygame.font.SysFont("Arial", 24)

    lineas = [
        "Tecla                       Acción",
        "1       Mostrar Cubo",
        "_______________________",
        "2       Mostrar Pirámide",
        "_______________________",
        "3       Mostrar Esfera",
        "_______________________",
        "4       Mostrar Cilindro",
        "_______________________",
        "5       Mostrar Superelipsoide",
        "_______________________",
        "6       Salir del programa"
    ]

    for i, texto in enumerate(lineas):
        render = fuente.render(texto, True, (255, 255, 255))
        pantalla.blit(render, (60, 50 + i * 35))

    pygame.display.flip()

def mostrar_menu():
    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Menú de Figuras 3D")
    figura = None
    salir = False

    while not figura and not salir:
        mostrar_menu_visual(pantalla)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                salir = True
            elif evento.type == KEYDOWN:
                if evento.key == K_1:
                    figura = cubo
                elif evento.key == K_2:
                    figura = piramide
                elif evento.key == K_3:
                    figura = esfera
                elif evento.key == K_4:
                    figura = cilindro
                elif evento.key == K_5:
                    figura = superelipsoide
                elif evento.key == K_6 or evento.key == K_ESCAPE:
                    salir = True
        pygame.time.wait(100)

    return figura

def main():
    figura = mostrar_menu()
    if not figura:
        pygame.quit()
        return

    pygame.display.quit()
    pygame.display.init()
    pygame.display.set_mode((ancho, alto), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Implementación de una escena 3D realista con OpenGL")
    init_opengl()

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == QUIT or (evento.type == KEYDOWN and evento.key == K_ESCAPE):
                corriendo = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -6)
        figura.draw()  

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
