class CommandError(Exception):
    pass


class CrawlerError(Exception):
    pass


class WebDriverError(Exception):
    pass


class RequestError(Exception):
    pass


class DatabaseError(Exception):
    def __init__(self, menssagem="Erro no banco de dados."):
        super().__init__(menssagem)


class InvalidCommandError(Exception):
    def __init__(self, menssagem="O comando não foi reconehecido como um comando válido."):
        super().__init__(menssagem)


class InvalidDriverType(Exception):
    def __init__(self, menssagem="The specified driver type does not exist."):
        super().__init__(menssagem)
