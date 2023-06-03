from pygame import *

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
    def update_r(self):
        keys_p = key.get_pressed()
        if keys_p[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys_p = key.get_pressed()
        if keys_p[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_p[K_s] and self.rect.y < win_height - 80:
            self.rect.x += self.speed


ball = GameSprite('ball.png',150,20,0,65,65)
play1 = Player('raketka.png',5,10,15,20,100)
play2 = Player('raketka.png',975,350,15,20,100)

game = True
finish = False
speed_x = 3
speed_y = 3
font.init()
font=font.Font(None,66)
lose1=font.render("Проиграл левый игрок")
lose2=font.render("Проиграл правый игрок")
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if not finish:
        win.fill((123,54,33))
        ball.reset()
        play1.reset()
        play2.reset()
        play1.update_r()
        play2.update_l()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 500 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(play1,ball) or sprite.collide_rect(play2,ball):
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        win.blit(lose1,(400,200))

    if ball.rect.x > 1000:
        finish = True
        win.blit(lose2,(400,200))

    display.update()
    clock.tick(60)