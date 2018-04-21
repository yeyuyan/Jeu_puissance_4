import pygame
from pygame.locals import *
import time



    ###Programme principal###



BLACK = (0,0,0)
WHITE = (255, 255, 255)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
white_rect = pygame.Rect(0, 0, 824, 549)
pygame.init()
windowSurface = pygame.display.set_mode((824, 549))
font = pygame.font.Font("FreeSans.ttf", 50)
win_text = font.render("You've won", True, BLACK)
pygame.display.set_caption('demo')
yellowPiece = pygame.image.load("黄棋.png")
bluePiece = pygame.image.load("蓝棋.png")
board = pygame.image.load("棋盘.png")
highLight = pygame.image.load("光条.png")
board = pygame.transform.scale(board, (824, 549))
highLight = pygame.transform.scale(highLight, (101, 549))
l_piece=90
yellowPiece = pygame.transform.scale(yellowPiece, (l_piece, l_piece))
bluePiece = pygame.transform.scale(bluePiece, (l_piece, l_piece))
wait=False
table=[[0 for j in range(13)] for i in range(12)]
tableT=list(zip(*table))
tableStr=["" for i in range(7)]
turn=1
while 1:
    mouse_pos = pygame.mouse.get_pos()
    #print(mouse_pos)

    pygame.draw.rect(windowSurface, WHITE, white_rect)#白色底

    x_left=60
    col=((mouse_pos[0]-x_left)//101)#数组index
    x_hl=x_left+col*101
    #print(col)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
        if event.type == MOUSEBUTTONDOWN:
            if not(wait) and 0 in tableT[col+3][3:9] and -1<col<7:
                x_falling=x_hl
                col_falling=col
                turn_falling=turn
                wait=True
                y_shouldBe=(4-len(tableStr[col_falling]))*(l_piece-14)+114
                
                y_falling=0
    if wait:
        y_falling+=5#当其正在掉落
        if turn_falling==1: windowSurface.blit(yellowPiece, (x_left+97+(col_falling-1)*104,y_falling))
        if turn_falling==2: windowSurface.blit(bluePiece, (x_left+97+(col_falling-1)*104,y_falling))
    if wait and y_shouldBe-y_falling<=3:
        #for i in range(4,10):
        #    print(table[i]) 
        wait=False
        y_falling=y_shouldBe
        tableStr[col_falling]+=str(turn)
        #print(tableStr)
        tableT=list(zip(*table))    
        line=len(tableStr[col_falling])
        tableT[col_falling+3]=[0]*3+[0]*(6-line)+list(tableStr[col_falling])[::-1]+[0]*3
        tableT[col_falling+3]=list(map(int,tableT[col_falling+3]))
        #for i in range(len(tableT)):
        #    print(tableT[i]) 
        table=list(zip(*tableT))
        
        cor=[-3,-2,-1,+1,+2,+3]
        print()
        for i in range(len(table)):
            print(table[i])   
        diagsP=[[(cor[i+j],cor[i+j]) for j in range(3)]+[(0,0)] for i in range(4)]
        win = False
        if True in [len(list(set([table[13-line-4+diagsP[i][j][0]][col_falling+3+diagsP[i][j][1]] for j in range(4)])))==1 for i in range(4)]:
            win = True
        cor=[-3,-2,-1,+1,+2,+3]
        diagsP=[[(cor[i+j],-cor[i+j]) for j in range(3)]+[(0,0)] for i in range(4)]
        if True in [len(list(set([table[13-line-4+diagsP[i][j][0]][col_falling+3+diagsP[i][j][1]] for j in range(4)])))==1 for i in range(4)]:
            win = True
        win = win or str(turn)*4 in "".join(list(map(str,table[13-line-4]))) or str(turn)*4 in "".join(list(map(str,tableT[col_falling+3])))      
        turn=3-turn
        if win:
            for i in range(3,10):
                for j in range(3,11):
                    if table[i][j]==1:
                        windowSurface.blit(yellowPiece, (x_left+97+(j-4)*104,(i-4)*(l_piece-14)+114))
                    if table[i][j]==2:
                        windowSurface.blit(bluePiece, (x_left+97+(j-4)*104,(i-4)*(l_piece-14)+114))
            windowSurface.blit(board, (0,0))
            windowSurface.blit(win_text, (10, 20))
            pygame.display.update()
            time.sleep(3000)
            pygame.quit()
    if -1<col<7:    
        windowSurface.blit(highLight, (x_hl,0))

        #print(table[i])
    for i in range(3,10):
        for j in range(3,11):
            if table[i][j]==1:
                windowSurface.blit(yellowPiece, (x_left+97+(j-4)*104,(i-4)*(l_piece-14)+114))
            if table[i][j]==2:
                windowSurface.blit(bluePiece, (x_left+97+(j-4)*104,(i-4)*(l_piece-14)+114))
    windowSurface.blit(board, (0,0))
    pygame.display.update()


            
    
    
        
