print('---------------------')
print('      TUPLAS         ')
print('---------------------')
# Como as listas, as tuplas também são containers. Ou seja, armazenam um conjunto de valores. 
# Porém, as tuplas são listas IMUTÁVEIS. Não é possível adicionar ou retirar valores dela.
# São usadas, portanto, quando possui um conjunto de valores fixos que deseja utilizar sem nenhuma alteração

print('1. Atribuição de Tuplas - com e sem desempacotamento')
minha_tupla = ('Jéssica', 89, 'Rua dos Tupiniquins', '850', 'Vila dos Povos Originária')

(nome, idade, *endereco) = minha_tupla

print(minha_tupla) # ('Jéssica', 89, 'Rua dos Tupiniquins', '850', 'Vila dos Povos Originária')
print(nome)
print(idade)
print(endereco) # Resulta em uma lista dos valores empacotados -> ['Rua dos Tupiniquins', '850', 'Vila dos Povos Originária']
                #Atenção: só pode correr um desenpacotamento por vez. Não é possível ter dois empacotamentos na mesma tupla

print('---------------------')
print('2. Função com tupla')

def minha_func():
    return 1,2,3

print(minha_func()) 

# Ao retornar valores separados por vírgula, a função retorna em formato de tupla (1, 2, 3)
# A vírgula é o que "define" uma tupla, não os parênteses. 
# Se quiser retornar uma lista ao invés de tupla, precisa deixar isso explícito -> return [1,2,3]


print('---------------------')
print('3. Pegar valores por posição em tuplas -> []')
# O colchete indica que você deseja pegar um valor das tuplas
# Se colocar () no index, vai dar erro porque o programa vai entender que deseja executar a tupla, como uma função.

resposta = minha_func () #sempre que precisar pegar a respota de uma função (com lista, ou tupla, ...) vai precisar guardar na variável se quiser reutilizá-la
print(resposta)
print(resposta[0])

#ou

ex_tupla = 15,6,7,8
print(ex_tupla)
print(ex_tupla[-1])



print('----')
print('3.1 Slice em tuplas')

print(resposta[1:])



print('---------------------')
print('4. Count -> contagem de quantos daquele valor existem na tupla, como na lista')

contagem = 1,2,3,1,5,6,1
print(contagem.count(1))



print('---------------------')
print('Index -> mostra a posição que o argumento ocupa na tupla, como na lista')

posicao = 5,6,7,8,9,10,11,12,13
print(posicao.index(12))