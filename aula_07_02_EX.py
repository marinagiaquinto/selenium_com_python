from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_07.html'

browser.get(url)

sleep(1)
nome_label = browser.find_element(By.ID, 'lnome').text
assert "nome:" == nome_label, 'A label do campo é diferente de "nome:" '
browser.find_element(By.ID, "nome").click()
nome_label = browser.find_element(By.ID, 'lnome').text
assert "Não vale mentir o nome" == nome_label, 'A label do campo é diferente de "Não vale mentir o nome" '

email_label = browser.find_element(By.ID, 'lemail').text
assert "email:" == email_label, 'A label do campo é diferente de "email:" '
browser.find_element(By.ID, "email").click()
email_label = browser.find_element(By.ID, 'lemail').text
assert "Esse email é mesmo válido?" == email_label, 'A label do campo é diferente de "Esse email é mesmo válido?" '

senha_label = browser.find_element(By.ID, 'lsenha').text
assert "senha:" == senha_label, 'A label do campo é diferente de "senha:" '
browser.find_element(By.ID, "senha").click()
senha_label = browser.find_element(By.ID, 'lsenha').text
assert "Já falei pra não colocar 1234" == senha_label, 'A label do campo é diferente de "Já falei pra não colocar 1234" '