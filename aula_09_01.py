from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_09_a.html'

browser.get(url)

# Espera implícita:
# Espera por um tempo determinadao, independente do que ocorra na pág nesse tempo. 

# Espera explícita:
# Espera por um elemento e/ou ação específica. 

"""
1. webDriverWait


wdw = webDriverWait(
    driver, # webdriver
    timout, # tempo em segundos que de espera até o erro
    poll_frequency=0.5, # Opcional: tempo entre uma tentativa e outra
    ignored_exceptions=None # Opcional: lista de coisas que se deve ignorar
)

"""



"""
2. Método until

wdw.until(
    callable, # "Chamável", operação que deve ser executada. Essa função é que vai ser chamada no tempo do pool pra ver se o elemento já está pronto (0.5 segundos).
    mensage # mensagem caso o erro ocorra
) # Faz o pool até retornar "true"

OU 

wdw.until_not(
    callable, 
    mensage
) # Faz o pool até retornar False.
"""


"""
3. Código sem reutilização da função de espera


wdw = WebDriverWait(browser, 10)

def esperar_botao(browser):

    elements = browser.find_elements(By.CSS_SELECTOR, 'button')
    return bool(elements)
    # Não existe uma lista de botões a serem salvos. Porém, foi chamado o elementS 
    # porque o seu return bool retorna FALSE ou TRUE. Que é justamente o que precisamos, 
    # saber se o elemento botão apareceu ou não na tela. 
    # Uma lista fazia retorna False, uma lista com qualquer elemento, retorna True

wdw.until(esperar_botao, 'Botão não localizado')
browser.find_element(By.ID, 'request').click()



def esperar_barra_carregamento(browser):
    elements2 = browser.find_elements(By.ID, 'finished')
    return bool(elements2)

wdw.until(esperar_barra_carregamento, 'Barra de carregamento não foi finalizada')
assert browser.find_element(By.ID, 'finished').text == 'Carregamento concluído' , 'Mensagem de conclusão do carregamento não foi apresentada'


browser.quit()
"""

"""
4. REUTILIZANDO A FUNÇÃO de espera COM PARTIAL

# O parcial cria uma função intermediária do elemento que queremos, já que 
# as funções passadas no until só aceitam browser (não aceitam o elemento) 
# e é preciso passar o elemento e o By para tornar a função reutiliável.

wdw = WebDriverWait(browser, 10)

def esperar_elemento(by, elemento, browser):

    elements = browser.find_elements(by, elemento)
    return bool(elements)

esperar_botao_2 = partial(esperar_elemento, By.CSS_SELECTOR, 'button')
wdw.until(esperar_botao_2, 'Botão não localizado')
browser.find_element(By.ID, 'request').click()

esperar_barra_carregamento_2 = partial(esperar_elemento, By.ID, 'finished')
wdw.until(esperar_barra_carregamento_2, 'Barra de carregamento não foi finalizada')
assert browser.find_element(By.ID, 'finished').text == 'Carregamento concluído' , 'Mensagem de conclusão do carregamento não foi apresentada'

"""

# 5. Reutilizando a função de espera usando classe (Orientação prog. a objeto)

# O _call_ evita o uso do partial

class EsperarElemento:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, browser):
        if browser.find_elements(*self.locator):
         return True
        return False
    
wdw = WebDriverWait(browser, 10)

locator_button = (By.CSS_SELECTOR, 'button')
locator_finished = (By.ID, 'finished')

wdw.until(EsperarElemento(locator_button),'Botão não localizado')
browser.find_element(By.CSS_SELECTOR, 'button').click()

wdw.until(EsperarElemento(locator_finished), 'Barra de carregamento não foi finalizada')
assert browser.find_element(By.ID, 'finished').text == 'Carregamento concluído' , 'Mensagem de conclusão do carregamento não foi apresentada'