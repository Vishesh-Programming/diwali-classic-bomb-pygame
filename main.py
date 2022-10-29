import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Code Olympics")

# fonts
font = pygame.font.SysFont("Times New Roman", 10)
bigFont = pygame.font.SysFont("Times New Roman", 40)

# variables for colors
red = (200, 14, 14, 0.2)
blue = (0, 0, 200)
green = (144, 238, 144)
black = (0, 0, 0)

# Text to display
winningText = font.render(
    "Congratulations! You made it out safely. Have a safe and happy diwali.",
    False, black)
losingText = font.render(
    "You were too close to cracker. Please maintain proper distance when using crackers.",
    False, black)
runText = bigFont.render("Run Run ....", False, red)
restartGame = font.render("Press R to restart the game", False, black)
nextLevel = font.render("Press N to start new Level.. ( you will have only 2 seconds to run )", False, black)
firstLevel = bigFont.render("Level : 1" , False , black)
secondLevel = bigFont.render("Level : 2" , False , black)

# images
boy = pygame.image.load("boy.png")
boy = pygame.transform.scale(boy, (100, 100))

tntImage = pygame.image.load("tnt.png")
tntImage = pygame.transform.scale(tntImage, (100, 100))

explosion = pygame.image.load("explosion.png")
explosion = pygame.transform.scale(explosion, (100, 100))

# global variables
level = 1

class Player:

    def __init__(self, x, y):
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
        window.blit(self.player, (self.x, self.y))

    def restart(self):
        self.x = 400
        self.y = 400


player = Player(400, 400)


class TNT:

    def __init__(self, x, y):
        self.tnt = tntImage
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
        window.blit(self.tnt, (self.x, self.y))

    def initiate_explosion(self):
        self.explosion_initiated = True

    def doExplosion(self):
        self.tnt = explosion
        self.explosion = True
        player.freeze = True

    def normalState(self):
        self.tnt = tntImage


tnt = TNT(100, 350)
tntCountDown = 180

clock = pygame.time.Clock()

run = True

# game loop
while run:
    clock.tick(60)
    window.fill(green)
    pygame.draw.rect(window, red, pygame.Rect(0, 250, 300, 300), 5)
    player.display()
    tnt.display()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and player.freeze == False:
                player.move_forward()
            if event.key == pygame.K_d and player.freeze == False:
                player.move_backward()
            if event.key == pygame.K_w and player.freeze == False:
                player.move_up()
            if event.key == pygame.K_s and player.freeze == False:
                player.move_down()
            if event.key == pygame.K_r:
                player.restart()
                tnt.normalState()
                tnt.explosion = False
                player.freeze = False
                if level == 1 :
                    tntCountDown = 180
                elif level == 2 :
                    tntCountDown = 120 
                else :
                    pass

            if event.key == pygame.K_n:
                player.restart()
                tnt.normalState()
                tnt.explosion = False
                player.freeze = False
                tntCountDown = 120
                level += 1
                

        # condition to burn tnt
        if abs(player.x - tnt.center_x) <= 20 and abs(player.y -
                                                      tnt.center_y) <= 20:
            tnt.initiate_explosion()

    if tnt.explosion_initiated == True:
        window.blit(runText, (20, 50))
        tntCountDown -= 1
        if tntCountDown < 0:
            tnt.doExplosion()
            tnt.explosion_initiated = False

    if tnt.explosion == True:
        if player.x > 300 or player.y < 250:
            pass  # display winning
            window.blit(winningText, (20, 100))
            window.blit(nextLevel, (20, 200))

        else:
            pass  # display loss
            window.blit(losingText, (20, 100))

        window.blit(restartGame, (20, 150))

    if level == 1:
        window.blit(firstLevel , (300 , 10))

    else :
        window.blit(secondLevel , ( 300 , 10))
        
    pygame.display.update()