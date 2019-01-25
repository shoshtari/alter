import pygame, math, random
from math import *
class draw():
    def __init__(self):
        self.tool=1200
        self.arz=700
    def kadr(self):
        a=self.tool
        b=self.arz
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (20, 20), (20, b-20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (a-20, 20), 7)
        pygame.draw.line(disp, (0, 0, 255), (a-20, b-20), (20, b-20), 7)
class goloole():
    def __init__(self):
        self.run=False
        self.x=500
        self.y=500
        self.angle=0
        self.a=1180
        self.b=680
        self.p=pygame.image.load("goloole.png")
        self.t=0
    def start(self, x, y, angle):
        self.run=True
        self.x=x
        self.y=y
        self.angle=angle
        self.t=0
    def fd(self):
        self.t+=1
        if self.x>=self.a or self.x <=20:
            self.angle=-self.angle
        if self.y>=self.b or self.y<=20:
            self.angle=180-self.angle
        self.x-=17*sin(radians(self.angle))
        self.y-=17*cos(radians(self.angle))
    
class tank():
    def __init__(self):
        self.x=random.randint(200,1000)
        self.y=random.randint(100,500)
        self.angle=0
        self.tir=[goloole(),goloole(),goloole(),goloole(),goloole()]
    t=0
    main=0
    def rt(self):
        self.angle-=15
        self.t=self.main
        self.t=pygame.transform.rotate(self.t, self.angle)
    def lt(self):
        self.angle+=15
        self.t=self.main
        self.t=pygame.transform.rotate(self.t, self.angle)        
    def fd(self):
        self.y-=15*cos(radians(self.angle))
        self.x-=15*sin(radians(self.angle))
    def bd(self):
        self.y+=10*cos(radians(self.angle))
        self.x+=10*sin(radians(self.angle))
    def bullet_update(self):
        i=4
        while i>=0 :
            if self.tir[i].run:
                self.tir[i].fd()
            if self.tir[i].t==200:
                self.tir[i].run=False
            i-=1
    def show_bullet(self):
        i=4
        while i>=0 :
            if self.tir[i].run==True:
                disp.blit(self.tir[i].p, (self.tir[i].x, self.tir[i].y))
            i-=1
pygame.init()
disp=pygame.display.set_mode((1200, 700), pygame.FULLSCREEN)
#disp=pygame.display.set_mode((1200, 700))
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
while not done:
    #event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                done=True
            if event.key==pygame.K_UP:
                rfd=True
            if event.key==pygame.K_RIGHT:
                rrt=True
            if event.key==pygame.K_LEFT:
                rlt=True
            if event.key==pygame.K_DOWN:
                rbd=True
            if event.key==pygame.K_SPACE:
                i=0
                while i<=4 and rtank.tir[i].run:
                    i+=1
                if i<=4:
                    rtank.tir[i].start(rtank.x, rtank.y, rtank.angle)
            if event.key==pygame.K_e:
                gfd=True
            if event.key==pygame.K_f:
                grt=True
            if event.key==pygame.K_s:
                glt=True
            if event.key==pygame.K_d:
                gbd=True
            if event.key==pygame.K_q:
                i=0
                while i<=4 and gtank.tir[i].run:
                    i+=1
                if i<=4:
                    gtank.tir[i].start(gtank.x, gtank.y, gtank.angle)
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
    rtank.bullet_update()
    rtank.show_bullet()
    gtank.bullet_update()
    gtank.show_bullet()
    pygame.time.Clock().tick(20)
    pygame.display.update()
pygame.quit()
