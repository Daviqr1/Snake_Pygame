import pygame
import sys
import random
import os



#iniciando o pygame

pygame.init()


class Cobra:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 255, 0)  # Cor verde
        self.direction = 'right'
        self.speed = 20
        self.body = [[x, y]]
        self.score = 0
        self.game_over = False

    def move(self):
        if self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed

        # Atualiza a posição da cabeça da cobra
        self.body.insert(0, [self.x, self.y])

    def grow(self):
        # Adiciona um segmento à cobra quando ela come
        self.score += 1

    def check_collision(self, screen_width, screen_height):
        # Verifica colisões com as bordas da tela
        if self.x < 0 or self.x >= screen_width or self.y < 0 or self.y >= screen_height:
            self.game_over = True

    def check_self_collision(self):
        # Verifica colisões com o próprio corpo
        for segment in self.body[1:]:
            if self.x == segment[0] and self.y == segment[1]:
                self.game_over = True

    def change_direction(self, new_direction):
        # Altera a direção da cobra
        if new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], self.size, self.size))
class Comida: 
    def __init__(self, screen_width, screen_height, size):
        self.size = size
        self.color = (255, 0, 0)  # Vermelho
        self.x = random.randint(0, (screen_width - size) // size) * size
        self.y = random.randint(0, (screen_height - size) // size) * size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def randomize_position(self, screen_width, screen_height):
        self.x = random.randint(0, (screen_width - self.size) // self.size) * self.size
        self.y = random.randint(0, (screen_height - self.size) // self.size) * self.size
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)


x = 200
y = 200
color = (0, 255, 0)  # Cor verde
size = 20
direction = 'right'
speed = 20
body = [[x, y]]

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')



def main():
    cobra = Cobra(x,y,color, size)
    comida = Comida(screen_width, screen_height, size)
    while not cobra.game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            cobra.direction = 'right'

        elif keys[pygame.K_LEFT]:
            cobra.direction = 'left'
        
        elif keys[pygame.K_UP]:
            cobra.direction = 'up'
        
        elif keys[pygame.K_DOWN]:
            cobra.direction = 'down'

        cobra.move()   


        #logica do jogo

        cobra.move()
        cobra.check_collision(screen_width, screen_height) 
        comida.check_collision(screen_width, screen_height) 
        if comida.eat(comida):
            comida.randomize_position(screen_width, screen_height)


        #limpando a tela e desenhando novamente


        screen.fill((0, 0, 0))
        cobra.draw(screen) 
        comida.draw(screen)
        pygame.display.update()

        #taxa de fps do jogo
        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    main()




