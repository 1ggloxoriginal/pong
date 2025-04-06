#Создай собственный Шутер!

from pygame import *
from random import choice

window = display.set_mode((700,500))
display.set_caption('пинг-понг')
background = transform.scale(image.load('maxresdefault.jpg'),(700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Player1(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 450 - 10 - self.rect.width:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 450 - 10 - self.rect.width:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.direct = [0,0]
    
    def update(self):
        self.rect.x += self.speed * self.direct[0]
        self.rect.y += self.speed * self.direct[1]
        if self.rect.y <= 0 or self.rect.y >= 500 - self.rect.height:
            self.direct[1] *= -1

    def start(self):
        self.rect.x = 325
        self.rect.y = 225

hero1 = Player1('i-Photoroom.png', 0, 250, 68, 100, 15)
hero2 = Player2('i-Photoroom.png', 650, 250, 68, 100, 15)

ball = Ball('perl-Photoroom.png', 350-25, 250-25, 50, 50, 5)
ball.direct = [choice([-1, 1]), choice([-1, 1])]

mixer.init()
mixer.music.load('musicmine.mp3')
mixer.music.play()



game = True

clock = time.Clock()
fps = 60
while game:  
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    hero1.update_l()
    hero1.reset()

    hero2.update_r()
    hero2.reset()

    ball.update()
    ball.reset()
    
    clock.tick(fps)
    display.update()        