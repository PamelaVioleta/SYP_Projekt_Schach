import pygame
pygame.init()

win = pygame.display.set_mode((600,600))

pygame.display.set_caption("First Game")

x = 200
y = 200
radio = 15
vel =20

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel 
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill((0,0,0))
    pygame.draw.circle(win,(255,182,193),(x,y),radio)
    pygame.display.update()
            
pygame.quit()

