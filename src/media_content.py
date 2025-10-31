from flask import url_for


def load_web_content():
    return [
        {
            "image": url_for("static", filename="images/android-chrome-1200x1200.png"),
            "link": "https://github.com/douglasdcm/search-jobs",
            "caption": "Star this project on GitHub!",
            "alt": "Star this project on GitHub!",
            "description": (""),
        },
        {
            "image": url_for("static", filename="images/guara-square.png"),
            "link": "https://github.com/douglasdcm/guara",
            "caption": "Page Transactions for UI test automation",
            "alt": "Page Transactions for UI test automation",
            "description": (
                "Guará is a Python framework designed to simplify UI test automation."
                " Inspired by design patterns like Page Objects, App Actions, and Screenplay,"
                " Guará focuses on Page Transactions—encapsulating user interactions"
                " (transactions) on web pages, such as Login, Logout, or Form Submissions."
                " It’s not just a tool; it’s a programming pattern that can be adapted to"
                " any web driver, not just Selenium."
            ),
        },
        {
            "image": url_for("static", filename="images/caqui.png"),
            "link": "https://github.com/douglasdcm/caqui",
            "caption": "Run synchronous and asynchronous commands in WebDrivers",
            "alt": "Run synchronous and asynchronous commands in WebDrivers",
            "description": (
                "Caqui executes commands against Drivers synchronously and asynchronously."
                " The intention is that the user does not worry about which Driver they're using."
                " It can be WebDrivers like Selenium, MobileDrivers like Appium, or DesktopDrivers"
                " like Winium. It can also be used in remote calls. The user can start the Driver"
                " as a server in any host and provide the URL to Caqui clients."
            ),
        },
        {
            "image": (
                "https://miro.medium.com/v2/resize:fit:720/format:webp/"
                "1*3O88y8CI3cWn1quZllqI_A.jpeg"
            ),
            "link": "https://python.plainenglish.io/python-refactoring-to-patterns-1ca71be08a60",
            "caption": "Python: Refactoring to Patterns",
            "alt": "Python: Refactoring to Patterns",
            "description": (
                "After nearly a year of effort, I’ve finally completed my self-imposed goal of "
                "writing all the refactoring examples from the book Refactoring to Patterns by "
                "Joshua Kerievsky in Python. This book broadened my understanding of how to "
                "apply design patterns in production code."
            ),
        },
        {
            "image": (
                "https://miro.medium.com/v2/resize:fit:1400/format:webp/"
                "1*6CYeBk_azj1c2sxpIPSajQ.jpeg"
            ),
            "link": (
                "https://medium.com/python-in-plain-english/python-cli-with-kinde"
                "-authentication-588bd46d64b3"
            ),
            "caption": "Building a Python CLI System with Kinde Authentication",
            "alt": "Building a Python CLI System with Kinde Authentication",
            "description": (
                "This is one of my experiments again. Now I built a CLI application in Python and"
                " integrated it with the authentication tool called Kinde to manage the user"
                " permissions and allow them to perform just the granted operations."
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
            "alt": "Playing with PyScript, Postgres and K8S",
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
            "caption": "QA e Dev stop fighting",
            "alt": "QA e Dev stop fighting",
            "description": (
                "QAs and Dev from all places, let's give hands and make a better world"
            ),
        },
        {
            "image": url_for("static", filename="images/chatbot.png"),
            "link": "https://github.com/douglasdcm/chatbot_for_movies",
            "caption": "Building a Chat Bot using AI with movie scripts dataset",
            "alt": "Building a Chat Bot using AI with movie scripts dataset",
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
            "caption": "What was it like speaking at TDC?",
            "alt": "What was it like speaking at TDC?",
            "description": (
                "In 2019, when we could still participate in in-person events without"
                " worrying about crowds, I was invited to speak at the largest"
                " developer conference in Latin America:"
                "The Developer's Conference (TDC)."
            ),
        },
        {
            "image": url_for("static", filename="images/win_rest.jpeg"),
            "link": (
                "https://medium.com/@douglas.dcm/"
                "testing-windows-apps-with-http-rest-b4e8f80f8b7e"
            ),
            "caption": "Testing Windows Apps with HTTP REST",
            "alt": "Testing Windows Apps with HTTP REST",
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
            "alt": "Find jobs using ML and help people",
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
            "image": url_for("static", filename="images/mtc.png"),
            "link": "https://www.youtube.com/watch?v=UTEikC3_n84",
            "caption": "MTC 2021 Conversation about shift left",
            "alt": "MTC 2021 Conversation about shift left",
            "description": (
                "Douglas Cardoso presents at the Minas Testing Conference (MTC) the"
                " concepts of the term 'Shift left' that has been disseminated"
                " in recent years in the software testing community."
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
            "alt": "Building a Chat Bot",
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
            "caption": "Over 2000 companies for you.",
            "alt": "Over 2000 companies for you.",
            "description": (
                "List of over 2000 Brazilian companies to register with and"
                "get a new job."
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
            "alt": "TDC Load test",
            "description": (
                "Douglas Cardoso presents performance testing concepts"
                " and some real-world results at The Developer's Conference."
            ),
        },
        {
            "image": url_for("static", filename="images/strategy.jpeg"),
            "link": "https://www.youtube.com/watch?v=1N60S1w-XTE",
            "caption": "Strategy pattern in software testing",
            "alt": "Strategy pattern in software testing",
            "description": (
                "Video with an example of implementing the design pattern"
                "'Strategy' for software test automation."
            ),
        },
        {
            "image": url_for("static", filename="images/repository.jpeg"),
            "link": "https://www.youtube.com/watch?v=vldamqyw4BE",
            "caption": "Object Repository using Selenium",
            "alt": "Object Repository using Selenium",
            "description": (
                "Video demonstrating an easy way to map pages of"
                "a graphical interface for software test automation."            ),
        },
        {
            "image": url_for("static", filename="images/ai_test_pso_ga.png"),
            "link": (
                "https://www.linkedin.com/in/douglas-cardosom/detail/overlay-view/urn"
                ":li:fsd_profileTreasuryMedia:(ACoAAAdISwAB2r6ESCQE2IRQ5cY0YUDoObigdjk"
                ",1599225926667)/"
            ),
            "caption": "IA in software testing (PSO e GA)",
            "alt": "IA in software testing (PSO e GA)",
            "description": (
                "Presentation with examples of the use of artificial intelligence"
                "in software testing."            
            ),
        },
        {
            "image": url_for("static", filename="images/poli.webp"),
            "link": "https://www.paginaseditora.com.br/product-page/poli-escolhe",
            "caption": "Children's book 'Poli escolhe'",
            "alt": "Children's book 'Poli escolhe'",
            "description": (
                "To address the theme of children's choices, the author"
                "Cláudia Rezende, who is a journalist, thought of a situation"
                "very common among generations, which is the decision of which"
                "football team will be their child's favorite. Thus, starting"
                "from an encounter in a playground, the doubt arises in"
                "the protagonist, and the plot unfolds, with Poli often"
                "putting the adults against the wall."
                "The idea, according to the journalist, is to encourage reflection on"
                "the interference that parents make in their children's choices"
                "and the possibility of providing them with the development"
                "of independent thinking from childhood."
                "The book also carries a message of peace between"
                "the fans, since the rivalry should only be on"
                "the pitch, right?"            ),
        },
        {
            "image": url_for("static", filename="images/xpath.jpg"),
            "link": "https://www.youtube.com/watch?v=x9Li9wh8H7s",
            "caption": "Xpath for testers",
            "alt": "Xpath for testers",
            "description": (
                "Video with concepts and practical examples of using XPath"
                "in software test automation."            
            ),
        },
        {
            "image": url_for("static", filename="images/dataset.jpg"),
            "link": "https://www.kaggle.com/douglasdcm/computer-events-errors-defects-and-warnings",
            "caption": "Dataset of defects",
            "alt": "Dataset of defects",
            "description": (
                "This dataset was created to be used in a machine learning exercise in order to"
                "discover if the events and errors of a personal computer"
                "Windows had any relationship or association between them."
                "This is a simple extraction of data from the Windows"
                "Events Viewer of a personal computer."            ),
        },
        {
            "image": url_for("static", filename="images/unit.png"),
            "link": "https://enterprisecraftsmanship.com/posts/unit-testing-dependencies/",
            "caption": "Unit Testing Dependencies",
            "alt": "Unit Testing Dependencies",
            "description": (
                "Author 'Vladimir Khorikov'. In this article, we’ll review the types"
                " of unit testing dependencies. This is more of a reference article,"
                " to which I’ll be referring in future posts. Still, this topic is"
                " important for establishing the common vocabulary"
            ),
        },
    ]
