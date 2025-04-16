from selenium.webdriver import Firefox
# o código chama a biblioteca selenium e ele chama o módulo webdriver que chama o firefox

#abrir navegador
navegador = Firefox()
url = 'https://curso-python-selenium.netlify.app/aula_03.html'

navegador.get(url)

#fechar navegador
#navegador.quit()
