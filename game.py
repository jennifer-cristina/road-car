# Pygame: Biblioteca python que cria interfaces gráficas para jogos de maneira simples.
from tkinter import font
import pygame
from random import randint
pygame.init()

# Eixos
x = 340 # max 460 - min 210
y = 100
position_x = 180
position_y = 800
position_y_a = 800
position_y_c = 800
timer = 0
second_time = 0

# Velocidades dos carros
velocity = 10
velocity_others = 12

# Carregando as imagens
background = pygame.image.load('road.png')
car = pygame.image.load('car-oficial.png')
police = pygame.image.load('police.png')
ambulance = pygame.image.load('ambulance.png')
taxi = pygame.image.load('taxi.png')

# Criando e Formatando o texto
font = pygame.font.SysFont('arial black', 30)
text = font.render("Time: ", True,(0,0,0))
position_text = text.get_rect()
position_text.center = (65,50)

# Definindo as dimensões da janela
window = pygame.display.set_mode((800,600))
# Definindo o nome da janela
pygame.display.set_caption("Criando um jogo com Python")

# Criando um looping para que a janela possa ser aberta e rodar o jogo
open_window = True
while open_window :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open_window = False

    # Variavel que recebe o metodo para ao clicar em alguma tela receber alguma ação
    commands = pygame.key.get_pressed()

    if commands[pygame.K_RIGHT] and x <= 460:
            x+= velocity
    if commands[pygame.K_LEFT] and x  >= 210:
            x-= velocity
 
    # Detectando a colisão
    # Colisão do lado direito
    if ((x + 80 > position_x and y + 180 > position_y)) :
        y = 1200

    # Colisão do lado esquerdo
   # if ((x - 80 < position_x - 150 and y + 180 > position_y_a)) :
   #     y = 1200

    # Colisão central
   # if ((x + 80 > position_x - 136 and y + 180 > position_y_c)) and ((x - 80 < position_x - 136 and y + 180 > position_y_c)):
   #     y = 1200

    # Condição para fazer a movimentação do carro ao sair da tela e voltar 
    # policia
    if (position_y <= -80) :
        position_y = randint(800, 1000)

    # ambulancia
    if ((position_y_a <= -80)) :
        position_y_a =  randint(1300, 2000)

    # taxi
    if ((position_y_c <= -80)) :
        position_y_c =  randint(2300, 3000)

    # Criando o tempo de duração do jogo
    if (timer < 20) :
        timer += 1
    else :
        second_time += 1
        text = font.render("Time: "+str(second_time), True,(0,0,0))
        timer = 0

    # Velocidade dos demais carros
    position_y -= velocity_others
    position_y_a -= velocity_others + 2
    position_y_c -= velocity_others + 10  # taxi

# Colocando a imagem de fundo (estrada)
    window.blit(background, (0,0))
# Colocando o carro na tela
    window.blit(car, (x,y))
# Colocando o carro da policia na tela
    window.blit(police, (position_x, position_y))
# Colocando o carro da ambulancia na tela
    window.blit(ambulance, (position_x + 300, position_y_a))
# Colocando o carro de taxi na tela
    window.blit(taxi, (position_x + 150, position_y_c))
# Colocando o texto na tela
    window.blit(text, position_text)


# Atualizando a janela
    pygame.display.update()

# fechando a janela
pygame.quit()


