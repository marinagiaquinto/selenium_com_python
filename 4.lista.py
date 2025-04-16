print('---------------------')
print('      LISTAS         ')
print('---------------------')
#Listas são conatiners, são objetos nos quais colocamos diversos valores

print('1. Para printar cada elemento da lista: ')

lista = ['Sabão', 'Sabonete', 'Arroz', 100]
for itens in lista:
    print(itens)

#----------------------------------------------------------------------------

print('-' * 5)
print('2. Acessar uma posição específica da lista:')

print(lista[0])

#----------------------------------------------------------------------------

print('-' * 5)
print('3. Acessar o último elemento da lista [-1]: ')

print(lista[-1])

#----------------------------------------------------------------------------

print('-' * 5)
print('4. Lista dentro de lista: ')
#É possível colocar uma lista dentro de outra lista e acessar elemntos da lista interna

lista2 = [['Cebolinha', 'Pimentão', 'Abacate', 'Feijão'], ['Sabão em pó', 'Amaciante', 'Veja']]

print(lista2)
print(lista2[-1][1])

#----------------------------------------------------------------------------

print('-'*5) 
print('5. String como lista: ')
#Assim como nas listas é possível pegar a posição da letra, nas strings também é possível fazer isso. 
#Isso porque essa forma de captação dos valores funciona pra tudo que é sequêncial
print('Roberta'[2])

#----------------------------------------------------------------------------

print('-'*5)
print('6. Slices (fatias): ')

n = [0,1,2,3,4,5,6,7,8,9]
lista = ['abacate', 'melancia', 'morando', 'caqui', 'jaca', 'uva']

print(' 6:  -> do sexto elemento pra frente (INICIANDO A CONTAGEM DO ZERO)')
print(n[6:]) # =>6
print(lista[1:])
print('')

print(' :-6 -> do sexto elemento pra frente, iniciando pelo final da lista (INICIANDO A CONTAGEM EM UM)')
print(n[:-6]) #=<6
print(lista[:-2])
print('')

print('de onde: até onde: de quanto em quanto') 
print(n[1:8:2])
print(lista[0:4:3])

print('Eduardo'[::-1]) #nome inteiro de traz pra frente

print('')
#----------------------------------------------------------------------------

print('-'*5)
print(' 7. MÉTODOS em Lista ')

lista3 = ['abacate', 'melancia', 'morando', 'caqui', 'jaca', 'uva', 'uva']

print('7.1.Append -> acrescenta o valor no final da lista')
# é uma FILA, ou seja, insere sempre no último
lista3.append('banana')
print(lista3)
print('')


print('7.2.Insert -> passa qual posição e o elemento a ser adicionado') 
# é uma LISTA, ou seja, pode inserir em qualquer posição
lista3.insert(2,'melão')
print(lista3)
print('')


print('7.3.Remove -> retira um elemento passando o nome do seu valor')

lista3.remove('banana')
print(lista3)
print('')


print('7.4.Pop -> remove através do índice')
# é uma PILHA, retira o último quando não passa nenhum valor
lista3.pop(0)
print(lista3)

lista3.pop() # quando não define posição nenhuma, ele retira o último da lista
print('')

print('7.5.Reverse -> inverte os valores da lista')

lista3.reverse()
print('')


print('7.6.Count -> conta quantos elementos existem na lista com aquele valor')

n3 = n.count(3)
print (n3)
qtdUva = lista3.count('uva')
print(qtdUva)
print('')

#----------------------------------------------------------------------------
print('-' * 5)
print('8. Ex1 - criar uma lista de comprar interando os valores pedidos')

lista_de_compra = []
resposta = ''

while resposta != 'acabou':

    resposta = input('O que devo trazer do mercado? ')

    if resposta != 'acabou':
        lista_de_compra.append(resposta)
    else:
        print(lista_de_compra)


print('')
print('9. Ex2: criar uma tabuada com o valor inserido pelo usuário, sendo os números de base multiplicadores, uma lista')

base = [1,2,3,4,5,6,7,8,9,10]
i=1
resposta = int(input('Insira um número: '))

while i <= 9:
    multiplicacao = base[i] * resposta
    print (f'{i}x{resposta} = {multiplicacao}')
    i+=1


"""poderia ser também:

for numero in base:
    print (f'{numero}x{resposta} = {numero*resposta}')

"""

print('')
print('10. Ex3: faça um programa que dada a entrada de uma lista, ele faça o cálculo acumulativo da mesma')

resposta = int(1)
soma = int(0)
lista_input = []
lista_soma = []

while resposta != 0:

    resposta = int(input('Insira um valor inteiro ou digite 0 para parar o programa: '))
    lista_input.append(resposta)
    print(f'Valores iniciais: {lista_input}')
    soma = soma + lista_input[-1]
    lista_soma.append(soma)
    print(f'Resultados da somatória: {lista_soma}')