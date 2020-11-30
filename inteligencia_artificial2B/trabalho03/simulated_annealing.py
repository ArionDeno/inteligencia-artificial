#Tempera Simulada (Simulated Annealing)

# matriz
matriz = []
#abre o arquivo para leitura
with open('arquivo.txt') as fp:
  linhas = fp.readlines()
  
# percorre as linhas
for linha in linhas:
  colunas = linha.split(' ')
  matriz.append([int(x) for x in colunas if x != ''])

# conveter em numero
for i, linhas in enumerate(matriz):
  for j, colunas in enumerate(linhas):
    print(matriz[i][j])



# funcao temperatura simulada
def tempe_simul(estado,temp):
    
  for x in range(len(matriz)):
    for y in range(len(matriz[0])):
   # pega a situacao de cada posicao da matriz   
      situacao = matriz[x][y]            
      for tm in range(temp,1-1):
       
          if situacao == 0:
            return "quente",estado,situacao
          #calcula delta temperatura
          delta_tp = situacao - estado
          # maior que zero atualiza aquela posicao
          if delta_tp >= 0:
            matriz[x][y] = situacao
          else:
            nu = random.randint(0,999)
            if n < math.exp(delta_tp/temp):
                   estado = situacao       
    return "ainda frio",estado

#------------------------------------------------
# chama funcao
tempe_simul(33,1000)              
                   