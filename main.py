import pygame

pygame.init()

window = pygame.display.set_mode([500,500])

pygame.display.set_caption("Code Olympics")

font = pygame.font.SysFont("Times New Roman",10)
bigFont = pygame.font.SysFont("Times New Roman" , 40)

# colors
red=(200,14,14,0.2)
blue = (0,0,200)
green = (144,238,144)
black = (0,0,0)

winningText = font.render("Congratulations! You made it out safely. Have a safe and happy diwali.",False, black)
losingText = font.render("You were too close to cracker. Please maintain proper distance when using crackers.",False, black)
runText = bigFont.render("Run Run ....",False, red)
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
        self.freeze = False

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
        self.explosion_initiated = False
        self.explosion = False

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

    def initiate_explosion(self):
        self.explosion_initiated = True

    def doExplosion(self):
        self.tnt = explosion
        self.explosion = True
        player.freeze = True
        
        
tnt = TNT(100,350)
tntCountDown = 180
    

clock = pygame.time.Clock()

run = True

# game loop
while run:
    clock.tick(60)
    window.fill(green)
    pygame.draw.rect(window,red,pygame.Rect(0,250,300,300),5)
    player.display()
    tnt.display()
  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if player.freeze == False :
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
        if abs(player.x - tnt.center_x) <= 20 and abs( player.y - tnt.center_y) <= 20 :
            print("In range")
            tnt.initiate_explosion()
            

    if tnt.explosion_initiated == True :
        window.blit(runText , (20 , 50))
        tntCountDown -= 1 
        if tntCountDown < 0 :
            tnt.doExplosion()

    if tnt.explosion == True :
        if player.x > 300 or player.y < 250 :
            pass  # display winning 
            window.blit(winningText,(20,100))

        else :
            pass # display loss
            window.blit(losingText, (20,100))
        
    pygame.display.update()