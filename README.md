# Introdução
Este projeto utiliza um crawler genérico para buscar por vagas em diferentes empresas e lhe permite comparar o seu currículo com essas vagas para que você possa achar as que são relevantes para você.

# Começando
Antes de começar a contribuir com o projeto, veja o nosso [Código de Conduta](https://github.com/douglasdcm/search-jobs/blob/master/docs/CODE_OF_CONDUCT.md).

# Adicionando empresas
Se você quiser adicionar mais empresas ao projeto é bem simples. Em poucos minutos você consegue fazer isso. Veja o exemplo abaixo:
![Exemplo](https://github.com/douglasdcm/search-jobs/blob/master/static/images/add-locator-example.jpg?raw=true)

Veja o [passo a passo](https://github.com/douglasdcm/search-jobs/blob/master/docs/STEPS.md)

# Atualizando o código fonte
Para atualizar o código fonte, ative seu ambiente virtual e instale as dependências
```bash
python3.7 -m venv env
source venv/bin/activate
pip install -r requirements.txt
pip install -r test-requirements.txt
mkdir captures
sudo mkdir -p /webapp/logs
sudo chmod -R 777 /webapp
sudo cp ./src/resources/basic_page.html /webapp
```
Instale o Docker e Docker Compose, faça o build da imagem Docker e suba os containers. Você pode usar o utilitário na pasta `./utils`
```bash
./utils/build_container.sh
```
Copie o arquivo ".env_template" para ".env" e adicione dados de teste no banco de dados
```bash
export PYTHONPATH=$(pwd); python ./utils/add_fake_data_to_databse.py
```
Após finalizar o build, suba o container:
```bash
sudo docker compose up -d
```
Acesse o link `http://localhost:5001`
Agora você pode mexer no código à vontade.

# CLI
```bash
python cli.py --help
2025-05-05 17:58:16 INFO     Commands:
--init            initialize the database
--sanity-check    check the installtion and clean the database
--help            open the help documentation
--overwrite       get the new positions from companies
   [--clean-db]   clean up the database
```

# Rodando os testes
```bash
python -m pytest
```
ou com tox
```bash
tox
```
# Contribuindo
Ajude este projeto a crescer adicionando novas empresas. Que tal começar pelas empresas GPTW do Brasil de 2020? https://conteudo.gptw.com.br/150-melhores-2020.<br>
Pull requests são bem-vindas. Para mudanças grandes crie uma issue para discutirmos o que está sendo modificado. Adicione os testes apropriados.

Dê uma estrelinha se você gostou deste projeto :)
