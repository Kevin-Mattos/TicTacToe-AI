#import intart 
import func
def num_partidas(qtd,who):
    board=func.zera_tab()

    player=['x','o']
    i=0
    k=0
    stats=[0,0,0]
    while(i<qtd):
        k=func.partida(board,player,who,True)
        stats[k]=stats[k]+1
        i=i+1
        func.imp(board)
        board=func.zera_tab()
        print(i)
    print('De {} jogos, x venceu {}, o venceu {} e {} foram empates'.format(q,stats[0],stats[1],stats[2]))
        
    return stats






x=int(input("deseja jogar quantas partidas: "))
y=int(input("0 pc comeca,1 vc comeca: "))
q=1
for i in range(0,x):
    num_partidas(q,y)


#x=intart.smart(func.zera_tab())





















