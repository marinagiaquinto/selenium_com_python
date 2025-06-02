from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_05_c.html'

browser.get(url)

def form_melhor_filme(filme, email, telefone):

    browser.find_element(By.NAME, 'filme').send_keys(filme) #Como o type em cypress, escreve o texto
    browser.find_element(By.NAME, 'email').send_keys(email)
    browser.find_element(By.NAME, 'telefone').send_keys(telefone)
    browser.find_element(By.NAME, 'enviar').click()

form_melhor_filme('Teste melhor filme', 'testemail@gmail.com','011 998562356')

browser.quit()