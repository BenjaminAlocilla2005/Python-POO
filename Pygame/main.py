import pygame 
from RectanguloPequeño import RectangunloPequeno
from RectanguloGrande import RectangunloGrande
# Inicio de la Biblioteca
pygame.init()

# Setseo de la ventana
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Colision Rectangular en Pygame") # titulo de la ventana

# Color fondo (variante)
background = (30,30,30) # negro
color_colision = (234, 63, 63)

# Instancias de los rectangulos
RectangunloPequeno = RectangunloPequeno(200, 200, 100, 100)
RectangunloGrande = RectangunloGrande(400, 300, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    teclas = pygame.keys.get_pressed()

    pos_anterior_pequeno = RectangunloPequeno.obtener_posicion()
    pos_anterior_grande = RectangunloGrande.obtener_posicion()

    RectangunloPequeno.mover(teclas)
    RectangunloGrande.mover(teclas)

    if RectangunloPequeno.rect.colliderect(RectangunloGrande.rect):
        RectangunloPequeno.restablecer_posicion(*pos_anterior_pequeno)
        RectangunloGrande.restablecer_posicion(*pos_anterior_grande)
        RectangunloPequeno.cambiar_color(color_colision)
        RectangunloGrande.cambiar_color(color_colision)
    else:
        RectangunloPequeno.cambiar_color((63, 145, 45))
        RectangunloGrande.cambiar_color((56, 200, 67))

    ventana.fill(background)
    RectangunloPequeno.dibujar(ventana)
    RectangunloGrande.dibujar(ventana)

    pygame.display.update()

pygame.quit()