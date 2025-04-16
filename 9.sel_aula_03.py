from selenium.webdriver import Firefox # o código chama a biblioteca selenium e ele chama o módulo webdriver que chama o firefox
from selenium.webdriver.common.by import By 


#abrir navegador
navegador = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador.get(url)
navegador.implicitly_wait(3)

a = navegador.find_element(By.TAG_NAME, 'a')
navegador.find_elements

for click in range(11):
    p = navegador.find_elements(By.TAG_NAME, 'p') 
        #find_element pega apenas o valor único. find_elements faz uma lista com os valores daquele elemento -> print(type(p)) mostra que é uma lista e print(len(p)) mostra a quantidade de itens na lista
        #find.element é um método genérico para encontrar um elemento único
        # By é uma classe importada do Selenium a partir da qual se define como quer localizar o elemento
        # Primeiro argumento do find.element -> é o tipo do localizador (By.CLASS_NAME, By.ID, By.TAG_NAME, etc)
        # Segundo argumento do find.element -> é o valor correspondente
        # está dentro do for para "p" ficar sempre com o valor da lista atualizada pós acréscimo de um novo valor

    a.click()
    print(f'Último valor de {p[-1].text} e o valor do click {click}')
    print(f'Os valores são iguais? {p[-1].text == str(click)} ')
    print('')


#fechar navegador
navegador.quit()
