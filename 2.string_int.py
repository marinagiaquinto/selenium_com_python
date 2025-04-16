# String

#Manipulação de string

x = 'Abracadaba'

print(x.count('a')) #conta quantas vogais 'a' tem na palavra

print(x.index('c')) #conta a posição da string 'c' na palavra

print(x.partition('c')) #divide a palavra pelo 'c' separando o antes e depois dele, e deixando ele sozinho. A resposta vem em tupla.

print(x.split('a')) #separa a palavra a cada 'a', aglutinando em lista os valores e desconsiderando seu valor

print(x.replace('a', 'c')) #transforma todos os 'a' em 'c'

print(x.lower()) #transforma tudo em minúsculo

print(x.upper()) # transforma tudo em maiúsculo

print('*' * 20)



#texto multilinhas

texto = """Teste de um texto multilinhas
Olha como ele fica printado
sem que você precise colocar '' em cada uma das frases
"""

print(texto)


#Para verificar se tem uma string específica dentro de uma frase (pertencimento)

msg = 'Eduardo foi a feira'

if 'feira' in msg:
    print('Sim, foi a feira')
else:
    print('Não foi a feira')




#ex com split

resposta = input('Qual sua data de nascimento? ')

#29/12/1987 -> com split vira [29, 12, 1987]

dia, mes, ano = resposta.split('/')
print(f'Você nasceu no dia {dia}, do mês {mes} e ano {ano}')

