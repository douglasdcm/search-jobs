# Introdução
Este projeto utiliza crawlers para buscar por vagas em diferentes empresas e lhe permite comparar o seu currículo com essas vagas para achar as que são mais mais similares e relevantes para você.
# Começando
Para usar o projeto você vai precisar instalar o Docker e Docker Compose, fazer o build da imagem Docker e subir os containers.
Mas antes, vá ao arquivo ./src/crawler/factory.py e mude a tag "enabled" de qualquer uma das empresas para True.<br>
Faça o build da imagem. Você pode usar o utilitário na pasta ./utils
<br><code>$./utils/build_image.sh</code><br>
Após finalizar o build, suba o container:
<br><code>$sudo docker compose up -d</code><br>
Depois, rode a request abaixo para polular o seu banco de dados:
<br><code>$curl -XPOST -H "Content-type: application/json" -d '{"hash": "dev"}' 'https://localhost:5000/update'</code><br>
As vagas da empresa são baixadas para o seu banco de dados.
Acesse o link http://localhost:5000 e cole o conteúdo do seu currículo. As vagas mais parecidas serão exibidas.
<br><br>
![alt text](https://i.ibb.co/HH2cJZk/web-page.png)

# Setup
Para contribuir com o projeto, ative seu ambiente virtual e instale as dependências:
<br><code>python3 -m venv env</code>
<br><code>source env/bin/activate</code>
<br><code>pip install -r requirements.txt</code>
<br><code>sudo mkdir -p /webapp/logs</code>
<br><code>sudo cp ./src/resources/basic_page.html /webapp</code><br>
<br><code>chmod -R 777 /webapp</code>
<br><code>sh ./utils/make_dev.sh</code><br>
<br><code>sh ./tests/utils/start_containers.sh</code><br>
Agora você pode mudar a o código e para testar, basta fazer a build da imagem e subir o container novamente.

# Rodando os testes
- instale a versão correta do Chrome
<br><code>sudo apt-get install ./src/resources/google-chrome-stable_current_amd64.deb</code>
- ou subistiua o arquivo em ./src/resources/chrome para a mesma versão do Chrome instalado em sua máquina. Será preciso verificar a sua versão e baixar o driver correto https://chromedriver.chromium.org/downloads 

# Adicionando empresas
Se você quiser adicionar mais empresas ao projeto é bem simples. Em poucos minutos você consegue fazer isso.
- Adicione o dicionário do empresa no arquivo "src/crawler/company.py"
- Adicione o 'locator' do link das vagas. O Selenium usa isso para descobrir as vagas da empresa 
- Adicione a url de vagas da empresa
- Suba o container novamente
- Rode o comando:
<br><code>curl -XPOST -H "Content-type: application/json" -d '{"hash": "dev"}' 'https://localhost:5000/update'</code><br>
Isso irá rodar o crawler que vai pegar as informações de vagas das empresas e salvar no banco de dados. Depois disso você pode comparar o currículo com as novas vagas<br><br>

# Contribuindo
Ajude este projeto a crescer adicionando novos crawlers. Que tal começar pelas empresas GPTW do Brasil de 2020? https://conteudo.gptw.com.br/150-melhores-2020.<br>
Pull requests são bem-vindas. Para mudanças grandes crie uma issue para discutirmos o que está sendo modificado. Adicione os testes apropriados.

Dê uma estrelinha se você gostou deste projeto :)