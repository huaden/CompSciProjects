import pygame as pg, sys
import pygame.display
from pygame.locals import*
import time
import random


sCount = 0


class Rock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("images/Rock.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vx = 1
        self.vy = 1

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def render(self, display):
        display.blit(self.image, self.rect)
    
    def updateRock(self, rock):
        if self.rect.colliderect(rock.rect):
            print("We have Collided with a Rock")
            return 0
    def updatePaper(self, paper):
        if self.rect.colliderect(paper.rect):
            print("We have Collided with a Paper")
            self.kill()
            return -1
        
    def updateScissor(self, scissor):
        if self.rect.colliderect(scissor.rect):
            print("We have Collided with a Scissor")
            scissor.kill()
            return 1

    

class Paper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("images/Paper.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.vx = 1
        self.vy = 1

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def render(self, display):
        display.blit(self.image, self.rect)

    def updateRock(self, rock):
        if self.rect.colliderect(rock.rect):
            print("We have Collided with a Rock")
            rock.kill()
            return 1
    def updatePaper(self, paper):
        if self.rect.colliderect(paper.rect):
            print("We have Collided with a Paper")
            return 0
        
    def updateScissor(self, scissor):
        if self.rect.colliderect(scissor.rect):
            print("We have Collided with a Scissor")
            self.kill()
            return -1


class Scissors(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pg.image.load("images/Scissors.png")
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.vx = 1
        self.vy = 1

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy        

    def render(self, display):
        display.blit(self.image, self.rect)

    def updateRock(self, rock):
        if self.rect.colliderect(rock.rect):
            print("We have Collided with a Rock")
            self.kill()
            return -1
    def updatePaper(self, paper):
        if self.rect.colliderect(paper.rect):
            print("We have Collided with a Paper")
            paper.kill()
            return 1
        
    def updateScissor(self, scissor):
        if self.rect.colliderect(scissor.rect):
            print("We have Collided with a Scissor")
            return 1
        



sGroup = pygame.sprite.Group()
rGroup = pygame.sprite.Group()
pGroup = pygame.sprite.Group()


game_state = "start_menu"

winner = "NONE"
width = 800
height = 1000
white = (255,255,255)
black = (10, 10, 10)
rockWin = 0
paperWin = 0
scissorWin = 0

betNum = 0
confirm = False

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Rock v Paper v Scissors")

r_img = pg.image.load("images/Rock.png")
p_img = pg.image.load("images/Paper.png")
s_img = pg.image.load("images/Scissors.png")

r_img = pg.transform.scale(r_img, (10, 10))
p_img = pg.transform.scale(p_img, (10, 10))
s_img = pg.transform.scale(s_img, (10, 10))

img_height = 50
img_width = 50


sWin = 0
pWin = 0
rWin = 0

numObj = 10

borders = []

topBorder = pygame.Rect(0,0,width, 1)
bottomeBorder = pygame.Rect(0,width-1,width, 1)

def game_opening():
    screen.fill(black)
    draw_rpsImages(numObj)
    renderObj

def renderObj():
    for r in rGroup:
        r.render(screen)
    for p in pGroup:
        p.render(screen)
    for s in sGroup:
        s.render(screen)

def updateObj():
    for r in rGroup:
        r.update()
        r.render(screen)
    for p in pGroup:
        p.update()
        p.render(screen)
    for s in sGroup:
        s.update()
        s.render(screen)


def draw_rpsImages(count):
    for i in range(3):
        for q in range(count):
            good = True
            if(i == 0):
                while(good):
                    x = random.randint(0, width-img_width)
                    y = random.randint(0, height-img_height)
                    rock = Rock(x,y)
                    good = checkCollision(rock.rect, rGroup, pGroup, sGroup)
                    if not good:
                        rGroup.add(rock)
                


            if(i == 1):
                while(good):
                    x = random.randint(0, width-img_width)
                    y = random.randint(0, height-img_height)
                    paper = Paper(x,y)
                    good = checkCollision(paper.rect, rGroup, pGroup, sGroup)
                    if not good:
                        pGroup.add(paper)
            
            if(i == 2):
                while(good):
                    x = random.randint(0, width-img_width)
                    y = random.randint(0, height-img_height)
                    scissor = Scissors(x,y)
                    good = checkCollision(scissor.rect, rGroup, pGroup, sGroup)
                    if not good:
                        sGroup.add(scissor)



def checkCollision(rect, r_rects, p_rects, s_rects):
    for r in r_rects:
        if rect.colliderect(r):
            return True
    for p in p_rects:
        if rect.colliderect(p):
            return True
    for s in s_rects:
        if rect.colliderect(s):
            return True
    return False
    
count = 0

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    if count == 0:
        game_opening()
    else:
        updateObj()
    
    count += 1

    pygame.display.update()





