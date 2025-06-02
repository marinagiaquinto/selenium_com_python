from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import time

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_07_d.html'

browser.get(url)

# EVENTOS

# Eventos são a parte dinâmica da página. 
# Quando se coloca um evento no elemento, o evento fica ouvindo e aguardando a intereção de algum tipo (um clique, dois cliques, mouse ouver, arrastar elementos, etc.)
# com o elemento em questão. Quando a interação determinada ocorre, desencadeia uma mudança de estado no próprio elemento ou em outro elemento do DOM. Seja no texto, seja no CSS, etc. 
# Ou seja, uma ação é ouvida por quem carrega esse evento e ele desencadeia a alteração do estado do elemento, dando dinamismo para a página (até aqui, estática)


# Um elemento pode ter nenhum, um ou mais eventos.

# Eventos : Focus e Blur
# Quando um evento é "acessado" (ex: caixa de texto é clicada) ele está em foco. Com isso, 
# o evento "FOCUS" é disparado (podendo, por exemplo, alterar a cor das bordas da caixa de texto).
# Quando o elemento perde o foco, o evento "BLUR" é desencadeado (fazendo, por exemplo, 
# que a cor da borda volte ao estado anterior ao de focus)

# Evento: Change
# Quando previsto, ocorre junto ao evento de Blur.
# Quando o elemento perde o foco (ou seja, quando dispara o evento de Blur), o elemento será analisado e
# caso ele tenha sofrido alguma mudança durante o período de foco (ex: foi escrito um texto no campo),
# ele será disparado. 
# O evento de change expressa que o elemento sofre alguma mudança (ao que parece, desencadeada pelo usuário)

#Exercício 1: verificar se a mudança ocorre no span 
# Span é o elemento do DOM que sofrerá alteração frente aos eventos de focus e blur que "escuta" o clique no campo de texto

browser.find_element(By.TAG_NAME, 'input').click()
texto_span_focus = browser.find_element(By.TAG_NAME, 'span').text
assert texto_span_focus == 'está com foco', 'Texto apresentado SE a verificação der erro'

browser.find_element(By.TAG_NAME, 'span').click()
texto_span_blur = browser.find_element(By.TAG_NAME, 'span').text
assert texto_span_blur == 'está sem foco', 'A mensagem "está em foco" não foi apresentada'

#Exercício 2: verificar se as alterações no campo texto elevam a contagem do pelemento p

valor_de_p = browser.find_element(By.TAG_NAME, 'p').text
assert valor_de_p == '0', 'O valor de p não é igual a zero'

browser.find_element(By.TAG_NAME, 'input').send_keys('alteração no campo')
browser.find_element(By.TAG_NAME, 'span').click()  # O evento change só acontece com a verificação do Blur (retirada do focus)
valor_de_p = browser.find_element(By.TAG_NAME, 'p').text
assert valor_de_p == '1', 'O valor de p não é igual a um'

browser.find_element(By.TAG_NAME, 'input').clear()
browser.find_element(By.TAG_NAME, 'span').click()
valor_de_p = browser.find_element(By.TAG_NAME, 'p').text
assert valor_de_p == '2', 'O valor de p não é igual a dois'

browser.quit()