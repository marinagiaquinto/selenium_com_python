from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
from urllib.parse import urlparse

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_04.html'

browser.get(url)

# EX1
print('1. Pegar todos os links de aulas ') 
sleep(2)
aside = browser.find_element(By.TAG_NAME, 'aside') #vai salvar os elementos dentro da tag aside
aside_ancora = aside.find_elements(By.TAG_NAME, 'a') #dentro do aside, vai retornar uma lista com todos os 'a', tag dentro do aside que contém os links

for ancora in aside_ancora:
    print(ancora.text, ancora.get_attribute('href'))
    #para cada 'a', na lista de ancoras dentro do aside, vai printar o valor

print('----------------------')
print('Para transformar em um dicionário com um print ordenado:')
resultado_1 = {}
for ancora in aside_ancora:
    resultado_1[ancora.text] = ancora.get_attribute('href')
pprint(resultado_1)

print('----------------------')
print('Para clicar em uma aula específica em um dicionário')
browser.get(resultado_1['Aula 4'])

#Ex2
print('2. Navegar até o exercício 3')

main = browser.find_element(By.TAG_NAME, 'main')
lista_ancora = main.find_elements(By.TAG_NAME, 'a')
resultado_2 = {}

for ancora_main in lista_ancora:
    resultado_2[ancora_main.text]= ancora_main.get_attribute('href')
pprint(resultado_2)

browser.get(resultado_2['Exercício 3'])

#Ex3
# Jogo - pág 1
comecar = browser.find_element(By.LINK_TEXT, 'Começar por aqui').click()

main = browser.find_element(By.ID, 'main')
lista_a = main.find_elements(By.TAG_NAME, 'a')


# Função p/ - pág 1 e 2
def atributo_certo(valor_atributo):
    sleep(3)
    main = browser.find_element(By.ID, 'main')
    lista_a = main.find_elements(By.TAG_NAME, 'a')
    for itens in lista_a:
        atributo = itens.get_attribute('attr')
        if atributo == valor_atributo:
            itens.click()
            break

# Pág 1
atributo_certo('errado') 
# Pág 2
atributo_certo('certo')

# Pág 3
path = urlparse(browser.current_url).path
vazio, path = path.split('/')
print(path)

main = browser.find_element(By.ID, 'main')
lista_a = main.find_elements(By.TAG_NAME, 'a')

for caminho in lista_a:
    texto_do_link = caminho.text
    print(texto_do_link)
    if texto_do_link == path:
        caminho.click()
        break



browser.quit()