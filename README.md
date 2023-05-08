# Introdução
Este projeto utiliza um crawler genárico para buscar por vagas em diferentes empresas e lhe permite comparar o seu currículo com essas vagas para que você possa achar as que são relevantes para você.

# Começando
Antes de começar a contribuir com o projeto, veja o nosso [Código de Conduta](https://github.com/douglasdcm/crawler_of_positions/blob/master/CODE_OF_CONDUCT.md).

# Adicionando empresas
Se você quiser adicionar mais empresas ao projeto é bem simples. Em poucos minutos você consegue fazer isso.
- Faça um fork deste projeto e clone o seu repositório 
- Adicione o link de vagas da empresa no arquivo `src/crawler/companies_data.csv`
- Adicione o Xpath 'locator' do link das vagas. O Selenium usa isso para descobrir as vagas da empresa. Veja os exemplos que estão no arquivo.
- Adicione `Y` no terceiro campo do csv. Isso indica que o link está habilitado para a próxima coleta de dados.
- Submeta sua Merge Request para este projeto

# Atualizando o código fonte
Para atualizar o código fonte, ative seu ambiente virtual e instale as dependências
```
python3.6 -m venv env
source venv/bin/activate
pip install -r requirements.txt
pip install -r test-requirements.txt
sudo mkdir -p /webapp/logs
sudo cp ./src/resources/basic_page.html /webapp
chmod -R 777 /webapp
```
Instale o Docker e Docker Compose, faça o build da imagem Docker e suba os containers. Você pode usar o utilitário na pasta `./utils`
```
./utils/build_image.sh
```
Copie o arquivo ".env_template" para ".env" e adicione dados de teste no banco de dados
```
python add_fake_data_to_databse.py
```
Após finalizar o build, suba o container:
```
sudo docker compose up -d
```
Acesse o link `http://localhost:5000`
Agora você pode mexer no código à vontade.

# Rodando os testes

- Baixe a versão correta do Chrome https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip
- Instale a versão baixada do Chrome
```
sudo apt-get install ./src/resources/google-chrome-stable_current_amd64.deb
```
- Ou substitua o arquivo `./src/resources/chrome` para a mesma versão do Chrome instalado em sua máquina. Será preciso verificar a sua versão e baixar o driver correto https://chromedriver.chromium.org/downloads
- Inicialize os containers manualmente (a issue https://github.com/douglasdcm/search-jobs/issues/139 é para melhorar isso)
```
sudo docker compose up -d
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

# Especificação da API REST
O projeto possui alguns end-points cuja documentação (Swagger) pode ser acessada em `http://localhost:5000/spec` 

# Contribuindo
Ajude este projeto a crescer adicionando novas empresas. Que tal começar pelas empresas GPTW do Brasil de 2020? https://conteudo.gptw.com.br/150-melhores-2020.<br>
Pull requests são bem-vindas. Para mudanças grandes crie uma issue para discutirmos o que está sendo modificado. Adicione os testes apropriados.

Dê uma estrelinha se você gostou deste projeto :)
