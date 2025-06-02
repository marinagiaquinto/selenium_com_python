from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

#BUSCA ANINHADA

browser = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_04_a.html'

browser.get(url)
ul = browser.find_element(By.TAG_NAME, 'ul')
li = ul.find_elements(By.TAG_NAME, 'li')
element1= li[0].find_element(By.TAG_NAME, 'a').text
# Obs: nesse caso, print(li[0].text) teria o mesmo resultado porque o text lê tudo o que tem na tag que pedidos, não apenas o texto do elemento específico
element2 = li[1].find_element(By.TAG_NAME, 'a').text
print(element1)
print(element2)

# ----------------------------------------------

elemento_ddg = browser.find_element(By.PARTIAL_LINK_TEXT, 'Du')
print(elemento_ddg.text)   # reposta: DuckDuckGo (texto do link)

url = elemento_ddg.get_attribute("href")
print(url) # resposta: http://ddg.gg/ (link do texto)

#------------------------------------------------

elemento_href = browser.find_element(By.XPATH, '//a[@href="http://ddg.gg"]')
print(elemento_href.text) #-> resposta 'DuckDuckGo'
# // faz procurar em qualquer lugar do HTML que tenha um 'a'
# @ faz filtrar por esse href em específico

browser.quit()