from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

print('Ex 1 -> Gere um dicionário, onde a chave é a tag h1 e o valor deve ser um novo dicionário')

drive = Firefox()
url ='https://curso-python-selenium.netlify.app/exercicio_01.html'

drive.get(url)
drive.implicitly_wait(3)

h1 = drive.find_element(By.TAG_NAME, 'h1')
value_h1 = h1.text
print(value_h1)

t1 = drive.find_element(By.CSS_SELECTOR,'p[atributo="texto1"]')
value_text1 = t1.text

t2 = drive.find_element(By.CSS_SELECTOR,'p[atributo="texto2"]')
value_text2 = t2.text

t3 = drive.find_element(By.CSS_SELECTOR,'p[atributo="texto3"]')
value_text3 = t3.text


dicionario_ex1 = {
    'h1' : 'value_text1',
    'atributos' : {
        'texto1': value_text1, 
        'texto2': value_text2, 
        'texto3': value_text3}
}

print(dicionario_ex1)





print('------------')
print('Ex2: ')

url ='https://curso-python-selenium.netlify.app/exercicio_02.html'

drive.get(url)
drive.implicitly_wait(3)

id_clique_aqui = drive.find_element(By.ID, 'ancora')
elemento_anterior = id_clique_aqui.find_element(By.XPATH, "preceding-sibling::*[1]")
            # "preceding-sibling::*[1]" -> pega o irmão anterior imediato, não importa a tag
            # "preceding-sibling::p[1]" -> pega o irmão anterior da tag especificada
text_elemento_anterior = elemento_anterior.text
texto, numero_esperado = text_elemento_anterior.split(':')

ultimo_valor_da_lista_do_elemento_posterior = ''

while 'Você ganhou' not in ultimo_valor_da_lista_do_elemento_posterior:
    id_clique_aqui.click()
    elemento_posterior = id_clique_aqui.find_elements(By.XPATH, "following-sibling::*") #"following-sibling::*" -> pega o irmão posterior imediato, não importa a tag
    ultimo_valor_da_lista_do_elemento_posterior = elemento_posterior[-1].text


drive.quit()