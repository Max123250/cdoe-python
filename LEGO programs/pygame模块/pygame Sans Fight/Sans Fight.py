import pygame
class Game():
    def __init__(self):
        self.k_up_down = False
        self.k_down_down = False
        self.k_left_down = False
        self.k_right_down = False
        self.run = True

    def init(self):
        pygame.init()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.k_up_down = True
                elif event.key == pygame.K_DOWN:
                    self.k_down_down = True
                elif event.key == pygame.K_LEFT:
                    self.k_left_down = True
                elif event.key == pygame.K_RIGHT:
                    self.k_right_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.k_up_down = False
                elif event.key == pygame.K_DOWN:
                    self.k_down_down = False
                elif event.key == pygame.K_LEFT:
                    self.k_left_down = False
                elif event.key == pygame.K_RIGHT:
                    self.k_right_down = False

    def flip(self):
        pygame.display.flip()

    def delay(self,time):
        pygame.time.delay(time)


class Button():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.images = None
        self.image = None

    def blit(self):
        s.blit(self.image,[self.x,self.y])


class Sans():
    def __init__(self):
        self.x = 257
        self.y = 10
        self.image = pygame.image.load("image/sans.png")

    def blit(self):
        s.blit(self.image,[self.x,self.y])


class FightButton(Button):
    def __init__(self):
        self.x = 40
        self.y = 418
        self.image = pygame.image.load("image/fight.png")

class ActButton(Button):
    def __init__(self):
        self.x = 190
        self.y = 418
        self.image = pygame.image.load("image/act.png")

class ItemButton(Button):
    def __init__(self):
        self.x = 340
        self.y = 418
        self.image = pygame.image.load("image/item.png")

class MercyButton(Button):
    def __init__(self):
        self.x = 490
        self.y = 418
        self.image = pygame.image.load("image/mercy.png")


class Name():
    def __init__(self):
        self.x = 40
        self.y = 388
        self.image = pygame.image.load("image/name.png")

    def blit(self):
        s.blit(self.image,[self.x,self.y])


game = Game()
sans = Sans()
fight = FightButton()
act = ActButton()
item = ItemButton()
mercy = MercyButton()
name = Name()

game.init()
s = pygame.display.set_mode([640,480])
s.fill([0,0,0])
pygame.display.set_caption("Sans Fight")

while game.run:
    game.check_event()
    game.flip()

    sans.blit()

    fight.blit()
    act.blit()
    item.blit()
    mercy.blit()
    name.blit()

    game.delay(10)
pygame.quit()