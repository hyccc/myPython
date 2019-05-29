# project: flapbird
# author: Ethan
# time: 2019/5/28
# conf：utf-8
import random

import pygame
from pygame.locals import *

bird_width, bird_height = 32, 32
pipe_list = []


class Bird():
    def __init__(self, screen):
        self.screen = screen
        self.x = 100
        self.y = 200
        self.image = pygame.image.load('./images/bird_wing_up.png')
        self.jump = False
        self.jump_height = 30
        self.gravity = 10

    def fly(self):                        # 为什么飞起来这么卡??  如何去优化
        if self.jump is True:
            self.y -= self.jump_height
            self.jump_height -= 1
        else:
            self.gravity += 0.5
            self.y += self.gravity

    def crash(self):
        pass

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


# pipe_body, pipe_end = 80*32
class Pipe():
    def __init__(self, screen):
        self.screen = screen
        self.pipe_body = pygame.image.load('./images/pipe_body.png')
        self.pipe_end = pygame.image.load('./images/pipe_end.png')

        self.pipe_gap = 150
        self.x = 570  # 570
        self.random_y = random.randint(100, 400)   # 底部管道的最高点
        self.bottom_y = self.random_y
        self.top_y = self.random_y - self.pipe_gap    # 顶部管道最低点

        self.pipe_list = []

    def move(self):
        self.x -= 5

    def display(self):
        self.screen.blit(self.pipe_end, (self.x, self.bottom_y))
        for i in range(self.bottom_y+32, 512):
            self.screen.blit(self.pipe_body, (self.x, i))
            if i > 512:
                break

        self.screen.blit(self.pipe_end, (self.x, self.top_y))
        for i in range(1, self.top_y):
            self.screen.blit(self.pipe_body, (self.x, i))
            if i > self.top_y-32:
                break


class Wall():
    pass


def key_control(bird):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYUP:
            if event.key == K_SPACE:
                print('jump')
                bird.jump = True
                bird.jump_height = 50
                bird.gravity = 5
                bird.fly()
                bird.jump = False

        else:
            bird.fly()
            print('fall')


def main():
    pygame.display.init()

    pygame.display.set_caption("flapy bird")
    screen = pygame.display.set_mode((284*2, 512), 0, 32)
    background = pygame.image.load('./images/background.png')

    bird = Bird(screen)

    clock = pygame.time.Clock()

    while True:
        clock.tick(30)

        screen.blit(background, (0, 0))
        screen.blit(background, (284, 0))

        # 创建pipe
        if not pipe_list:
            pipe_list.append(Pipe(screen))
        else:
            for pipe in pipe_list:
                if pipe.x == 200:
                    pipe_list.append(Pipe(screen))
                pipe.move()
                pipe.display()

        bird.display()





        pygame.display.update()
        key_control(bird)

if __name__ == '__main__':
    main()
