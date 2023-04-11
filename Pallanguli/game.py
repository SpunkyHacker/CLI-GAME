import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 1700,600
FPS = 60

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pallanguli')

class Player:
    def __init__(self,name):
        self.name = name

class Kuli:
    def __init__(self, x, y, kasi=False):
        self.x = x
        self.y = y
        self.kasi = kasi

def draw():
    win.fill(BLACK)
    pygame.draw.circle(win, WHITE, (210,150), 70, 1)
    pygame.draw.circle(win, WHITE, (420,150), 70, 1)
    pygame.draw.circle(win, WHITE, (630,150), 70, 1)
    pygame.draw.circle(win, WHITE, (840,150), 70, 1)
    pygame.draw.circle(win, WHITE, (1050,150), 70, 1)
    pygame.draw.circle(win, WHITE, (1260,150), 70, 1)
    pygame.draw.circle(win, WHITE, (1470,150), 70, 1)

    pygame.draw.circle(win, WHITE, (210,400), 70, 1)
    pygame.draw.circle(win, WHITE, (420,400), 70, 1)
    pygame.draw.circle(win, WHITE, (630,400), 70, 1)
    pygame.draw.circle(win, WHITE, (840,400), 70, 1)
    pygame.draw.circle(win, WHITE, (1050,400), 70, 1)
    pygame.draw.circle(win, WHITE, (1260,400), 70, 1)
    pygame.draw.circle(win, WHITE, (1470,400), 70, 1)



    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    

    Running = True
    while Running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
                pygame.quit()


        draw()
        


if __name__ == '__main__':
    main()