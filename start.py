import pygame 
pygame.init()
window = pygame.display.set_mode([500,500])
pygame.display.set_caption("First Programme")
x = 0
y = 0
red=(200,0,0)
blue = (0,0,200)
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(60)
    pass
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    window.fill(red)
    pygame.draw.rect(window,blue,[x,y,50,50])
    # if x<=450 and y<=450:
    #     x+=1
    # elif y<=450 and x>=450:
    #     y+=1
    # elif y>50 and x<50:
    #     y-=1
    # elif y>450:
    #     x-=1

    if y<=50 and x<=450:
        x+=1
    if x>450:
        y+=1
    if y>450:
        x-=1
    if x<50 and y>50:
        y-=1
    pygame.display.update()