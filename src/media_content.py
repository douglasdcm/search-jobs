from flask import url_for


def load_web_content():
    return [
        {
            "image": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "link": "https://github.com/douglasdcm/search-jobs",
            "caption": "Contribute",
            "description": (
                ""
            ),
        },
        {
            "image": (
                "https://miro.medium.com/v2/resize:fit:640/"
                "format:webp/1*jLSxNQvNqsYr02VB_wr96A.jpeg"
            ),
            "link": (
                "https://medium.com/@douglas.dcm/"
                "playing-with-pyscript-postgres-and-k8s-55690f0cd4da"
            ),
            "caption": "Playing with PyScript, Postgres and K8S",
            "description": (
                "I’ve talked in other posts about my hobby of experimenting with "
                "technologies"
                " that interest me. This time I spent some time"
                " experimenting with PyScript. I have to say that I decided to"
                " study PyScript, because I’m a no-no with JavaScript and I wanted"
                " to know if using PyScript it would be possible to get the same "
                "results I get when using JavaScript. So, in my tests I used pure "
                "Python to develop an application that integrates front-end,"
                " back-end and some database."
            ),
        },
        {
            "image": url_for("static", filename="images/qa_dev.jpeg"),
            "link": "https://medium.com/@douglas.dcm/qa-e-dev-parem-de-brigar-e577fa583d63",
            "caption": "QA e Dev parem de brigar",
            "description": (
                "The intention of this project is to create a chatbot based on movie"
                " reviews so that you can ask questions and have a free conversation"
                " about this topic."
            ),
        },
        {
            "image": url_for("static", filename="images/chatbot.png"),
            "link": "https://github.com/douglasdcm/chatbot_for_movies",
            "caption": "Building a Chat Bot using AI with movie scripts dataset",
            "description": (
                "The intention of this project is to create a chatbot based on movie"
                " reviews so that you can ask questions and have a free conversation"
                " about this topic. Recently I had to buy a new internet service,"
                " so I tried to do it using the available chatbot of the company."
                " I noticed the conversation with the chatbot was based on rules"
                " and conditions. Hence, for each question I was doing to the bot,"
                " it was sending to me a list of options I needed to choose to go"
                " to the next step of the conversation. The experience was not good"
                " for me and it did not solve my problem. So, I started search for"
                " possible solutions, just for curiosity, and I found some contents"
                " in the internet talking about the training of a chatbot using"
                " Natural Language Processing (NLP). After this reading, I decided"
                " to take the challenge and train my on chatbot for natural"
                " conversations."
            ),
        },
        {
            "image": url_for("static", filename="images/tdc.jpeg"),
            "link": "https://medium.com/@douglas.dcm/como-foi-palestrar-no-tdc-d13d7bebdfe2",
            "caption": "Como foi palestrar no TDC",
            "description": (
                "Em 2019, quando ainda podíamos participar de eventos presenciais sem"
                " nos preocupar com aglomerações, fui convidado para palestrar na maior"
                " conferência de desenvolvedores da América Latina:"
                " The Developer’s Conference (TDC)."
            ),
        },
        {
            "image": url_for("static", filename="images/win_rest.jpeg"),
            "link": (
                "https://medium.com/@douglas.dcm/"
                "testing-windows-apps-with-http-rest-b4e8f80f8b7e"
            ),
            "caption": "Testing Windows Apps with HTTP REST",
            "description": (
                "Did you already have the necessity to test a Frankenstein app that"
                " had the operation mixed in Desktop, Web and Mobile pages?"
                " So, keep reading this post. This is for you."
            ),
        },
        {
            "image": url_for("static", filename="images/job_ml.jpeg"),
            "link": (
                "https://medium.com/@douglas.dcm/"
                "find-jobs-that-match-your-curriculum"
                "-using-ml-and-help-people-137ff19dae3d"
            ),
            "caption": "Find jobs using ML and help people",
            "description": (
                "Here in Brazil the situation is not good nowadays. We have more than"
                " 500 thousands of dead people by Covid-19, many companies closed"
                " the doors, hence a lot of people lose their jobs."
                " In my LinkedIn feed every day there is a new post about someone"
                " that was fired and is searching for a new job position. "
                "Some months ago, before the pandemic, something similar happened"
                " to me. More than 80 people including me, were fired suddenly"
                " because our company loose a very big project that was responsible"
                " for more than 60% for its revenue."
            ),
        },
        {
            "image": url_for("static", filename="images/mtc.jpeg"),
            "link": "https://www.youtube.com/watch?v=UTEikC3_n84",
            "caption": "MTC 2021 Conversa sobre shift left",
            "description": (
                "Douglas Cardoso apresenta no Minas Testing Conference (MTC) os"
                " conceitos de termo 'Shift left' que vem sendo difundido"
                " nos últimos anos na comunidade de testes de software."
            ),
        },
        {
            "image": url_for("static", filename="images/chatbot_medium.png"),
            "link": (
                "https://medium.com/analytics-vidhya/"
                "building-a-chat-bot-using-ai-with-movie"
                "-scripts-dataset-f18fc1f9629e"
            ),
            "caption": "Building a Chat Bot",
            "description": (
                "Recently I had to buy a new internet service, so I tried to do it"
                " using the available chatbot of the company. I noticed the"
                " conversation with the chatbot was based on rules and"
                " conditions. Hence, for each question I was doing to the bot"
                ", it was sending to me a list of options I needed to choose"
                " to go to the next step of the conversation. The experience"
                " was not good for me and it did not solve my problem."
                " So, I started search for possible solutions,"
                " just for curiosity, and I found some contents in the internet"
                " talking about the training of a chat bot using Natural Language"
                " Processing (NLP). After this reading, I decided to take the"
                " challenge and train my on chatbot for natural conversations."
            ),
        },
        {
            "image": url_for("static", filename="images/2k.avif"),
            "link": (
                "https://docs.google.com/spreadsheets/d/1f79chLKAfuaD-"
                "aLbJ_9TPeyG2PTsUrlDNWkafkBxx6Q/edit?pli=1#gid=2079962305"
            ),
            "caption": "Mais de 2000 empresas para você",
            "description": (
                "Lista de mais de 2000 empresas de brasileiras para se cadastrar e"
                " conseguir um novo emprego."
            ),
        },
        {
            "image": url_for("static", filename="images/tdc.png"),
            "link": (
                "https://www.linkedin.com/in/douglas-cardosom/detail/overlay-view"
                "/urn:li:fsd_profileTreasuryMedia:(ACoAAAdISwAB2r6ESCQE2IRQ5cY0YUDoObigdjk"
                ",1599226983384)/"
            ),
            "caption": "TDC Load test",
            "description": (
                "Douglas Cardoso apresenta no The Developer's Conference conceitos"
                " de teste de performance e alguns resultados reais."
            ),
        },
        {
            "image": url_for("static", filename="images/strategy.jpeg"),
            "link": "https://www.youtube.com/watch?v=1N60S1w-XTE",
            "caption": "Strategy pattern em testes de software",
            "description": (
                "Vídeo com um exemplo de implementação do padrão de projeto"
                " 'Strategy' para automação de testes de software."
            ),
        },
        {
            "image": url_for("static", filename="images/repository.jpeg"),
            "link": "https://www.youtube.com/watch?v=vldamqyw4BE",
            "caption": "Object Repository usando o Selenium",
            "description": (
                "Vídeo com implementação de uma forma fácil de mapear as páginas de"
                " uma interface gráfica para automação de testes de software."
            ),
        },
        {
            "image": url_for("static", filename="images/ai_test_pso_ga.png"),
            "link": (
                "https://www.linkedin.com/in/douglas-cardosom/detail/overlay-view/urn"
                ":li:fsd_profileTreasuryMedia:(ACoAAAdISwAB2r6ESCQE2IRQ5cY0YUDoObigdjk"
                ",1599225926667)/"
            ),
            "caption": "IA em testes de software (PSO e GA)",
            "description": (
                "Apresentação com exemplos de utilização de inteligência"
                " artificial em testes de software."
            ),
        },
        {
            "image": url_for("static", filename="images/poli.webp"),
            "link": "https://www.paginaseditora.com.br/product-page/poli-escolhe",
            "caption": "Livro infantil 'Poli escolhe'",
            "description": (
                "Para abordar a temática da escolha das crianças, a autora"
                " Cláudia Rezende, que é jornalista, pensou em uma situação"
                " muito comum entre as gerações, que é a definição de qual vai"
                " ser o time de futebol do coração do filho. Assim, a partir"
                " de um encontro num parquinho, a dúvida se estabelece na"
                " protagonista, e o enredo se desenvolve, com Poli muitas"
                " vezes colocando os adultos contra a parede."
                " A ideia, conforme a jornalista, é propor a reflexão sobre"
                " as interferências que os pais fazem nas escolhas dos filhos"
                " e a possibilidade de proporcionar a estes o desenvolvimento"
                " da autonomia do pensar já desde a infância."
                " O livro não deixa, também, de levar uma mensagem de paz entre"
                " as torcidas, já que a rivalidade deve ser mesmo só nos"
                " gramados, certo?"
            ),
        },
        {
            "image": url_for("static", filename="images/xpath.jpg"),
            "link": "https://www.youtube.com/watch?v=x9Li9wh8H7s",
            "caption": "Xpath para testadores",
            "description": (
                "Vídeo com conceitos e exemplos práticos de utilização de Xpath"
                " em automação de testes de software."
            ),
        },
        {
            "image": url_for("static", filename="images/lasciva_lula.jpeg"),
            "link": "https://www.youtube.com/watch?v=FyMZ-iC7Jl4",
            "caption": "Música 'Suportar'",
            "description": (
                "'Suportar', música da banda 'Lasciva Lula' lançada no disco "
                "Sublime Mundo Crânio (2007). Clipe inspirado na série de quarentena"
                " do fotógrafo Lauro Machado."
            ),
        },
        {
            "image": url_for("static", filename="images/dataset.jpg"),
            "link": "https://www.kaggle.com/douglasdcm/computer-events-errors-defects-and-warnings",
            "caption": "Dataset de defeitos",
            "description": (
                "Este dataset foi criado para ser usado em um exercício de ML a fim"
                " de ser descobrir se os eventos e errors de um computador pessoal"
                " Windows tinham alguma relação, ou associação entre eles."
                " Isso é uma simples extração de dados do Windows "
                "Events Viewer de um computador pessoal."
            ),
        },
        {
            "image": url_for("static", filename="images/unit.png"),
            "link": "https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/",
            "caption": "Unit Testing Dependencies",
            "description": (
                "Author 'Vladimir Khorikov'. In this article, we’ll review the types"
                " of unit testing dependencies. This is more of a reference article,"
                " to which I’ll be referring in future posts. Still, this topic is"
                " important for establishing the common vocabulary"
            ),
        },
    ]
