from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_05.html'

browser.get(url)

# Forms
# 3 principais tags
# target (redirecionamento da página) -> self(abre na mesma janela) ou blank(abre outra janela)
# method (a forma como envia a informação)-> get(se envia as informações na url) ou post(envia dentro da requisição da web)
# action (onde será feita a request)-> URL (request em outras urls) ou #(request para a mesma página)

sleep(1)
def form(nome, email, senha, telefone):
    browser.find_element(By.NAME, 'nome').send_keys(nome)
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'senha').send_keys(senha)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'btn').click()


estrutura = {
    'nome': 'Marina',
    'email': 'marina@gmail.com',
    'senha': '123456',
    'telefone': '14998564555'
}

form(**estrutura)

url_parseada = urlparse(browser.current_url)
# resultado:
# ParseResult(scheme='https', netloc='curso-python-selenium.netlify.app', 
# path='/aula_05.html', params='', query='nome=Marina&email=marina%40gmail.com&
# senha=123456&telefone=14+998564555&btn=Enviar%21', fragment='')

sleep(2)

texto_resultado = browser.find_element(By.TAG_NAME, 'textarea').text
#resultado:
#{'nome': 'Marina', 'email': 'marina@gmail.com', 'senha': '123456', 'telefone': '14998564555'}

resultado_arrumado = texto_resultado.replace('\'', "\"")
#resultado:
#transforma aspas simples em duplas dentro do json
#{"nome": "Marina", "email": "marina@gmail.com", "senha": "123456", "telefone": "14998564555"}

dic_result = loads(resultado_arrumado)
#Resultado:
# {'nome': 'Marina', 'email': 'marina@gmail.com', 'senha': '123456', 'telefone': '14998564555'}
#transforma o json em string para poder comparar com o texto

assert dic_result == estrutura
# verifica se a resposta continda no texto é igual a resposta que vem na URL formatada


browser.quit()