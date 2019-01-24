import pygame, math
" dast garmi bood hich cari nakardam"
class draw():
    def __init__(self):
        self.xt=400
        self.yt=300
        self.xd=10
        self.yd=10
        self.tool=1200
        self.arz=800
    def kadr(self):
        a=self.tool
        b=self.arz
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (20, b-20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (20, b-20), 7)
    def toop(self):
        pygame.draw.circle(disp, (255, 0, 0), (self.xt, self.yt), 25)
    def toop_mov(self):
        xt=self.xt
        yt=self.yt
        if xt>=self.tool or xt<=20:
            self.xd=-self.xd
        if yt>=self.arz or yt<20:
            self.yd=-self.yd
        self.xt+=self.xd
        self.yt+=self.yd
pygame.init()
disp=pygame.display.set_mode((1200, 800))
done=False
pen=draw()
gtank=pygame.image.load("green tank.png")
rtank=pygame.image.load("red tank.png")

while not done:
    #event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    #update
    #draw
    disp.fill((41, 68, 190))
    pen.kadr()
    disp.blit(rtank, (500, 500))
    pygame.time.Clock().tick(30)
    pygame.display.update()
pygame.quit()
