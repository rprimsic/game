#создай игру "Лабиринт"!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,image_p,px,py,pspeed):
        super().__init__()
        self.image = transform.scale(image.load(image_p),(65,65))
        self.speed = pspeed
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
    
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x>5:
            self.rect.x-=self.speed

        if keys[K_d] and self.rect.x<win_w-80:
            self.rect.x+=self.speed

        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed

        if keys[K_s] and self.rect.y<win_h-80:
            self.rect.y+=self.speed

class Enemy(GameSprite):
    naprav = 'left'
    def update(self):
        if self.rect.x<= win_w -200:
            self.naprav = 'right'
        if self.rect.x>= win_w - 85:
            self.naprav = 'left'

        if self.naprav == 'left':
            self.rect.x-=self.speed
        if self.naprav == 'right':
            self.rect.x+=self.speed

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wallx,wally,wall_w,wall_h):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width,self.height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally
        
        
        
        
    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
win_w = 700
win_h = 500
window = display.set_mode((win_w,win_h))       
display.set_caption('Mazelov')
background = transform.scale(image.load('background.jpg'),(win_w,win_h))

player = Player('hero.png',5,win_h-80,3)
enemy = Enemy('cyborg.png',win_w-80,300,3)
treasure = GameSprite('treasure.png', win_w-80, win_h-80,0)
w1 = Wall(23,0,234,0,20,win_w,10)
w2 = Wall(23,0,234,200,20,10,400)
w3 = Wall(23,0,234,300,win_h-300,10,350)
w5 = Wall(23,0,234,300,20,10,100)
w4 = Wall(23,0,234,400,20,10,400)

w7 = Wall(23,0,234,600,20,10,150)
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
clock = time.Clock()
font.init()
font = font.Font(None,70)
win = font.render('ты затащил',True,(255,255,0))
lose = font.render('ты не затащил',True,(255,255,0))
game = True
kick = mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    player.reset()
    enemy.reset()
    treasure.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    
    w7.draw_wall()
    if game:
        player.update()
        enemy.update()
    if sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5)  or sprite.collide_rect(player,w7) or sprite.collide_rect(player,enemy) :
        game = False
        window.blit(lose,(200,200))
        kick.play()
    if sprite.collide_rect(player,treasure):
        game = False
        window.blit(win,(200,200))
    display.update()
    clock.tick(60)
    