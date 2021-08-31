# Introdução
Este projeto utiliza crawlers para buscar por vagas em diferentes empresas e lhe permite comparar o seu currículo com essas vagas para achar as que são mais mais similares e relevantes para você.
# Começando
Para usar o projeto basta salvar o conteúdo do seu currículo em um arquivo de texto, por exemplo "/tmp/cv.txt", clonar o repositório, ir para a pasta raíz e executar:
<br><code>$pip install -r requirements.txt</code>
<br><code>$python main.py --compare /tmp/cv.py</code><br><br>
O ranking de vagas mais similares será impresso. O projeto já vem com mais de 250 vagas pré-cadastradas para serem usadas.
# Fazendo seu própiro crawler
Se você quiser adicionar mais crawlers ao projeto, é bem simples. Em poucos minutos você consegue adicionar um novo crawler. Você precisa seguir o protocolo da classe "src/crawler/ICrawler.py::ICrawler" para que os campos certos sejam salvos no banco de dados. Faça isso:
- Adicione o crawler na pasta "src/crawler"
- Adicone os Page Objects para o crawler na pasta "src/pages". Por exemplo, "scr/pages/my_crawler/vagas.py"
- Edite o seu crawler para utilizar o novo Page Objects
- Adicione o dicionário do crawler no arquivo "src/crawler/factory.py" abaixo da linha comentada
- Adicione a url de vagas da empresa em "src/settings.py::URLS"
- Rode o comando:
<br><code>$python main.py --run</code><br><br>
Isso irá rodar os crawler "enabled", pegar as informações de vagas das empresas e salvar no banco de dados. Depois disso você pode comparar o currículo com as novas vagas.<br><br>
Tente "--help" para mais informações.
<br><code>$python main.py --help</code><br>
# Web page
O currículo pode ser comparado utilizando o a Web page. Rode:
<br><code>$python app.py</code><br><br>
e acesse http://localhost:5000
<br><br>
![alt text](https://i.ibb.co/HH2cJZk/web-page.png)
# Contribuindo
Pull requests são bem-vindas. Para mudanças grandes crie uma issue para discutirmos o que está sendo modificado. Adicione os testes apropriados.

Dê uma estrelinha se você gostou deste projeto :)