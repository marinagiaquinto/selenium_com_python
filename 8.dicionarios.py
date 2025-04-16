print('---------------------')
print('     DICIONÁRIOS     ')
print('---------------------')

#São estruturas que aglomeram outras estruturas

#Possui uma estrutura similar a um JSON. Composto por CHAVE e VALOR.
#Assim como o conjunto não é possível pegar pela posição, mas é possível pegar pelo nome

dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': {
        'outraChave1': 'outroValorDeChave1',
        'outroValorDeChave': ['valor1', 'valor2', 100]}
}


print('1. MÉTODOS')


print('')
print('1.1 [] -> Pegar o valor a partir da chave')
print(dicionario['chave1']) #devolve o valor da chave -> 'valor1'
print(dicionario['chave3']['outraChave1']) #devolve o valor da chave -> 'outroValorDeChave1'

print('')
print('1.2  KEYS -> pegar todas as chaves')

print(dicionario.keys()) #dict_keys(['chave1', 'chave2', 'chave3'])


print('')
print('1.3 [] = -> Atribuir novos valores para a chave')  #As chaves são imutáveis mas os valores são mutáveis
dicionario['chave1']= 'teste novo valor chave1'
print(dicionario['chave1']) 


print('')
print('1.4 VALUES -> pega todos os valores')
print(dicionario.values()) #dict_values(['teste novo valor chave1', 'valor2', {'outraChave1': 'outroValorDeChave1', 'outroValorDeChave': ['valor1', 'valor2', 100]}])

print('')
print('1.5 POPITEM -> Tira um item qualquer do dicionário ou elimina por nome')

dicionario.popitem()



print('-------------------------')
print('2. Dicionário em funções')

def relatorio (objeto_dicionario):
    return f"O funcionário {objeto_dicionario['chave1']}, de CPF {objeto_dicionario['chave2']} e telefone {objeto_dicionario['chave3']['outraChave1']}, está oficialmente de férias"

print(relatorio(dicionario))
