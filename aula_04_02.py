from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from urllib.parse import urlparse

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_04_b.html'

browser.get(url)

print(' --- NAVEGAÇÃO --- ')

print('1. ALTERAÇÃO DE PÁGINA-> para trás e para frente')

# Quando você está em uma página e muda para outra, o navegador mantém o histórico da quela janela no browser (que ´o que permite retornar a pág anterior)
# O armazenamento das páginas é por pilha, sendo zero sempre a última pág acessada

# Ex:

# Pág DuckduckGo 
# 0 -> DuckduckGo

# Pág DuckduckGo -> Pág Reddit -> Pág FSF
# 2 -> DuckduckGo
# 1 -> Reddit
# 0 -> FSF


# Se está na pág 0 (FSF) e der um:
#  browser.back() -> volta para a pág anterior (Reddit)

# Se estiver em uma pág anterior (Reddit) e de um:
# browser.forward() -> volta para a página seguinte (FSF)

# ATENÇÃO: não é feita uma nova requisição para retornar ou avançar de pág. 
# É como se tirassem um print do último estado da página e é pra ele que retornarmos
# Portanto, ao retornar para págs, ela terá os últimos caches e estados anteriormante utilizados.


for Id in ['box-1', 'box-2', 'box-3', 'box-4']:
    browser.find_element(By.ID, Id).click()

# box-1 posição 3 na pilha -> box-2 na 2 -> box-3 na 1 e box-1 na 0

browser.back() #retorna para box-3
browser.back() #retorna para box-2
browser.back() #retorna para box-1

browser.forward() #retorna para o box-2

#-------------------------------------------------------

print('')
print('2. EXTRAÇÃO DA URL Corrente')

parseResult = urlparse(browser.current_url)
#ParseResult(scheme='https', netloc='curso-python-selenium.netlify.app', path='/selected=box-2', params='', query='', fragment='')

print(parseResult)
print(parseResult.path)


#------------------------------------------------
print('')
print('3. NOME contido na aba da pág')

print(browser.title)


browser.quit()