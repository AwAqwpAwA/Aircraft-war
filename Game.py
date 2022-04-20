
import pygame#引用模块

pygame.init()#初始化
window = pygame.display.set_mode((820,820))#设置窗口
pygame.display.flip()#刷新
pygame.display.set_caption("飞机大战")#修改标题

ttc = pygame.font.SysFont('microsoftyaheiui',80)#设置字体
fps = pygame.time.Clock()#设置帧数
die = False
win_x = window.get_size()[0]
win_y = window.get_size()[1]
home = [int(win_x/2),int(win_y/2)]
plane = home[0],home[1]-40
kill = 0
FPS = 24
弹=[]
red_弹=[]
max = 20
生成=max
red_plane = []
杀戮光环=False

def 随机数(min,mix):
    import random
    return random.randint(min, mix)

def 绘制矩形(颜色,x,y,w,h,l=0):pygame.draw.rect(window,颜色,(x,y,w,h),l)

def make_plane(x,y):
    绘制矩形("black",x-10,y-60,20,20)
    绘制矩形("black",x-10,y-40,20,20)
    绘制矩形("black",x-30,y-40,20,20)
    绘制矩形("black",x+10,y-40,20,20)

def make_red_plane(x,y):
    绘制矩形("red",x-10,y-60,20,20)
    绘制矩形("red",x-10,y-40,20,20)
    绘制矩形("red",x-30,y-60,20,20)
    绘制矩形("red",x+10,y-60,20,20)

def make_弹(x,y):绘制矩形("black",x,y,20,20)

def make_red_弹(x,y):绘制矩形("red",x,y,20,20)

def 范围(x,y,X,Y):
    A = X - 30
    B = Y
    C = Y + 20
    D = X + 30
    E = x
    F = y
    G = y + 20
    H = x + 20
    return (D > E > A or D > H > A) and (C > F > B or C > G > B)

while True :

    fps.tick(FPS)
    window.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:die = False
            if event.key == pygame.K_UP:FPS += 1
            if event.key == pygame.K_DOWN and FPS > 1 :FPS -= 1
            if event.key == pygame.K_c:杀戮光环=1
            if event.key == pygame.K_x:杀戮光环=0
            if event.key == pygame.K_q:
                kill += len(red_plane)
                red_plane.clear()
        if event.type == pygame.MOUSEMOTION:plane = event.pos

    if len(弹) < 10 and 生成 % 5 == 0 and 生成 : 弹.append([plane[0]-10,plane[1]-60])

    if len(red_plane) < 10 and 生成 % 2 == 0 and not 生成 : red_plane.append([随机数(30,win_x-30),随机数(60,400 )])

    if 生成 == max :

        for i in range(len(red_弹)):
            try:
                if red_弹[i][1] > win_y : red_弹.pop(i)
            except:pass

        for i in range(len(red_plane)):
            if len(red_弹) < 10 :red_弹.append([red_plane[i][0]-10,red_plane[i][1]-40])

        生成 = 0
    
    elif 生成 < max : 生成 += 1

    window.blit(ttc.render(str(kill),True,"black","white"),(0,0))

    make_plane(plane[0],plane[1])

    try:
        for i in range(len(弹)):
            弹[i][1]-=20
            if 弹[i][1]<0:弹.pop(i)
            else:make_弹(弹[i][0],弹[i][1])
            for ii in range(len(red_plane)):
                if 范围(弹[i][0],弹[i][1],red_plane[ii][0],red_plane[ii][1]-40) or 杀戮光环 :
                    red_plane.pop(ii)
                    kill += 1
                    弹.pop(i)
    except:pass
    
    for i in range(len(red_plane)):
        try:
            red_plane[i][1]+=4
            if red_plane[i][1]>win_x:
                red_plane.pop(i)
                die = True
            else:make_red_plane(red_plane[i][0],red_plane[i][1])
        except:pass

    for i in range(len(red_弹)) : 
        red_弹[i][1] += 16  
        make_red_弹(red_弹[i][0],red_弹[i][1])
        if 范围(red_弹[i][0],red_弹[i][1],plane[0],plane[1]-40):die = True

    if die:
        window.fill("white")
        die_text = ttc.render("逊",True,"black","white")
        die_x,die_y = die_text.get_size()
        window.blit(die_text,(win_x/2-die_x/2,win_y/2-die_y/2))
        plane = home
        red_plane.clear()
        弹.clear()
        red_弹.clear()
        kill = 0
        生成 = max - 2
    
    pygame.display.update()