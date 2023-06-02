from pygame import *
from random import randint
from time import time as timer

wind = display.set_mode((700,500))
display.set_caption('Пинг-Пон')
background = transform.scale(image.load('fon.jpg'),(700,500))

font.init()
font = font.SysFont('Arial',30)
win = font.render('YOU WIN!',True,(0, 255, 0))
lose = font.render('YOU LOSE!',True,(255, 0, 0))


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,wight,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        wind.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_p(self):
        keys_p = key.get_pressed()
        if keys_p[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
    def update_p(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < win_height - 80:
            self.rect.x += self.speed


ball = GameSprite('ball.png',10,450,420)
play1 = Player('raketka.png',10,450,420)
play2 = Player('raketka.png',10,450,420)

game = True
finish = False
    speed_x = 3
    speed_y = 3

    while game:
        for i in event.get():
            if i.type == QUIT:
                
        if finish != True:
            ball.rect.x += speed_x
            ball.rect.x += speed_y

        if ball.rect.

        if ball.rect.x < 0
        finish = True
clock = time.Clock()
FPS = 60
finish = False
rel_time = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:   
            if i.key == K_SPACE:
                if num_fire < 15:
                    hero.fire()
                    fire.play()
                    num_fire += 1
                if num_fire >= 15:
                    rel_time = True
                    w = timer()

    if not finish:
        text_lose = font.render('Пропущено: '+str(lost), True,(255,255,255))
        count = font.render('Счёт: '+str(ezz), True,(255,255,255))
        wind.blit(background,(0,0))
        per = font.render('Перезарядка',True,(255,255,255))
        wind.blit(count,(10,35))
        wind.blit(text_lose,(10,10))

        hero.update()
        monst.update()
        hero.reset()
        buls.update()
        monst.draw(wind)
        buls.draw(wind)
        asts.update()
        asts.draw(wind)

        if rel_time == True:
            t = timer()
            if t - w <= 3:
                wind.blit(per,(300,450))
            else:
                num_fire = 0
                rel_time = False

        death = sprite.groupcollide(monst,buls,True,True)
        if sprite.spritecollide(hero,monst,False) or lost > 4:
            finish = True
            wind.blit(lose,(325,200))
        for e in death:
            ezz += 1
            ufo1 = Enemy('ufo.png',3,randint(10,570),0)
            monst.add(ufo1)
        if ezz == 10:
            finish = True
            wind.blit(win,(325,200))

    display.update()
    clock.tick(FPS)


        