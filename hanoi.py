"""
trabalho torre de hanoi
-------------
*Somente um disco pode mover de cada vez.

*Cada movimento consiste em retirar o disco do topo de uma das torres e
mover para outra.

*Nenhum disco pode ficar em cima de um disco menor.
------------------------
Implemente algoritmos de busca sem informacao para encontrar uma solucao
para este problema. O programa devera receber o numero de discos como entrada
e imprimir os passos a serem executados para obter a solcao.
Os seguintes algoritmos devem ser implementados:
------------------
• Busca em largura
• Busca em profundidade
• Busca de custo uniforme

 inves de arvore usa-se pilhas eu vai descolando, no abc, torre de hanoi
 --------------------------------------------------
"""

class Noh:

#Classe para representar  um noh

#construtor
  def __init__(self,dado =0, prox_noh=None):
    self.dado = dado
    self.prox = prox_noh

#mostra dados
  def __repr__(self):
    return '%s -> %s' % (self.dado,self.prox)
#-----------------------------------

class Fila:
#usando os nohs , representa uma fila encadeada

# construtor da fila
  def __init__(self):
    self.pri = None
    self.ult = None
    self.n_nohs =0

#mostra dados
  def __repr__(self):
    return"[" + str(self.pri) + "]"

# função de insercao na fila
  def inserir(self,novo_dado):
#insere um novo com o dado novo recebido      
    novo_noh = Noh(novo_dado)      
#insere em uma fila vazia caso seja o primeiro
    if self.pri == None:
      self.pri = novo_noh
      self.ult = novo_noh
    else:
# insere no final caso ja exista
      self.ult.prox = novo_noh
# o ultimo, faz referencia ao novo
      self.ult.prox = novo_noh
      self.n_nohs +=1
#Funcao de remocao da fila
  def remover(self):
    assert self. pri != None , "Fila está vazia"
# atualiza na fila     
    self.pri = self.pri.prox
    self.n_nohs -=1
# se a lista ficou vazia      
    if self.pri == None:
      self.ult = None
#---------------------------------------



# funcao que simula torre de hanoi
def move_torre(altura,poste_origem, poste_destino, com_poste):
  if altura >= 1 :
    move_torre(altura - 1,poste_origem, poste_destino, com_poste)
    print("mover do poste ",poste_origem,"para: ",poste_destino,":",altura)
    return "mover do poste ",poste_origem,"para: ",poste_destino,":",altura
    move_torre(altura - 1,com_poste,poste_destino,poste_origem)

#--------------------------
# salva o resultado na Fila
fila = Fila()
fila1 = Fila()
print("Fila vazia por hora")


# iniucaliza torre de hanoi 
alt = 4    
    
while alt >1:
  fila.inserir(move_torre(alt,"A","B","C"))
  alt -= 1
  
print("--------|||-----------------------")

# busca em largura
#executar a busca por largura nessa fila
while fila.n_nohs !=0:
    print(fila.remover())
    if fila.n_nohs < alt:
        z = fila.n_nohs - alt
        while z > 1:
          fila1.inserir(fila.remover())
          print("nohs nao visitados",fila1.n_nohs)
    

#------------------------------------------------------------
alt = 5    
    
while alt >1:
  fila.inserir(move_torre(alt,"A","B","C"))
  alt -= 1
  
print("--------|||-----------------------")
          
# busca em profundidade
# fazendo buscas em profundidade
fila2 = Fila()

z = fila.n_nohs
x = z-1

while z != fila.n_nohs:
  if x < alt:
    fila2.inserir(fila.remover)
    print("remove itens ja visitados")
    x -=1
  z -=1

print("--_______----_____-----")



#busca uniforme
#ordenar a lista
fila3 =  sorted(fila)
#lista está vazia
if lista3 == None:
    print("lista vazia")

#pega a quantidade de nohs
d = fila3.n_nohs_nohs-1;
#percore a lista
while d != 0:
#remove o noh
  print("valor retornado",fila.remover)
# ordena a lista novamente
  fila3 = sorted(fila3)
#diminui o contador  
  d-= 1


# busca largura fila
# busca profundidade pilha
# busca uniforme fila ordenada.

