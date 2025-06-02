from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_09.html'

browser.get(url)


class EsperarElementoNotClick:
    def __init__(self, locator):
        self.locator = locator
    def __call__(self, browser):
        elementos = browser.find_elements(*self.locator)
        if elementos:
            return 'unclick' in elementos[0].get_attribute('class')
        return False


def esperar_elemento(by, elemento, browser):
    if browser.find_elements(by, elemento):
        return True
    return False


wdw = WebDriverWait(browser, 10)

wdw.until_not(EsperarElementoNotClick(locator=(By.CSS_SELECTOR, 'button')), 'Botão não apareceu')
browser.find_element(By.CSS_SELECTOR, 'button').click()


wdw.until(
    partial(esperar_elemento, 'id', 'finished'),
    'A mensagem de sucesso não apareceu'
)

sucesso = browser.find_element(By.ID, 'finished')
assert sucesso.text == 'Carregamento concluído'