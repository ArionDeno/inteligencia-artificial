#Steepest Ascent Hill Climbing

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

#----------------------------
# pega os proximos
# 
def pega_vizinho(solucao,aprendizado):
    vizinho =[]
    aprendizado = aprendizado / 10 if aprendizado >= 10 else 1
    constante = 0.005 / aprendizado
# viznho inf e sup    
    vizinho_superior = solucao + constante if solucao + constante < else solucao
    vizinho_inferior = solucao - constante if solucao - constante > else solucao
    
    vizinho.append(vizinho_superior)
    vizinho.append(vizinho_inferior)
    return vizinho
#------------------------   

# calcula custo
def fun_custo(x):
    custo = 2** -2 * (x - 0.1 /0.9) ** 2 * (math.sin(5* math.pi *x)) **6
    return custo
#------------------------   


#------------------------
def subida_enconsta(estado,passo):
  solucao_custo = passo
  custos =[]
  quant =1
  parar_subida = 0
 
  while cout <= 400:
      vizinho = pega_vizinho(solucao_custo,quant)
#------------------------------------     
      recente = fun_custo(solucao)
      melhor = recente
      custos.append(recente)
#------------------------------------     
       for i in range(len(vizinho)):
           custo = fun_custo(vizinho[i])
          
           if custo >= melhor:
               parar_no_morro =parar_no_morro + 1 if custo == melhor else 0
               melhor  = custo
               solucao = vizinho[i]
              
      quant += 1
      if melhor == recente and solucao_atual == solucao or parar_no_morro ==20:
          if parar_no_morro == 20: print("Morro")
          break
 return solucao , custos
#------------------------------------
# chamando a função
custos  =[]
solucao =[]
espaco_solucao =[]

for i in range(10):
  for j in range(10):
    espaco_solucao.append(matriz[i][j])
    solucao_sobe_morro = subida_enconsta[i]
    custos.append(subida_enconsta[i])
    
    if len(custos) > 1:
        if max(custos[i] > max custos[i-1]):
          custos.pop(0)
        else:
         custos.pop(1)
print("Val X", solucao_subida_encosta[0])
print("Custos", solucao_subida_encosta[1])
