import random
import os
import intart
def checa_vit(board,player):

    soma=0
    for i in range(0,3):#horizontal
        for j in range(0,3):
            if(board[i][j]==player):
                soma+=1
        if(soma==3):
            #print("horizontal na linha ",i+1)
            return True        
        soma=0

        
    soma=0
    for i in range(0,3):#Vertical
        for j in range(0,3):
            if(board[j][i]==player):
                soma+=1
        if(soma==3):
            #print("vertical na coluna ",i+1)
            return True        
        soma=0
        
    soma=0
    for i in range(0,3):#diagonal dir-esq
        if(board[i][i]==player):
             soma+=1
        if(soma==3):
            #print("diag 1 ")
            return True        
        
        

    if(board[0][2]==player and board[1][1]==player and board[2][0]==player):#dag esq-dir
        #print("diag 2")
        return True

    return False 
        
    
def imp(board):
    for i in range(0,3):
        print('|',end='')
        for j in range(0,3):
            if(board[i][j]==''):
                print(' |',end='')
            else:
                print('{}|'.format(board[i][j]),end='')
        print()
    print()

def play(board,player,eu):##random
    
    if(player=='o'and eu==True):
        imp(board)        
        linha=int(input('Digite linha: '))-1
        coluna=int(input('Digite coluna: '))-1

        while(not playable(board,(linha, coluna))):
            print('Posicoes invalidas')
            linha=int(input('Digite linha: '))-1
            coluna=int(input('Digite coluna: '))-1
        
    else:
        x=intart.iaplays(board,player)
        linha=x[0]#x[0]#random.randint(1,3)-1#
        coluna=x[1]#random.randint(1,3) -1#x[1]#
    #while((checa_ja_jogado(board,linha,coluna) )):
      #  linha=random.randint(1,3)-1
      #  coluna=random.randint(1,3) -1
       # print('{} {}'.format(linha,coluna))
    #imp(board)
    board[linha][coluna]=player
    imp(board)
    
def playable(board, pos):
    return board[pos[0]][pos[1]] == '' 

def checa_ja_jogado(board,i,j):#true para jogado
    if(board[i][j]=='x' or board[i][j]=='o'):
        return True
    return False

def partida(board,player,comeco,eu):
    i=comeco
    j=0
    while( j<9 ):
    
        play(board,player[i],eu)
        
    
        j+=1
        if((checa_vit(board,player[i]))):
            print('Vitoria de {}'.format(player[i]))
            j=199
            return i

        i+=1    
        i=i%2


    if(j!=199):
        print('empate')
        return 2
    
def zera_tab():
    board= [ ['','',''],
             ['','',''],
             ['','','']
            ]
    return board

def maior(x,y):
    if(x>y):
        return x
    else:
        return y

    return x

def menor(x,y):
    if(x<y):
        return x
    else:
        return y

    return x
    
