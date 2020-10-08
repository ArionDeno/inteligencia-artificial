#!/usr/bin/env python3
from pprint import pprint

with open('maze01.txt') as fp:
    dados = fp.readlines()

pprint(dados)

labirinto = []

for linha in dados:
    aux = []
    for coluna in linha.strip():
        if coluna == ' ':
            aux.append(0)
        elif coluna == 'E':
            aux.append(1)
        elif coluna == 'S':
            aux.append(2)
        else:
            aux.append(9)
    labirinto.append(aux)

for i, linha in enumerate(labirinto):
    for j, coluna in enumerate(linha):
        print(coluna, end='')
    print()

print(labirinto[1][0])

#--------------------


# busca gulosa

def busca_dolab(lab, lin_i,col_i):
    # o numero 9 faz papel da parede
    if lab[lin_i][col_i] == 9:
        return False
   # 5 será o lugar onde já foi tentando 
    if lab[lin_i][col_i] != 5: 
        return False
   #atualiza o labirinto
        lab[lin_i][col_i] =5:
# se não está EM uma parede      
    if lab[lin_i][col_i] != 9:
  # atualiza co 3 que é pra indicar parte do caminho      
        lab[lin_i][col_i] =5:
   # busca recursivamente     
     achar = busca_dolab(lab, lin_i-1,col_i) or \  
             busca_dolab(lab, lin_i+1,col_i) or \
             busca_dolab(lab, lin_i,col_i -1) or \
             busca_dolab(lab, lin_i,col_i +1) or \
    
    if achar:
   # marca o caminho     
        lab[lin_i][col_i] =3:
    else:
     # marca como parede   
        lab[lin_i][col_i] =9:
    return achar


# acha o labirinto
busca_dolab(labirinto, [1],[0])


# imprime for i, linha in enumerate(labirinto):
    for j, coluna in enumerate(linha):
        print(coluna, end='')
    print()

print(labirinto[1][0])

# A*

def a_estrela(lab, ini,fim)
  i = ini
  j = fim
  per = 1
  lab_percorr = []
  lab_percorr[1] =0
#enquanto não ahca o fim
  while lab[i][j] != 2 :
  # salva o noh percorrido com menor valor
    if lab[i][j] < lab_percorr[per]:
       # recebe o menor 
        lab_percorr.append(lab[i][j])
      #remove o noh anigo  
        lab.[i][j].remove()
        
     #se chegou ao fim
     if lab[i][j] == 2:
         print("fim do albirinto")
  #incrementa as variavies    
    i+= 1     
    j+= 1
  
  # percorre a lista
  for z in lab_percorr:
      #calcula a disntancia
      g = lab_percorr[z] + (lab_percorr[z] - lab_percorr[z+1])
      # se a dist for maior que o estado atual
      if g > lab_percorr[z] :
      #continua o laço    
          continue
      else
          lab_percorr.append(g)
     #imprime os dados     
      print(lab_percorr[z]) 


a_estrela(labirinto 1,2)    
    
    









