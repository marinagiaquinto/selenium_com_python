# Selenium com python

Curso oferecido pelo youtube pelo Eduardo Mendes: 
https://www.youtube.com/watch?v=PHHXksljGNA&list=PLOQgLBuj2-3LqnMYKZZgzeC7CKCPF375B 

## I. Instalação do Python no Ubuntu:

pyenv -> https://github.com/pyenv/pyenv?tab=readme-ov-file#installation 

1. Instalação de dependências: 

sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

2. git clone https://github.com/pyenv/pyenv.git ~/.pyenv

3. echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc

4. pyenv (para conferir se instalou corretamente)

5. Conferir se já tem o python na versão correta: python3 --version 

6. Caso tenha versões a baixo de 3.8, instalar pyenv install 3.8.2 ou 3.8.10


## II. Instalação dos Navegadores e Webdrivers:

**Webdrive** -> servidor web que fica na sua máquina e que faz com que o Selenium consiga conectar com seu browser. 
Caso não tenha os navegadores na sua máquina, será necessário intalar. Caso já possua, instale apenas os webdrives.

### II.a - Google-Chrome

1. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
2. sudo apt -y install ./google-chrome-stable_current_amd64.deb
3. google-chrome  -> deve abrir o browser. 
     3.1 Vá em três pontinhos > ajuda > Sobre o google chrome pra conferir a versão de instalação
     3.2 nessa mesma aba de navegador (Linux, se estiver com o wsl), entrar em https://googlechromelabs.github.io/chrome-for-testing/
     3.3 copiar o link da versão do webdrive compatível a versão baixada do navegador e colar na aba desse mesmo navegador

4. após o download do webdrive
    4.1 ir até da pasta de download (linux)
    4.2 unzip <nome do arquivo>
    4.3 cd <nome da pasta>
    4.4 sudo cp chromedriver /usr/local/bin   -> para alterar o arquivo de pasta
    4.5 dar cd .. 2x pra chegar até a raiz "$"
    4.6 chromedriver  -> deve responder com Starting ChromeDriver ... quer dizer que está ok.



### II.b - Firefox

1. sudo apt install firefox
2. firefox
   2.1 verificar a versão instalada
   2.2 acessar https://github.com/mozilla/geckodriver/releases 
   2.3 baixar a versão do geckodriver compatível a versão do navegador (no firefoz aberto no linux, caso esteja no wsl) -> https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html

3. após o download do webdrive
   3.1 obs: usada aqui: geckodriver-v0.36.0-linux64.tar.gz
   3.2 tar xvvf geckodriver-v0.36.0-linux64.tar.gz
   3.3 sudo cp geckodriver /usr/local/bin
   3.4 geckodriver -> fica só com o nome, sem erros e sem resposta de sucesso, mas quer dizer que está ok

   


## III. Instalação do plugin "PlatformIO IDE" no Vscode. 
    Com ctrl + '  -> abre o terminal


## IV. Instalação do Docker

//verificar se já tem o Docker na máquina
docker -version                 
docker-compose --version

sudo docker run hello-world  //pra ver se o Docker está ok

sudo docker ps //pra ver o container de pé



## V. Instalação do Selenium dentro da venv

- Criar uma venv pra deixar o selenium acessível só dentro do ambiente que eu quero

     python -m venv venv_selenium

     Pra ativar a venv : source venv_selenium/bin/activate/

- Com venv ativa, instalar o Selenium

     pip install selenium





## VI. O que é o Selenium?
É uma biblioteca (conjunto de ferramentas, feitas com código) de software livre que ajuda a resolver trabalhos manuais e repetitivos usando o browser.

## Selenium Webdriver 
Foi desenvolvido para melhorar a maneira de interação do Selenium com os navegadores. Separa o navegador do código, dando origem a uma camada intermediária pra onde você manda o código e a partir dela (do webdriver), ele executa o código no navegador. Isso possibilitou uqe o código não fosse construindo só em Java Script, ampliando os tipos de linguagens possíveis de escrita da automação.

## Selenium IDE
É um plugin para browser que permite que você faça a sua automação "gravando" o que faz no navegador e dele as reproduz.

## Selenium Grid
Permite a execução de diversos browsers ao mesmo tempo. 
O Grid é dividido em "HUB" e "Nodes". 

Você "cadastra" diversas máquinas (Nodes) no servidor/máquina (HUB).  Quando executa o comando, ele chama o HUB e se o HUB tiver o browser na sua configuração "base", ele executa (ex: Linux e chama um chrome). E ele não tiver (ex: Linux e chama um Safare), ele vai chamar um dos Nodes (alguma das outras máquinas) que possuem essa configuração de navegador para executá-lo. 

Com isso, você pode paralelizar os testes e você desacoplar os testes da máquina que está executando (que pode não ter o browser desejado ou a versão de browser desejada). Ao executar o código, o GRID é o que possibilita que o HUB chame outra máquina (Nodes) na qual realmente roda o teste.
