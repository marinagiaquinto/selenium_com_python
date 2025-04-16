# While (Enquanto) - enquanto <tal condição> não for cumprida, siga executando o laço de repetição
# Pode sair do laço de repetição por a condição ter sido cumprida ou pelo break
# A repetição é a partir de um estado bolleano, verdadeiro ou falso


print('-' *10)
print('   Wile')
print('-' *10)

resp = input("Bora dar um rolê [s/n]: ")

n = 1

while resp != "s" and resp != "SIM" and resp != "sim":
    resp = input(f'Bora{"a" * n}?! ')
    n += 1
    if 'chato' in resp or 'chata' in resp:
        print('Foi mal!')
        break
        
    elif n == 11:
        print('Okkk')
        break

else: 
    print(f'Então bora{ "a" * n}')


#For (Para) - para cada elemento dentro de uma sequência, faça algo
# Não possui break
# Repete a partir de um interável. Para cada pedaço de coisa (ex: letra, palavra) dentro da coisa maior (ex: palavra ou frase), faça algo.

print('-' *10)
print('   For')
print('-' *10)

#ex:1
palavra = 'Python'

for letra in palavra:
    print(letra)


print('-' * 5)

#enumerate dentro do for: consegue saber cada letra e a posição delas
#ex2:
palavra = 'Python'

for posicao, letra in enumerate (palavra):
    print(posicao, letra)



print('-' * 5)

#ex3:
frase = ('Eduardo foi a feira').split()

for palavra in frase:
    print(palavra)


print('-' * 5)

#ex4: Escolha uma palavra e print seu nome entre as vogais dela

palavra = input('Escreva uma palavra: ')
vogais = 'aeiouAEIOUáéíóúÁÉÍÓÚãô'

for letra in palavra:
    if letra in vogais:
        print (letra)
        print('Marina')
    else:
        print(f'{letra} - sou uma consoante')


#ex5: receba uma string com um número de ponto flutuante e imprima qual a parte dele não é inteira

valor = input('Escreva um número decimal: ')

while ('.' not in valor) and (',' not in valor):
 valor = input('Por favor, digite um número decimal: ')

if '.' in valor:
 inteiro, decimal = valor.split('.')
elif ',' in valor:
 inteiro, decimal = valor.split(',')

print(f'A parte inteira do seu número é {inteiro} e a parte decimal é {decimal}')