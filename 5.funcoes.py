print('-'*12)
print('  FUNÇÕES  ')
print('-'*12)

#Funções nomeadas
#Funções são blocos de código que são utilizados para o código não ficar repetitivo.

"""
def -> define, definir
nome -> nome do bloco de código
parâmetro -> é uma variável que é definida na função, REPRESENTANDO o valor que a função deve receber
argumento -> valor que é passado para a variável (parâmetros), dutante a chamada da função
return -> o que ela deve retornar

def nome_funcao (parmetro1, parametro2):
    return

"""

print('ex:1 - Diferença entre parâmetros e argumentos')
print('')

def nome_funcao (parametro1, parametro2):
    return f'Função é um bloco de código reutilizável conforme a passagem de valores \n(argumentos) para a função (ex:{parametro1} e {parametro2}). '


print(nome_funcao('argumento 1', 'argumento 2'))


#-----------------------------------------------------------------
print('---------------------------------')
print('ex:2 - Cálculo da média')
print('')

def media (lista_de_numeros):
    soma =  sum (lista_de_numeros) 
    qtd = len (lista_de_numeros)
    media_result = soma/qtd
    return f'A média da lista é feita por {soma}/{qtd} e seu resultado é {media_result}'

print(media([2,4,6,10]))


#-----------------------------------------------------------------
print('---------------------------------')
print('Tipos de Argumentos')
print('')


print('1. Argumento posicional -> identifica o argumento pela posição passada na função')

def relatorio (nome,cpf,telefone):
    return f'O funcionário {nome}, de CPF {cpf} e telefone {telefone}, está oficialmente de férias'

print(relatorio('Joilson', '371.458.956-78','5511998562456'))



print('------------')
print('2. Argumento nomeado -> identifica o valor pela nomeação do parâmentro')

def relatorio (nome,cpf,telefone):
    return f'O funcionário {nome}, de CPF {cpf} e telefone {telefone}, está oficialmente de férias'

print(relatorio(telefone='5511998562456', nome='Joilson', cpf='371.458.956-78',))



print('---')
print('2.1 Argumento nomeado com valor default')

def relatorio (nome='SEM NOME',cpf='SEM CPF',telefone='SEM TELEFONE'):
    return f'O funcionário {nome}, de CPF {cpf} e telefone {telefone}, está oficialmente de férias.'

print(relatorio()) # se não passar o valor, utiliza o valor default
print(relatorio(cpf='371.458.956-78')) #se passar o valor, utilizar o valor passado



print('------------')
print('3. Pacote de Argumentos - empacota com * desenpacote tirando o * . Origina uma tupla ()')

def relatorio (nome, *pacode_de_argumentos):
    print(nome, pacode_de_argumentos) #cria uma tupla. Como a lista, a tupla também é  um container. Uma "coisa" que contém outras "coisas" dentro.


relatorio('Python', 1,2,3,4,5) # resultado -> Python (1, 2, 3, 4, 5)



print('------------')
print('4. Dicionário de Argumentos - empacota com ** desenpacote tirando o ** . Origina um dicionário {}')

def relatorio (nome, **pacode_de_argumentos):
    print(nome, pacode_de_argumentos) #cria um dicionário. Como a lista e a tupla, o dicionário também é  um container.


relatorio('Python') # resultado -> Python {}

print('---')
print('4.1 Valor adicionado no dicionário a partir de uma nomeação de argumento')

relatorio('Jéssica', parametro_nomeado_nao_existente='1', parametro_nomeado_nao_existente_2='2' ) 
#adiciona o valor no dicionário -> Jéssica {'parametro_nomeado_nao_existente': '1', 'parametro_nomeado_nao_existente_2': '2'}