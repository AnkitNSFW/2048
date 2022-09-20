from os import system
from random import choice

r1=[0,0,0,0]
r2=[0,0,0,0]
r3=[0,0,0,0]
r4=[0,0,0,0]

#  Necessary predefined Values
'''r1=[2,0,2,2]
r2=[2,128,2,0]
r3=[2,128,256,0]
r4=[2,512,512,0]'''


board=[r1,r2,r3,r4]

pad=' '
space='|'
line='-'

replacement1=[2,2,2,2,4] 
replacement2=[2,2,4]
replacement3=[2,2,4,4,8]
right_input=['w','a','s','d','quit']  

game=True

def padding(num):
    if num==0:
        return space+pad*5
    elif num==1:
        return space+pad*5
    elif len(str(num))==1:
        return space+pad*4+str(num)
    elif len(str(num))==2:
        return space+pad*3+str(num)
    elif len(str(num))==3:
        return space+pad*2+str(num)
    elif len(str(num))==4:
        return space+pad+str(num)
    else:
        return space+str(num)

def display():
    for x in range(4):
        print(line*25)
        '''a=board[x][0]
        b=board[x][0]
        c=board[x][0]
        d=board[x][0]'''
        print(padding(board[x][0])+padding(board[x][1])+padding(board[x][2])+padding(board[x][3])+space)
    print(line*25)

def random_generator():
    empty_list_loc=[]
    for x in range(4):
        for y in range(4):
            if board[x][y]==0:
                empty_list_loc.append([x,y])
    if len(empty_list_loc)!=0:
        [a,b]=choice(empty_list_loc)
        large=largest()
        if largest()>=256:
            board[a][b]=choice(replacement3)
        elif largest()>=128:
            board[a][b]=choice(replacement2)
        else:
            board[a][b]=choice(replacement1)

def largest():
    large=0
    for x in range(4):
        for y in range(4):
            if board[x][y]>large and board[x][y]%2==0:
                large=board[x][y] 
    return large
                
def same_check():
    same_list_x=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    for x in range(4):
        for y in range(3):
            if   not (board[x][y]==0) | (board[x][y]==1) :  #Only works if not 0 or 1
                if board[x][y]==board[x][y+1]:
                    if board[x][y]==board[x][y+1]:
                        same_list_x[x][y]=1


    same_list_y=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]               
    for x in range(3):
        for y in range(4):
            if   not ( board[x][y]==0) | (board[x][y]==1) :  #Only works if not 0 or 1
                if board[x][y]==board[x+1][y]:
                        same_list_y[x][y]=1
    
    return same_list_x,same_list_y

def same():
    slistx,slisty=same_check()
    for x in range(len(slistx)):
        print(slistx[x])
    print('\n')
    for x in range(len(slisty)):
        print(slisty[x])

def fit(input):
    if input=='w':
        for z in range(3):
            for x in range(3):
                for y in range(4):
                    if board[x][y]==0:
                        board[x][y]=board[x+1][y]
                        board[x+1][y]=0

    elif input=='s':
        for z in range (3):
            for x in reversed(range(1,4)):
                for y in range(4):
                    if board[x][y]==0:
                        board[x][y]=board[x-1][y]
                        board[x-1][y]=0

    elif input=='a':
        for z in range(3):
            for y in range(3):
                for x in range(4):
                    if board[x][y]==0:
                        board[x][y]=board[x][y+1]
                        board[x][y+1]=0

    elif input=='d' :
        for z in range(3):
            for y in reversed(range(1,4)) :
                for x in range(4):
                    if board[x][y]==0:
                        board[x][y]=board[x][y-1]
                        board[x][y-1]=0

    return board

def userinput():
    while True:
        user_input=input('Enter the Next Move : ')
        user_input.lower()
        if user_input in right_input:
            break
        else:
            print('Incorrect Input ')
    return user_input

def game_logic():
    user_move=userinput()
    global game
    hor,ver=same_check()
    fit(user_move)

    if user_move=='q':
        print('Game Over')
        game=False
        return game

    elif user_move=='w':
        hor,ver=same_check()
        fit(user_move)
        for y in range(4):
            for x in range(3):        
                if ver[x][y]==1:
                    board[x][y]=board[x][y]*2
                    board[x+1][y]=0
                    fit(user_move)
                    hor,ver=same_check()

    elif user_move=='s':
        hor,ver=same_check()
        fit(user_move)
        for y in range(4):
            for x in reversed(range(1,4)):           
                if ver[x-1][y]==1:
                    board[x][y]=board[x][y]*2
                    board[x-1][y]=0
                    fit(user_move)
                    hor,ver=same_check()

    elif user_move=='d':   # logic broken
        hor,ver=same_check()
        fit(user_move)
        for x in range(4):
            for y in reversed(range(3)):           
                if hor[x][y]==1:
                    board[x][y+1]=board[x][y+1]*2
                    board[x][y]=0
                    fit(user_move)
                    hor,ver=same_check()
        
    elif user_move=='a':
        hor,ver=same_check()
        fit(user_move)
        for x in range(4):
            for y in range(3):           
                if hor[x][y]==1:
                    board[x][y]=board[x][y]*2
                    board[x][y+1]=0
                    fit(user_move)
                    hor,ver=same_check()
    random_generator() 
    system('cls')
    display()  
    return board

def game_end():
    empty_space=0
    for x in range(4):
        for y in range(4):
            if board[x][y]==0:
                empty_space+=1
    same=0        
    hor,ver=same_check()
    for x in range(4):
        for y in range(3):
            if hor[x][y]==1:
                same+=1
    for x in range(3):
        for y in range(4):
            if ver[x][y]==1:
                same+=1
    if  same==0 and empty_space==0:
        return True
    else:
        return False

random_generator()
display()
while True:
    game_logic()
    l=largest()
    if l >=128:
        print('You Won!!!')
        break
    flag=game_end()
    if flag:
        print('Game Over!!!')
        break

        
    











