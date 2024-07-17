import random
import os
# x anda pelas colunas e y pelas linhas
posicao = {
    'posicao_x': 0,
    'posicao_y': 0,
}
linhas_mapa = 10
colunas_mapa = 10

dificuldade = int(input("Escolha a dificuldade 1, 2 ou 3"))

if dificuldade == 1:
    dificuldade = 15
elif dificuldade == 2:
    dificuldade = 25
elif dificuldade == 3:
    dificuldade = 40

def direcao(x):
    if x == 'd':
        posicao['posicao_x']+=1
    if x == 'a':
        posicao['posicao_x']-=1
    if x == 'w':
        posicao['posicao_y']-=1    
    if x == 's':
        posicao['posicao_y']+=1 
    
    if posicao['posicao_x'] < 0 or posicao['posicao_y'] < 0 or posicao['posicao_x'] > colunas_mapa-1 or posicao['posicao_y'] > linhas_mapa-1:
        if x == 'd':
            posicao['posicao_x']-=1
        if x == 'a':
            posicao['posicao_x']+=1
        if x == 'w':
            posicao['posicao_y']+=1    
        if x == 's':
            posicao['posicao_y']-=1 
        return posicao
    return posicao

def mapa(y, x):
        os.system('cls')
        global A
        A = []	
        
        for i in range(y):	    
            A = A + [["🟪"]*x] # cria uma nova lista [0]*5
        for i in range(dificuldade):
            A[random.randint(0, y-1)][random.randint(0, x-1)]='🟥'
        
        A[linhas_mapa-1][colunas_mapa-1]= '🟩'
        
        for l in range(y):
            for c in range(x):
                if posicao['posicao_y'] == l and posicao['posicao_x'] == c and c == x-1:
                    print("🏌️")
                elif posicao['posicao_y'] == l and posicao['posicao_x'] == c:
                    print("🏌️", end="  ")
                elif c == x-1:
                    print(A[l][c])
                else:
                    print(A[l][c], end=" ")    
        
while True:
    mapa_tamanho = mapa(linhas_mapa,colunas_mapa)
    posicao = direcao(input("Escolha uma direção: (w/a/s/d)"))  
    
    if A[posicao['posicao_y']][posicao['posicao_x']] == '🟥':
        print("Que pena. Você pisou no vermelho...")
        break
    if A[posicao['posicao_y']][posicao['posicao_x']] == '🟩':
        print("Você venceu!")
        break
    


  
    

    
   