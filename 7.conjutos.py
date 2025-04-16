
print('---------------------')
print('      CONJUNTOS      ')
print('---------------------')


print('1.Conjuntos e dicionários NÃO posuem posições')
# Conjuntos e dicionários possuem um outro tipo de estrutura que impede pegar "posições" como acontece em listas e tuplas
# Sua estrutura é por árvore e, assim sendo, pode ter mais de um elemento na posição seguinte, 
# o que nos impede de pegar elementos por posições.


#ex da estrutura de LISTA e TUPLA:

    #elemento 1 -> elemento 2 -> elemento 3 -> elemento 4 -> elemento 5 ...


#ex da estrutura de um CONJUNTO e DICIONÁRIO:

                    #elemento 1
        #elemento 2             elemento 3
#elemento 4  elemento 5     elemento6  elemento 7


print('2. Conjuntos e cicionários são conjunto de dados IMUTÁVEIS, como nas tuplas')


print('3. Conjuntos são como conjuntos matemáticos e sofrer funções de união, interseção, etc')


x = {1,2,3}
y = {3,4,5}

print('3.1 UNION -> cria um novo grupo unindo os 2 gurpos e descartando a duplicidade de argumentos em comum entre os grupos')
print(x.union(y))  # {1,2,3,4,5}

print('3.2 INTERSECTION -> pega só o valor em comum entre os grupos')
print(x.intersection(y)) # {3}


print('3.3 DIFFERENCE -> pega a diferença de um grupo em relação ao outro')
print(x.difference(y)) #{1,2} -> diferença de x em relação a y. Portanto, considera apenas os valores de x.
print(y.difference(x)) #{4,5} -> diferença de y em relação a x. Portanto, considera apenas os valores de y.

print('3.4 UPDATE -> pega tudo que tem em um grupo e traz pra dentro do outro conjunto')
x = {1,2,3}
y = {3,4,5}
x.update(y)
print(x) #{1,2,3,4,5} -> traz o y pra dentro do x
y.update(x)
print(y) #{1,2,3,4,5} -> traz o x pra dentro do y

print('3.5 DISCARD -> dicard um elemento considerando seu valor')
x = {1,2,3}
x.discard(1)
print(x)  #{2,3}

print('3.6 POP -> retira o primeiro argumento do grupo')
x = {1,2,3}
x.pop()
print(x) #{2,3}
         # o pop em lista tirava apenas o último. Porém, isso não ocorre aqui, dado que conjuntos não são sequênciais 

print('4. Não existe valor repetido em um mesmo conjunto -> SET (conjunto)') #Por princípio matemático

conjunto = {'Eduardo', 'Eduardo', 'Eduardo'}
print(conjunto) #Resultado -> {'Eduardo'}

lista = [1,1,1,1,1,1,1,1,25,25,25,25,648,45,78,78,15,78,1,1]
print(set(lista)) #{1, 648, 45, 78, 15, 25}
                  #Por esse princípio, ao transformar uma lista em um conjunto, retira-se a duplicidade dos valores

lista = [1,1,1,1,1,1,1,1,25,25,25,25,648,45,78,78,15,78,1,1]                  
print(list(set(lista))) #se desejar voltar o valor pra lista de novo [1, 648, 45, 78, 15, 25]

lista = [1,1,1,1,1,1,1,1,25,25,25,25,648,45,78,78,15,78,1,1]   
print(tuple(set(lista))) #se desejar transformar o valor em tupla pós alteração (1, 648, 45, 78, 15, 25)

