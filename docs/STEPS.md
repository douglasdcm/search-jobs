# Adicionando empresas
Se você quiser adicionar mais empresas ao projeto é bem simples. Em poucos minutos você consegue fazer isso. Veja o exemplo abaixo:
![Exemplo](https://github.com/douglasdcm/search-jobs/raw/master/static/images/add-locator-example.jpg?raw=true)

- Faça um fork deste projeto e clone o seu repositório 
- Adicione o link de vagas da empresa no arquivo [companies_data.csv](https://github.com/douglasdcm/search-jobs/blob/master/src/crawler/companies_data.csv)
- Adicione o Xpath 'locator' do link das vagas. O Selenium usa isso para descobrir as vagas da empresa. Veja os exemplos que estão no arquivo.
- Adicione `Y` no terceiro campo do csv. Isso indica que o link está habilitado para a próxima coleta de dados.
- Submeta sua Merge Request para este projeto

