import pygame
import random
import math
import io
from pygame import mixer

def fuente_bytes(fuente):
    # Abre el archivo TTF  en modo lectura binaria
    with open(fuente, 'rb') as f:
        # Lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto BytesIO a partir de los bytes del archvio TTF
    return io.BytesIO(ttf_bytes)
# Inicializar Pygame
pygame.init()


#Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

#Título e Icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.png')


# Agregar música
mixer.music.load('musica_fondo.mp3')
mixer.music.set_volume(0.75)
mixer.music.play(-1)


NAVE_MEDIO_Y = 10
NAVE_MEDIO_X = 4

#Variables de jugador
img_jugador = pygame.image.load('astronave.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0
game_over = False


#Variables de enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(25,200))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(50)

#Variables de la bala
balas = []
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 2
bala_visible = False

# Puntaje
puntaje = 0
fuente_como_bytes1 = fuente_bytes('Fastest.ttf')
fuente_como_bytes2 = fuente_bytes('Begok v15_2015___free.ttf')
fuente = pygame.font.Font('Begok v15_2015___free.ttf', 32)
texto_x = 10
texto_y = 10

# Texto final
fuente_final = pygame.font.Font(fuente_como_bytes1, 50)

def texto_final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (200, 250))



# Función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f'puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Función jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Función enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Función disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + NAVE_MEDIO_X, y + NAVE_MEDIO_Y))

# Función detectar colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 45:
        return True
    else:
        return False


#Loop del juego
se_ejecuta = True
while se_ejecuta:
    #imagen de fondo
    pantalla.blit(fondo, (0, 0))


    #Iterar eventos
    for evento in pygame.event.get():
        #Cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN and game_over == False:
            #print('Tecla presionada')
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_UP:
                jugador_y_cambio = -1
            if evento.key == pygame.K_DOWN:
                jugador_y_cambio = 1
            if evento.key == pygame.K_SPACE:
                sondio_bala = mixer.Sound('disparo.mp3')
                sondio_bala.play()
                if bala_visible:
                    nueva_bala = {
                        'x': jugador_x,
                        'y': jugador_y,
                        'velocidad': -5
                    }
                    balas.append(nueva_bala)

                if not bala_visible:
                    bala_x = jugador_x
                    bala_y = jugador_y
                    disparar_bala(bala_x, bala_y)


        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                jugador_y_cambio = 0


    #Modificar ubicación del jugador
    jugador_x += jugador_x_cambio
    jugador_y += jugador_y_cambio

    #Mantener dento de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    if jugador_y <= 0:
        jugador_y = 0
    elif jugador_y >= 536:
        jugador_y = 536

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):

    # Fin del juego por colision
        colision_game_over = hay_colision(enemigo_x[e], enemigo_y[e], jugador_x, jugador_y)
        if colision_game_over:
            texto_final()
            for k in range(cantidad_enemigos):
                enemigo_y[k] = -1000
            sonido_explosion = mixer.Sound("explosion.mp3")
            sonido_explosion.play()
            img_jugador = pygame.image.load('boom.gif')
            mi_fuente_final = fuente_final.render('GAME OVER', True, (255, 255, 255))
            pantalla.blit(mi_fuente_final, (200, 250))
            game_over = True
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # Mantener dento de los bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]
        if enemigo_y[e] >= 536:
            enemigo_y[e] = random.randint(20, 200)
            enemigo_x[e] = random.randint(0, 736)


        # Colisión
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("grito.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break


        enemigo(enemigo_x[e], enemigo_y[e], e)

    #Movimiento de la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + NAVE_MEDIO_X, bala["y"] + NAVE_MEDIO_Y))
        if bala["y"] < 0:
            balas.remove(bala)

    if bala_y <= -64:
        bala_y = jugador_y
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio



    jugador(jugador_x, jugador_y)


    mostrar_puntaje(texto_x, texto_y)


    #Actualizar
    pygame.display.update()
