import pygame, math
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
        pygame.draw.line(disp, (0,import pygame, random
from math import *
" dast garmi bood hich cari nakardam"
class draw():
    def __init__(self):
        self.tool=1200
        self.arz=800
    def kadr(self):
        a=self.tool
        b=self.arz
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (20, b-20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (20, b-20), 7)
class tank():
    def __init__(self):
        self.x=random.randint(200,1000)
        self.y=random.randint(100,500)
        self.angle=0
    t=0
    def rt(self):
        self.angle-=10
        self.t=pygame.image.load("red tank.png")
        self.t=pygame.transform.rotate(self.t, self.angle)
    def lt(self):
        self.angle+=10
        self.t=pygame.image.load("red tank.png")
        self.t=pygame.transform.rotate(self.t, self.angle)        
    def fd(self):
        
        self.y-=20*cos(radians(self.angle))
        self.x-=20*sin(radians(self.angle))
    def bd(self):
        self.y+=10*cos(radians(self.angle))
        self.x+=10*sin(radians(self.angle))
pygame.init()
disp=pygame.display.set_mode((1200, 800))
done=False
pen=draw()
gtank=tank()
rtank=tank()
gtank.t=pygame.image.load("green tank.png")
rtank.t=pygame.image.load("red tank.png")
rfd=False
rrt=False
rlt=False
rbd=False
while not done:
    #event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                rfd=True
            if event.key==pygame.K_RIGHT:
                rrt=True
            if event.key==pygame.K_LEFT:
                rlt=True
            if event.key==pygame.K_DOWN:
                rbd=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                rfd=False
            if event.key==pygame.K_RIGHT:
                rrt=False
            if event.key==pygame.K_LEFT:
                rlt=False
            if event.key==pygame.K_DOWN:
                rbd=False
    #update
    if rrt:
        rtank.rt()
    if rfd:
        rtank.fd()
    if rlt:
        rtank.lt()
    if rlt:
        rtank.lt()
    if rbd:
        rtank.bd()
    #draw
    disp.fill((41, 68, 190))
    pen.kadr()
    disp.blit(rtank.t, (rtank.x, rtank.y))
    pygame.time.Clock().tick(15)
    pygame.display.update()
pygame.quit()
 0, 255), (20, 20), (a-20, 20), 7)
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
