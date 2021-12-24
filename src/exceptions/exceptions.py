class ErroBancoDados(Exception):
    def __init__(self, menssagem="Erro no banco de dados."):
        super().__init__(menssagem)

class ComandoInvalido(Exception):
    def __init__(self, menssagem="O comando não foi reconehecido como um comando válido."):
        super().__init__(menssagem)

class InvalidDriverType(Exception):
    def __init__(self, menssagem="The specified driver type does not exist."):
        super().__init__(menssagem)

class NotificationException(Exception):
    def __init__(self, menssagem="Error in the notification process."):
        super().__init__(menssagem)