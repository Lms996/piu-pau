from pygame import *
win_x = 700
win_y = 500
window = display.set_mode((win_x,win_y))
background = transform.scale(image.load('backgroud.jpg'),(win_x,win_y))
clock = time.Clock()
game = True
display.set_caption('пиу пиу тыщ тыщ')

#Персонажи
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,weight,height,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
        

class Ball(GameSprite):
    def __init__(self,player_image,player_x,player_y,weight,height,player_speed):
        super().__init__(player_image,player_x,player_y,weight,height,player_speed)
        self.speedx = self.speed
        self.speedy = self.speed
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if sprite.collide_rect(player1, self) or sprite.collide_rect(player2, self):
            self.speedx *= -1           

        if self.rect.y <= 0 or self.rect.y >= 445:
            self.speedy *= -1

            



class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
score = 0

player1 = Player('platform.png',50,200,30,100,5)

player2 = Player('platform.png',600,200,30,100,5)

ball = Ball('shaiba.png',325,225,50,50,3)

font.init()

font1 = font.SysFont('arial',20)
font2 = font.SysFont('arial',40)

score1 = 0
score2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            

    window.blit(background,(0,0))
    window.blit(font1.render('Счет слева ' + str(score1),1,(255,0,0)),(30,37))
    window.blit(font1.render('Счет справа ' + str(score2),1,(255,0,0)),(530,37))       
    player1.reset()
    player2.reset()
    ball.reset()
    player1.update1()
    player2.update2()
    ball.update()

    if ball.rect.x >= 650:
        score1 += 1
        ball.rect.x = 325
        ball.rect.y = 225
        ball.speedx *= -1

    if ball.rect.x <= 0:
        score2 += 1
        ball.rect.x = 325
        ball.rect.y = 225
        ball.speedx *= -1

    if score2 >= 5:
        window.blit(font2.render('Выиграл игрок справа!',1,(0,255,255)),(200,225))
        ball.speedx = 0
        ball.speedy = 0
    if score1 >= 5:
        window.blit(font2.render('Выиграл игрок слева!',1,(0,225,255)),(200,225))
        ball.speedx = 0
        ball.speedy = 0

    display.update()
    time.delay(20)