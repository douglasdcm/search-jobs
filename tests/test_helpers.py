from src.helper.helper import data_pre_processing, steam_data, summarize_text
from pytest import mark


@mark.functional
class TestUnitHelper:

    testdata = [
        ("mecân", "mecan"),
        ("123", ""),
        ("@#$%", ""),
        ("ãáçäx", "aacax"),
        ("", ""),
        ("administração", "administraca"),
    ]

    steamdata = [
        ("maravilhoso", "maravilh"),
        ("vejam", "vej"),
        ("administrar", "administr"),
        ("testes", "test"),
        ("tests", "test"),
        ("cats", "cat"),
    ]

    @mark.parametrize("message, result", testdata)
    def test_preprocessing_return_data_for_special_char(self, message, result):
        assert data_pre_processing(message) == result

    @mark.parametrize("message, result", steamdata)
    def test_steamming_is_striping_the_text(self, message, result):
        assert steam_data(message) == result

    def test_steamming_is_striping_the_list_of_texts(self):
        texts = ["cats", "dogs"]
        expected = ["cat", "dog"]
        actual = [steam_data(t) for t in texts]
        assert set(actual) == set(expected)

    def test_preprocessing_works_with_list_of_texts(self):
        text = "cats dogs administração testes analista"
        expected = ["cat", "dog", "administraca", "test", "anal"]
        actual = data_pre_processing(text)
        for term in expected:
            assert term in actual

    def test_summarization_of_positions(self):
        text = """
        Skip to main content
        Go to careers page
        Apply
        Account Executive
        Copy link
        Published on JUNE 05, 2025
        Applications open until DECEMBER 31, 2026
        Workplace: São Paulo - SP
        São Paulo - SP
        Job type: Full-time employee
        Full-time employee
        Work model: Hybrid
        Hybrid
        Also for PwD
        Also for PwD
        JOB DESCRIPTION
        Você é movido por resultados, apaixonado por tecnologia e tem perfil consultivo?
        A FCamara está em busca de uma pessoa para atuar como Account Executive com foco em
        venda de soluções de tecnologia, que saiba navegar em ambientes desafiadores e colaborar
        com diferentes níveis hierárquicos dos clientes, do operacional ao C-Level.
        RESPONSIBILITIES AND ASSIGNMENTS
        Gerenciar e expandir contas estratégicas, com foco em relacionamento (perfil Farmer);
        Atuar com venda consultiva e técnica de serviços de tecnologia e transformação digital;
        Identificar e mapear necessidades dos clientes para propor soluções personalizadas
        de alocação de profissionais (bodyshop);
        Conduzir reuniões de relacionamento e negociação com stakeholders de diferentes
        áreas (negócios, operações e executivos);
        Garantir o uso eficiente do CRM Salesforce para reportar atividades
        , oportunidades e status das contas;
        Colaborar com áreas internas para garantir excelência na
        entrega de projetos e satisfação do cliente;
        Ser agente de transformação e inovação nas contas geridas.

        REQUIREMENTS AND QUALIFICATIONS
        Sólida experiência em venda consultiva de serviços de tecnologia;
        Vivência em consultorias de TI, especialmente com modelo de alocação (bodyshop);
        Atuação comprovada em projetos de transformação digital;
        Facilidade em transitar entre diferentes áreas e níveis hierárquicos;
        Domínio do CRM Dynamics;
        Ensino superior completo;
        Inglês avançado.
        Foco no cliente e senso de urgência;
        Pensamento crítico e capacidade de influenciar;
        Protagonismo e visão de dono;
        Habilidade em negociação e resolução de conflitos;
        Inovação, pesquisa e orientação a resultados.
        Vivência em Multisetores
        Experiência anterior com grandes contas ou ambientes corporativos complexos;
        Conhecimento em squads ágeis e estruturação de times técnicos.
        ADDITIONAL INFORMATION
        Somos um ecossistema de tecnologia e inovação, com atuação global e foco em gerar impacto
        real nos nossos clientes e na sociedade. Acreditamos na transformação digital como
        ferramenta
        estratégica para crescimento e evolução de negócios.
        PROCESS STAGES
        Step 1: Registration
        1
        Registration
        Step 2: Entrevista R&S
        2
        Entrevista R&S
        Step 3: Entrevista Técnica
        3
        Entrevista Técnica
        Step 4: CV Enviado ao Cliente
        4
        CV Enviado ao Cliente
        Step 5: Entrevista Cliente
        5
        Entrevista Cliente
        Step 6: Carta Proposta
        6
        Carta Proposta
        Step 7: Hiring
        7
        Hiring
        TRANSFORMAMOS MUNDOS SONHADOS EM TRAJETÓRIAS REAIS.🧡🚀

        Aqui somos #SangueLaranja!

        Estamos há 17 anos no mercado, lado a lado com nossos clientes, proporcionando
        experiências transformadoras.
        Somos um ecossistema de tecnologia e inovação, com expansão global; Além do Brasil
        estamos presentes na Europa e Reino Unido com escritórios em Portugal, Londres,
        Dubai e Holanda. 🌎
        F de Formação: acreditamos na prática da cultura do compartilhamento, no senso de
        comunidade, e que o conhecimento
        tem o poder da transformação!
        Possuímos iniciativas, e ações sociais, que promovem o desenvolvimento, como a comunidade
        tech Orange Juice, o Programa de Formação
        nossa escola de liderança e diversas parcerias com ONGs e Edtechs.
        Na FCamara todos são bem-vindos, para nós, Diversidade, Respeito e Ética,
        são elementos inegociáveis e fazem parte do nosso DNA.
        E aí, está pronto para fazer parte de um time incrível e ser protagonista da
        própria história?
        CONHEÇA MAIS SOBRE NÓS
        Website
        LinkedIn
        Facebook
        Instagram
        Glassdoor
        Apply
        Copy link
        Powered by Gupy 2025. All rights reserved.
        ×
        By clicking “Accept cookies,” you agree to the storing of cookies on your device to
        improve site navigation, analyze site usage, and assist in our marketing
         efforts. Cookie Notice Privacy Notice
        Reject All
        Accept Cookies
        Cookie Settings
        """
        expected = "Gerenciar e expandir contas estratgicas, com foco em relacionamento"
        assert expected in summarize_text(text)
