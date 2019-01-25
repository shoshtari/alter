import pygame, math, random
from math import *
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
    main=0
    def rt(self):
        self.angle-=10
        self.t=self.main
        self.t=pygame.transform.rotate(self.t, self.angle)
    def lt(self):
        self.angle+=10
        self.t=self.main
        self.t=pygame.transform.rotate(self.t, self.angle)        
    def fd(self):
        self.y-=20*cos(radians(self.angle))
        self.x-=20*sin(radians(self.angle))
    def bd(self):
        self.y+=10*cos(radians(self.angle))
        self.x+=10*sin(radians(self.angle))
class goloole():
    def __init__(self):
        self.x=500
        self.y=500
        self.angle=0
        self.a=1180
        self.b=780
        self.p=pygame.image.load("goloole.png")
    def fd(self):
        if self.x>=a or self.x <=20:
            self.angle=180-self.angle
        if self.y>=b or self.y<=20:
            self.angle=180-self.angle
        self.x-=21*sin(radians(self.angle))
        self.y-=21*cos(radians(self.angle))
        
pygame.init()
disp=pygame.display.set_mode((1200, 800))
done=False
pen=draw()
gtank=tank()
rtank=tank()
gtank.main=pygame.image.load("green tank.png")
rtank.main=pygame.image.load("red tank.png")
gtank.t=pygame.image.load("green tank.png")
rtank.t=pygame.image.load("red tank.png")
rfd=False
rrt=False
rlt=False
rbd=False
gfd=False
grt=False
glt=False
gbd=False
g1=goloole()
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
            if event.key==pygame.K_e:
                gfd=True
            if event.key==pygame.K_f:
                grt=True
            if event.key==pygame.K_s:
                glt=True
            if event.key==pygame.K_d:
                gbd=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                rfd=False
            if event.key==pygame.K_RIGHT:
                rrt=False
            if event.key==pygame.K_LEFT:
                rlt=False
            if event.key==pygame.K_DOWN:
                rbd=False
            if event.key==pygame.K_e:
                gfd=False
            if event.key==pygame.K_f:
                grt=False
            if event.key==pygame.K_s:
                glt=False
            if event.key==pygame.K_d:
                gbd=False
    #update
    if rrt:
        rtank.rt()
    if rfd:
        rtank.fd()
    if rlt:
        rtank.lt()
    if rbd:
        rtank.bd()
    if grt:
        gtank.rt()
    if gfd:
        gtank.fd()
    if glt:
        gtank.lt()
    if gbd:
        gtank.bd()
    #draw
    disp.fill((41, 68, 190))
    pen.kadr()
    disp.blit(rtank.t, (rtank.x, rtank.y))
    disp.blit(gtank.t, (gtank.x, gtank.y))
    disp.blit(g1.p, (g1.x, g1.y))
    pygame.time.Clock().tick(15)
    pygame.display.update()
pygame.quit()
