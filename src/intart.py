import func
import random
def copy(board):#problema memoria
    copy= [ ['','',''],
            ['','',''],
            ['','','']
            ]
    for i in range(0,3):
        for j in range(0,3):
            copy[i][j]=board[i][j]
    return copy

    

def heuristica(board,x,player):
    soma=0
    if(  (x[0]==0 and  (x[1]==0 or x[1]==2)) or (x[0]==2   and  (x[1]==0 or x[1]==2))   ): ##canto
       soma+= 1

    if(x[0]==1 and x[1]==1):#meio
        soma+= 2

    if(func.checa_ja_jogado(board,x[0],x[1])): #ja tem peça
        soma= -10000
        return soma

    
    board_x=copy(board)
    board_o=copy(board)
    board_x[x[0]][x[1]]='x'
    board_o[x[0]][x[1]]='o'

    if(player=='x'):
        if(func.checa_vit(board_x,player)):
            soma= 500
            return soma
        if( func.checa_vit(board_o,other_player(player)) ):
            soma= 20
            return soma

    if(player=='o'):
        if(func.checa_vit(board_o,player)):
            soma= 500
            return soma
        if( func.checa_vit(board_x,other_player(player)) ):
            soma= 20
            return soma

   
    return soma
    
def other_player(player):
    if (player=='x'):
        return 'o'
    else:
        return 'x'

def zera_matrix():
    matriz= [ [0,0,0],
              [0,0,0],
              [0,0,0]
             ]
    return matriz
def deleta_td(x):
    for i in range(0,len(x)):
        del x[0]
        
def iaplays(board,player):
    if(player=='x'):
        return x_plays(board)
        
    bestplay=zera_matrix()
    maior=[0,0]
    count=0
   
    x=[0,0]
    linhas=[]
    colunas=[]
    
    for i in range(0,3):
        for j in range(0,3):
            x[0]=i
            x[1]=j
            bestplay[i][j]=heuristica(board,x,player)
            
    aux=bestplay[0][0]
            
    for i in range(0,3):
        for j in range(0,3):
            if(bestplay[i][j]>=aux):                
                maior[0]=i
                maior[1]=j

                if(bestplay[i][j]==aux):
                    linhas.append(i)
                    colunas.append(j)
                else:                    
                    deleta_td(linhas)
                    deleta_td(colunas)
                    
                aux=bestplay[i][j]
                
    print(bestplay)
    print(linhas)
    print(colunas)
       
    if(len(linhas)>0):
        aux2=random.randint(0,len(linhas)-1)
        #print('aux2=',aux2)
        maior[0]=linhas[aux2]
        maior[1]=colunas[aux2]

    return maior

def minimax(node,profundidade,maxplayer,player):
    #func.imp(node)
    #print("i== ",profundidade)
    v=0
    best_value=0
    aux=todas_pos(node)

    if (node==[['x','',''],['','o',''],['','','x']]):
        return 10
        

    if(len(aux)==0 or func.checa_vit(node,'x') or func.checa_vit(node,'o')):#or not(node.tem_filho()) ):
        #print("ENTROU AUQI GRANDAO HEHE")
        if(func.checa_vit(node,'x')):
            return 10
        elif(func.checa_vit(node,'o')):
            return -10
        else:
            return 0
     

    if(maxplayer==True):
        best_value=-10
        for i in range(0,len(aux)):#qtd de filhos
            v=minimax(play(node,player,aux[i]),profundidade+1,False,other_player(player))
            best_value=func.maior(best_value,v)
        return best_value

    else:
        best_value=+10
        for i in range(0,len(aux)):#qtd de filhos NA VDD É O NUMERO DE POSSIBILIDADES
            v=minimax(play(node,player,aux[i]),profundidade+1,True,other_player(player))
            best_value=func.menor(best_value,v)
        return best_value

def x_plays(x):

    num_jog=todas_pos(x)
    h=[]
    print(num_jog)
    if(len(num_jog)==9):
        x=[0,0]
        return x

    
    for i in range(0,len(num_jog)):
        y=copy(x)
        vet=num_jog[i]
        y[vet[0]][vet[1]]='x'
        h.append(minimax(y,0,False,'o'))#intart.iaplays(board,'x')#)
    k=0
    aux=h[0]
    for i in range(0,len(h)):
        if(h[i]>aux):
            k=i
            aux=h[i]


    vet=num_jog[k]
    #x[vet[0]][vet[1]]='x'
    print(h)
    return vet
        
    func.imp(x)
    
def play(board,player,pos):
    aux=copy(board)
    aux[pos[0]][pos[1]]=player
    return aux
    
    
def heuri2(board,x,player):
    if(len(x)==0):
        return 0
    soma=0
    
    board_x=copy(board)
    board_o=copy(board)
    board_x[x[0]][x[1]]='x'
    board_o[x[0]][x[1]]='o'

    if(player=='x'):
        if(func.checa_vit(board_x,player)):
            soma=10
        if( func.checa_vit(board_o,other_player(player)) ):
            soma=-10

    if(player=='o'):
        if(func.checa_vit(board_o,player)):
            soma=10
        if( func.checa_vit(board_x,other_player(player)) ):
            soma=-10

   
    return soma


def todas_pos(board):
    v=[]
    
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==''):
                v.append([i,j])

    return v
            
    

class smart:
    filho=[]
    board=0
    def __init__(self,board):
        self.board=copy(board)

    def insere(self,board):
        self.filho.append(smart(board))
        
    def get_board(self):
        return self.board
    
    def get_filho(self,i,pos,player):
        self.board[pos[0]][pos[1]]=player
        
        self.insere(self.board)
        
        return self.filho[i]
    
    def tem_filho(self):
        if (len(self.filho)==0):
            return False
        else:
            return True
    


















    
