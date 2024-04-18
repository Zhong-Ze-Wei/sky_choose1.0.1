# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
# 显示中文  YaHei  JhengHei
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
import numpy as np
import sys, random, math, pygame,os
from pygame.locals import *
from  matplotlib import cm
from bf_button import BFButton
pygame.mixer.init()

#————————————————————————————————————————————————————建立转盘类型———————————————————————————————————————————————————————

class   zhuanpan():
    def __init__(self,image,x,y):
        self.rawimage = pygame.image.load(image)            #原始图形
        self.image = self.rawimage                        #旋转后的图形,初始值就是原始图啦
        self.rect = self.rawimage.get_rect()            #获取原始图形的矩形.
        self.rect.x = x
        self.rect.y = y
    def rotate(self,degree):
        self.image = pygame.transform.rotate(self.rawimage,degree)
        self.rect = self.image.get_rect()
        self.rect.y = screenHeight//2 - self.rect.h//2

    def update(self):
        screen.blit(self.image,self.rect)



#——————————————————————————————————————以下是制图———————————————————————————————————————————————————————————————————————
myfile = open('name.txt',encoding="utf-8")
lines = len(myfile.readlines())
sizes=[1]*lines                                                                  #通过zp.txt的行数生成饼状图的元素

with open('name.txt','r',encoding="utf-8") as f:
    labels = f.read().splitlines()

colors = cm.rainbow(np.arange(len(sizes))/len(sizes))# colormaps: Paired, autumn, rainbow, gray,spring,Darks(渐变色)

plt.pie(sizes,labels=labels,textprops={'fontsize': 12, 'color': 'w'},startangle=0,colors=colors)      #生成主图像

plt.axis('equal')                                                                       #保证形状为圆形

plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0)                    #防止白边过大

#————————————————————————————制图结束，需要每次保存都是不同的png图片————————————————————————————————————————————————

f = open("num.txt", "r")
i = f.read()
f = open("num.txt", "w")
f.write(str(int(i)+1))
f.close()
plt.savefig('转盘库/p'+str(i)+'.png')


plt.legend(loc='center left',fontsize=10,bbox_to_anchor=(0.83,0.7),borderaxespad=0.9)         #生成图例
plt.savefig('转盘库/tl'+str(i)+'.png')
#——————————————————————————————————————————————————————————创建窗口—————————————————————————————————————————————

pygame.init()                                                 #初始化图像
#size=width,height=1000,800                                    #窗口大小
size=screenWidth ,screenHeight = 800,600
screen = pygame.display.set_mode(size,pygame.NOFRAME)        #主页面无边框
#screen = pygame.display.set_mode(size)                        #主页面有边框
pygame.display.set_caption('大转盘')                          #游戏标题
fclock = pygame.time.Clock()                                  #刷新率用
fps=60                                                       #刷新率用
tt= "转盘库/p"+i+".png"                                     #加载图片
tl= '转盘库/tl'+i+'.png'
speed=350
pygame.mixer.music.load("move.mp3")
screen = pygame.display.set_mode((screenWidth,screenHeight))
angle=0

#bgRect = bg.get_rect()
#get_rect()是一个处理矩形图像的方法，返回值包含矩形的居中属性（ center centerx centery ）
#————————————————————————————————————以下是按钮设置——————————————————————————————————————————————————————————————

def do_click1(btn):
    btn.visible = False



def do_click2(btn):
    pygame.quit()
    exit()


buttona = BFButton(screen, (0, 0,800, 150),text ='Welcome to the SKY CHOOSE',click = do_click1)
buttonb = BFButton(screen, (0, 150, 800, 150),text ="USE  'UP'   to add  speed",click = do_click1)
buttonc = BFButton(screen, (0, 300, 800, 150),text ="USE 'DOWN'  to lose speed",click = do_click1)
buttond = BFButton(screen, (0, 450, 800, 150),text ="USE  'SPACE'   to    STAR",click = do_click1)
button2 = BFButton(screen, (720,0,80,40),text='QUIT',click=do_click2)
#————————————————————————————————————————————————————————————————————————————————————————————————————————————————
class Star():
    def __init__(self,image,x,y):
        self.rawimage = pygame.image.load(image)            #原始图形
        self.image = self.rawimage                        #旋转后的图形,初始值就是原始图啦
        self.rect = self.rawimage.get_rect()            #获取原始图形的矩形.
        self.rect.x = x
        self.rect.y = y
    def rotate(self,degree):
        self.image = pygame.transform.rotate(self.rawimage,degree)
        self.rect = self.image.get_rect()
        self.rect.x = screenWidth//2 - self.rect.w//2
        self.rect.y = screenHeight//2 - self.rect.h//2

    def update(self):
        screen.blit(self.image,self.rect)

#————————————————————————————————————————创建转盘与图标————————————————————————————————————————————————————
form = pygame.image.load(tl)

星星 = zhuanpan(tt,screenWidth//2,screenHeight//2)

clock = pygame.time.Clock()

#------------------------------------------------------------------------------------------------------
while speed>=-1:                                                   #游戏循环

    for event in pygame.event.get():                          #获取事件
        if event.type ==pygame.QUIT:                          # QUIT关闭按钮被点击事件
            sys.exit()
        if button2.update(event):
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()



        buttona.update(event)
        buttonb.update(event)
        buttonc.update(event)
        buttond.update(event)

    screen.fill((255,255,255))

    text=pygame.font.SysFont('SimHei', 36)
    speedtext = text.render('SPEED:'+str(int(speed/2)), True, (0, 0, 0))
    textRectObj = speedtext.get_rect()
    textRectObj.center = (700, 70)

#——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
    keys = pygame.key.get_pressed()
    if keys[K_UP] and speed <= 598 and speed>=200:
        speed += 2
    if keys[K_DOWN] and speed <= 600 and speed>=202:
        speed -= 2
    if (keys[K_SPACE] or angle>=1) and speed>=1:
        angle = angle + speed
        ran = random.uniform(0, 1)
        if speed>=20 and ran>=0.3:
            speed-=1
        if speed>=50 and ran>=0.5:
            speed-=1
        if speed>=100and ran>=0.7:
            speed-=1
        ran = random.uniform(0, 1)
        if 1-ran**2<=speed*0.05:
            speed-=0.2
            星星.update()

#————————————————————————————————————————————描绘转盘外物————————————————————————————————————————————————————————
    a=((lines-1)-int(int(angle%360-90)/(360/lines)))%lines

    if speed<1 and (angle%360)%(360/lines)<(360/lines)/2-5:
        angle+=1
    if speed < 1 and (angle%360)%(360/lines)> (360/lines)/2+5:
        angle-=1
        星星.update()
    print((angle%360)%(360/lines))
    if speed>=1 and angle>=100:
        pygame.mixer.music.play()
    星星.rotate(angle)
    星星.update()
    screen.blit(form, (-537,20))                                            #图例
    screen.blit(speedtext, textRectObj)                                #文字
    pygame.draw.line(screen, (0,0,0), (400,300), (398,200),3)
    pygame.draw.line(screen, (0,0,0), (400,300), (402,200),3)


    end = text.render('恭喜' + str(labels[a]), True, (0, 0, 0))
    textend = end.get_rect()
    textend.center = (400,300)
    if speed<=1:
        screen.blit(end, textend)

    if int(i)<=3:
        buttond.draw()
        buttonc.draw()
        buttonb.draw()
        buttona.draw()
    button2.draw()
    fclock.tick(60)

    pygame.display.update()



