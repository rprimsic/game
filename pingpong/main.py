import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image,x,y,speed,width,height):

        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image),(width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[pygame.K_DOWN] and self.rect.y<win_height-80:
            self.rect.y+=self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[pygame.K_s] and self.rect.y<win_height-80:
            self.rect.y+=self.speed

bg = (200,255,255)
win_width = 800
win_height = 600
fps = 60
window = pygame.display.set_mode((win_width,win_height))
window.fill(bg)

game = True
finish = False
clock = pygame.time.Clock()
clock.tick(fps)

racket1 = Player('ball.png',30,200,15,50,150)
racket2 = Player('ball.png',700,200,15,50,150)
ball = GameSprite('ball.png',400,300,5,50,50)

pygame.font.init()
font = pygame.font.Font(None,35)

lose1 = font.render('левый слил', True, (180,0,0))
lose2 = font.render('правый слил', True, (180,0,0))
speed_x = 2
speed_y = 1

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    if not finish:
        window.fill((0,0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y +=speed_y
        if pygame.sprite.collide_rect(racket1,ball) or pygame.sprite.collide_rect(racket2,ball):
            speed_x *= -1.1
            speed_y*=-1.1
        if ball.rect.y<0 or ball.rect.y>win_height-80:
            speed_y *=-1
        if ball.rect.x>win_width:
            finish = True
            window.blit(lose2, (win_width/2,win_height/2))
            game = False
        if ball.rect.x<0:
            finish = True
            window.blit(lose1, (win_width/2,win_height/2))
            game = False
        racket1.reset()
        racket2.reset()
        ball.reset()
        pygame.display.update()
        clock.tick(fps)