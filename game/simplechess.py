# Copyright(c) 2023-present, z-jarvis-z
import pygame
import sys
from pygame.locals import QUIT,KEYDOWN #quit关闭窗口的事件，
import time #调试，查找bug时使用过

BLACK = -1
NONE = 0
WHITE = 1

BLACKCOLOR = [0,0,0]
WHITECOLOR = [255,255,255]

screen_color = [60,80,100]#窗口颜色
frame_color = [0 ,229 ,238 ]#选框颜色

# 画框时使用
# if width == 0, (default) fill the rectangle
# if width > 0, used for line thickness
# if width < 0, nothing will be drawn
width = 2
border_radius = 1

#画布大小
HEIGHT = 720
WIDTH = 720

JUDGESIZE = 90#用于范围判断

FRAMESIZE = 120 #选中框大小

CHESSSIZE = 60 #棋子大小（半径）

#分数的文本位子
BLACKPOS = (355,660)
WHITEPOS = (355,30)

#鼠标按下数组中的左键下标
LEFTBUTTON = 0

#pos元组中的x轴，y轴数据下标
X = 0
Y = 1

#用于判断俩点之间是否有路线
#各顶点与连线构成一个无向图
#此无向图属于稀疏图，且只用于判断，不做其他用途，故只存储其16条路径
# 0  1  2
# 3  4  5
# 6  7  8
def MovePath():
    move_path={}#(x,y):TRUE x<y

    for i in range(6):#竖线路径
        move_path[(i,i+3)] = True
    for i in range(3):#横线路径
        for j in range(2):
            move_path[(i*3+j,i*3+j+1)]  = True
    # 斜线我找不到规律先凑合用吧
    move_path[(0,4)] = True
    move_path[(2,4)] = True
    move_path[(4,6)] = True
    move_path[(4,8)] = True
    return move_path

# 获取棋子可放位置的列表(才九个数据就不用for创造了主要是刚开始忘了哈哈哈哈哈哈)
def PositionInit(WIDTH=WIDTH,HEIGHT=HEIGHT):
    position_list=[(WIDTH/4,HEIGHT/2-WIDTH/4),(WIDTH/2,HEIGHT/2-WIDTH/4),(WIDTH/4*3,HEIGHT/2-WIDTH/4),
                   (WIDTH/4,HEIGHT/2),        (WIDTH/2,HEIGHT/2),        (WIDTH/4*3,HEIGHT/2),
                   (WIDTH/4,HEIGHT/2+WIDTH/4),(WIDTH/2,HEIGHT/2+WIDTH/4),(WIDTH/4*3,HEIGHT/2+WIDTH/4)
                  ]
    return position_list

def FindPos(position_list,x,y):
    for position in position_list:
        left = position[X] - JUDGESIZE
        right = position[X] + JUDGESIZE
        up =position[Y] - JUDGESIZE
        down =position[Y] + JUDGESIZE
        if x > left and x < right and y < down and y > up :
            return position        
    return (x,y)
# 初始化六枚棋子
def ChessInit():
    return [WHITE,WHITE,WHITE,NONE,NONE,NONE,BLACK,BLACK,BLACK]

#是否允许移动
def MoveAllow(start,end,move_path,chess_list):
    if  start == end :#起点与终点一致
        return False
    path_allow=None#路径是否存在
    if start < end :
        path_allow = (start,end) in move_path
    else :
        path_allow = (end,start) in move_path
    if not path_allow :
        return False
    if chess_list[end] == NONE :
        return True
    return False

def CheckEnd(chess_list):
    # 横线检查
    for i in range(3):
        if i == 0 and chess_list[0] == WHITE:
            continue
        if i == 2 and chess_list[2*3] == BLACK:
            continue
        if(chess_list[i*3] != NONE and chess_list[i*3] == chess_list[i*3+1] and chess_list[i*3] == chess_list[i*3+2]):
            return chess_list[i*3]
        
    # 竖线检查
    for i in range(3):
        if(chess_list[i] != NONE and chess_list[i] == chess_list[i+3] and chess_list[i] == chess_list[i+6]):
            return chess_list[i]
    # 斜线检查
    for i in [-1,1]:
        if(chess_list[4] != NONE and chess_list[4] == chess_list[1+i] and chess_list[4] == chess_list[7-i]):
            return chess_list[4]
    return NONE

# 画一个二分之一屏幕宽大小的米字格，默认画笔颜色为黑色，粗细为10BLACKCOLOR
def DrawGrid(screen,line_color=BLACKCOLOR,pen_size=10,WIDTH=WIDTH,HEIGHT=HEIGHT):
    for i in range(3):#三条横线
        y=WIDTH/4*(i+1)
        pygame.draw.line(screen,line_color,[WIDTH/4,y],[WIDTH/4*3,y],pen_size)
    for i in range(3):#三条竖线
        x=WIDTH/4*(i+1)
        pygame.draw.line(screen,line_color,[x,HEIGHT/2-WIDTH/4],[x,HEIGHT/2+WIDTH/4],pen_size)
    # 俩条斜线
    pygame.draw.line(screen,line_color,[WIDTH/4,HEIGHT/2-WIDTH/4],[WIDTH/4*3,HEIGHT/2+WIDTH/4],pen_size)
    pygame.draw.line(screen,line_color,[WIDTH/4*3,HEIGHT/2-WIDTH/4],[WIDTH/4,HEIGHT/2+WIDTH/4],pen_size)

# 画六个棋子
def DrawChess(screen,chess_list,position_list):
    for i in range(9):
        if chess_list[i] != NONE:
            if chess_list[i] == BLACK :
                pygame.draw.circle(screen,BLACKCOLOR,position_list[i],CHESSSIZE)
            elif chess_list[i] == WHITE :
                pygame.draw.circle(screen,WHITECOLOR,position_list[i],CHESSSIZE)

# 游戏开始喽
def GameStart():
    move_path = MovePath()
    position_list = PositionInit()
    chess_list = ChessInit()
    current_status = WHITE #用于判断当前应该选择黑棋还是白棋
    current_choose = None #用于存储选择的棋子的位子
    black_score = 0
    white_score = 0
    pygame.init()
    font = pygame.font.SysFont('Arial', 32)#文本的字体，大小
    screen = pygame.display.set_mode((WIDTH,HEIGHT)) #创建一个窗口
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN):
                sys.exit()#终止程序
        screen.fill(screen_color)
        DrawGrid(screen)#maybe去掉更好看xuanran
        DrawChess(screen,chess_list,position_list)
        white_txt = font.render(str(white_score), True,WHITECOLOR)#渲染
        black_txt = font.render(str(black_score),True,BLACKCOLOR)
        screen.blit(white_txt, WHITEPOS)#显示
        screen.blit(black_txt,BLACKPOS)
        #获取鼠标坐标信息
        x,y = pygame.mouse.get_pos()
        pos=FindPos(position_list,x,y)#定位
        pygame.draw.rect(screen,frame_color,[pos[X]-FRAMESIZE/2,pos[Y]-FRAMESIZE/2,FRAMESIZE,FRAMESIZE],width,border_radius)#画框

        keys_pressed = pygame.mouse.get_pressed()#鼠标按下

        if keys_pressed[LEFTBUTTON] == True:#左键按下
            if pos in position_list :
                if chess_list[position_list.index(pos)] == current_status :#是否选择了当前状态的棋子
                    current_choose = position_list.index(pos)
                elif chess_list[position_list.index(pos)] == NONE and current_choose != None:#不能下在有棋子的地方
                    #time.sleep(0.1)
                    if MoveAllow(current_choose,position_list.index(pos),move_path,chess_list) == True:#判断是否有路径
                        chess_list[current_choose],chess_list[position_list.index(pos)] = chess_list[position_list.index(pos)], chess_list[current_choose]
                        # 状态改变下一步移动另一个颜色的棋子 ||下一局输的人先下
                        if current_status == WHITE:
                            current_status = BLACK
                        else:
                            current_status = WHITE
        if CheckEnd(chess_list) != NONE:#赢了
            if CheckEnd(chess_list) == WHITE:
                white_score = white_score + 1
            else:
                black_score = black_score + 1
            chess_list = ChessInit()
            current_choose = None               
        pygame.display.update()#刷新页面

GameStart()
