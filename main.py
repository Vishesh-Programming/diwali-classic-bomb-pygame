import pygame

pygame.init()

window = pygame.display.set_mode([500,500])

pygame.display.set_caption("Code Olympics")

# images 
boy = pygame.image.load("boy.png")
boy = pygame.transform.scale(boy,(100,100))

tnt = pygame.image.load("tnt.png")
tnt = pygame.transform.scale(tnt,(100,100))

explosion = pygame.image.load("explosion.png")
explosion = pygame.transform.scale(explosion,(100,100))

# global variables

class Player:
    def __init__(self , x ,  y):
        self.player = boy
        self.x = x
        self.y = y
        self.center_x = self.x - 10
        self.center_y = self.y + 25

    def move_forward(self):
        self.x -= 10    

    def move_backward(self):
        self.x += 10

    def move_up(self):
        self.y -= 10        
      
    def move_down(self):
        self.y += 10

    def display(self):
            window.blit(self.player , (self.x,self.y))

player = Player(400,400)


class TNT:
    def __init__(self , x ,  y):
        self.tnt = tnt
        self.x = x
        self.y = y
        self.center_x = self.x + 50
        self.center_y = self.y + 50

    def move_forward(self):
        self.x -= 10   
        self.center_x -= 10

    def move_backward(self):
        self.x += 10
        self.center_x += 10

    def move_up(self):
        self.y -= 10    
        self.center_y -= 10
      
    def move_down(self):
        self.y += 10
        self.center_y += 10

    def display(self):
        window.blit(self.tnt , (self.x,self.y))

    def explosion(self):
        self.tnt = explosion
        
tnt = TNT(100,350)
        
# colors
red=(200,0,0)
blue = (0,0,200)

clock = pygame.time.Clock()

run = True

# game loop
while run:
    clock.tick(60)
    window.fill(red)
    player.display()
    tnt.display()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_forward()
            if event.key == pygame.K_d:
                player.move_backward()
            if event.key == pygame.K_w:
                player.move_up()
            if event.key == pygame.K_s:
                player.move_down()

        # condition to burn tnt
        print("player x" , player.x)
        print("tnt x" , tnt.x) 
        print("-")
        print(abs(player.center_x - tnt.center_x))
        print(abs( player.center_y - tnt.center_y))
        print("-")
        if abs(player.x - tnt.center_x) <= 20 and abs( player.y - tnt.center_y) <= 20 :
            print("In range")
            tnt.explosion()
        
    pygame.display.update()