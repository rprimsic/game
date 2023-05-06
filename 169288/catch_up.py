from pygame import *

#создай окно игры
window = display.set_mode((1280,720))
display.set_caption('Догонялки')

#задай фон сцены
background = transform.scale(image.load('background.png'),(1680,1050)) 
clock = time.Clock()
#создай 2 спрайта и размести их на сцене
x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load('sprite1.png'),(100,100))
sprite2 = transform.scale(image.load('sprite2.png'),(100,100))

speed = 3

run = True
while run:
    window.blit(background,(0,0))
    window.blit(sprite1,(x1,y1))
    window.blit(sprite2,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            run = False
    keysp1 = key.get_pressed()
    
    if keysp1[K_LEFT] and x1>5:
        x1-=speed
    if keysp1[K_RIGHT] and x1<1280:
        x1+=speed
    if keysp1[K_UP] and y1>5:
        y1-=speed
    if keysp1[K_DOWN] and y1<720:
        y1+=speed
    if keysp1[K_a] and x2>5:
        x2-=speed
    if keysp1[K_d] and x2<1280:
        x2+=speed
    if keysp1[K_w] and y2>5:
        y2-=speed
    if keysp1[K_s] and y2<720:
        y2+=speed    
    display.update()
    clock.tick(60)
#обработай событие «клик по кнопке "Закрыть окно"»