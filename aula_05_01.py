from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from pprint import pprint

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_05_b.html'

browser.get(url)


#Pegar valores da classe 'linguagens'em um dicionário
dicionario_linguagens = {}

lista_linguagens = browser.find_elements(By.CLASS_NAME, 'linguagens')
print(lista_linguagens[0].text)

for linguagem in lista_linguagens:
    dicionario_linguagens[linguagem.find_element(By.TAG_NAME, 'h2').text] = linguagem.find_element(By.TAG_NAME, 'p').text

pprint(dicionario_linguagens)



#Pegar valores da classe 'linguagens'em uma tupla
for linguagem in lista_linguagens:
    print(
        (
            linguagem.find_element(By.TAG_NAME, 'h2').text,
            linguagem.find_element(By.TAG_NAME, 'p').text
        )
    )


browser.quit()