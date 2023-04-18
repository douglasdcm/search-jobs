from src.exceptions.exceptions import DatabaseError
from src.settings import DEBUG
from src.database.db_postgres import Database as DbBase


class Database(DbBase):
    """Class used for Sqlite"""

    def cria_banco(self, banco):
        """The database is not created for Sqlite"""
        pass

    def _cria_conexao(self):
        try:
            con = type(self)._conexao
            cur = con.cursor()
            return [con, cur]
        except Exception as e:
            raise DatabaseError(f"Não foi possível criar a conexão de banco.\n{str(e)}")

    def cria_tabela(self, tabela, campos, complemento=""):
        if complemento:
            complemento = "," + complemento
        query = f"create table if not exists {tabela} (id INTEGER NOT NULL PRIMARY KEY, {campos} {complemento})"
        mensagem_erro = "Não foi possível criar a tabela."
        self._run(query, mensagem_erro)
