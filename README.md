# Introdução
Este projeto utiliza crawlers para buscar por vagas em diferentes empresas e lhe permite comparar o seu currículo com essas vagas para achar as que são mais mais similares e relevantes para você.

# Começando
Para usar o projeto você vai precisar instalar o Docker e Docker Compose, fazer o build da imagem Docker e subir os containers. Você pode usar o utilitário na pasta ./utils
```
./utils/build_image.sh
```
Após finalizar o build, suba o container:
```
sudo docker compose up -d
```
Mude o arquivo ".env_template" para ".env".
Depois, rode o comando abaixo para polular o seu banco de dados:
```
python cli.py --overwrite

# veja mais detalhes com "python cli.py -h"
```
As vagas das empresas serão baixadas para o seu banco de dados.
Acesse o link http://localhost:5000 e cole o conteúdo do seu currículo. As vagas mais parecidas serão exibidas.

# Setup
Para contribuir com o projeto, ative seu ambiente virtual e instale as dependências:
```
python3.6 -m venv env
source venv/bin/activate
pip install -r requirements.txt
pip install -r test-requirements.txt
sudo mkdir -p /webapp/logs
sudo cp ./src/resources/basic_page.html /webapp
chmod -R 777 /webapp
docker compose up -d
```
Adicione dados de teste no banco de dados

```
python add_fake_data_to_databse.py
```

Agora você pode mudar o código à vontade.


# Rodando os testes
- Baixe a versão correta do Chrome https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip
- instale a versão correta do Chrome
```
sudo apt-get install ./src/resources/google-chrome-stable_current_amd64.deb
```
- ou substitua o arquivo em ./src/resources/chrome para a mesma versão do Chrome instalado em sua máquina. Será preciso verificar a sua versão e baixar o driver correto https://chromedriver.chromium.org/downloads
- Inicialize os containers manualmente (a isse 139 é para melhorar isso)
```
docker compose up -d
```
- Rode os testes.
Atenção: os teste não funcionais demoram mais de uma hora para terminar. Melhor deixar pra rodar quando necessário
```
python -m pytest -m functional
```
ou com tox
```
tox
```
ou com os utilitários
```
./utils/run_functional.sh
```


## Testes não funcionais
Para executar os testes de performance da API REST (demoram mais de 1h)
```
./utils/run_non_functional.sh
```
Para testes do comandos no terminal

```
./utils/cProfile/run_perfomance_test_cli.sh
```
Os resultados da execução serão abertos no navegador
<br>
References about snakeviz
- https://jiffyclub.github.io/snakeviz/
- https://docs.python.org/3/library/profile.html#module-cProfile


# Debug
- Ver número de conexões no banco de dados
```
select count(*) from pg_stat_activity;
```
- Conectar no banco de dados
```
docker exec -it postgres psql -U postgres
```
- Logs da aplicação
```
tail -f /webapp/logs/crawlers.log
```

# Adicionando empresas
Se você quiser adicionar mais empresas ao projeto é bem simples. Em poucos minutos você consegue fazer isso.
- Adicione o dicionário da empresa no arquivo "src/crawler/company.py"
- Adicione o 'locator' do link das vagas. O Selenium usa isso para descobrir as vagas da empresa
- Adicione a url de vagas da empresa
- Suba o container novamente
- Rode o comando:
```
python cli.py --ovewrite
```
Isso irá rodar o crawler que vai pegar as informações de vagas das empresas e salvar no banco de dados. Depois disso você pode comparar o currículo com as novas vagas


# Especificação da API REST
O projeto possui alguns end-points cuja documentação (Swagger) pode ser acessada em `http://localhost:5000/spec` 

# Contribuindo
Ajude este projeto a crescer adicionando novos crawlers. Que tal começar pelas empresas GPTW do Brasil de 2020? https://conteudo.gptw.com.br/150-melhores-2020.<br>
Pull requests são bem-vindas. Para mudanças grandes crie uma issue para discutirmos o que está sendo modificado. Adicione os testes apropriados.

Dê uma estrelinha se você gostou deste projeto :)