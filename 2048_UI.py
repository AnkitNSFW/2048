from os import system
from random import choice
import tkinter as tk
import time

gui = tk.Tk()
gui.title('2048')
score = 0
gamef = True


board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
numcolor={0:'#cdc0b2',2:'#efe4db',4:'#ece1c8',8:'#f2b078',16:'#f49463',32:'#f67d5e',64:'#f75f3b',128:'#edce73',256:'#edcd60',512:'#ecc851',1024:'#ecc43f',2048:'#edc22e',4096:'#3f3833'}

pad=' '
space='|'
line='-'

replacement1=[2,2,2,2,4] 
replacement2=[2,2,2,4]
replacement3=[2,4]
right_input=['w','a','s','d','q','r']  

gamestatus=''

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


def game_logic(user_move):
    #user_move=userinput()
    global gamef,gamestatus,score,board
    hor,ver=same_check()
    fit(user_move)

    if gamef:
        if user_move=='q':
            print('Game Ended')     
            quit()

        elif user_move=='w':
            hor,ver=same_check()
            fit(user_move)
            for y in range(4):
                for x in range(3):        
                    if ver[x][y]==1:
                        board[x][y]=board[x][y]*2
                        board[x+1][y]=0
                        score+=board[x][y]
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
                        score+=board[x][y]
                        fit(user_move)
                        hor,ver=same_check()

        elif user_move=='d':
            hor,ver=same_check()
            fit(user_move)
            for x in range(4):
                for y in reversed(range(3)):           
                    if hor[x][y]==1:
                        board[x][y+1]=board[x][y+1]*2
                        board[x][y]=0
                        score+=board[x][y]
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
                        score+=board[x][y]
                        fit(user_move)
                        hor,ver=same_check()
        elif user_move=='r':
            board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            score=0
            num_display()
        random_generator() 
        game_move() 
    return board,gamestatus,score,gamef

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

def zerotoempty(x):
    if x==0:
        return ' '
    else:
        return x



def num_display():
    global gamestatusd
    tk.Label(gui,text='Score : '+str(score)).grid(row=0,columnspan=4)
    for x in range(4):
        for y in range(4):
            tk.Label(gui,text=zerotoempty(board[x][y]),bg=numcolor.get(board[x][y]),width=6,height=3,borderwidth=0.5,relief='solid',font=30).grid(row=x+1,column=y)
            tk.Label(gui,text=gamestatus,font=40).grid(row=5,columnspan=4)


def key_pressed(user_key):
    global gamestatus

    x=str(user_key.char)
    if x in right_input:
        if x =='q':
            gamestatus= 'Game Ended'

        game_logic(x)

def game_move():
    global gamestatus
    num_display()
    l=largest()
    flag=game_end()
    num_display()
    if flag:
        print('Game Over!!!')
        quit()
    return gamestatus

def quit():
    global gamestatus
    num_display() 
    time.sleep(5)
    gui.destroy()


random_generator()
num_display()
gui.bind('<Key>',key_pressed)

    
num_display()
gui.mainloop()

