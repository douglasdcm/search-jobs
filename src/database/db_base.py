from logging import info
from src.exceptions.exceptions import ErroBancoDados
from src.settings import DEBUG


class Database:

    _conexao = None

    def __init__(self, conexao=None):
        if type(self)._conexao is None:
            if conexao is not None:
                type(self)._conexao = conexao
            else:
                raise ErroBancoDados("Uma conexão precisa ser informada.")

    def cria_banco(self, banco):
        try:
            cmd = f"create database {banco}"
            items = self._cria_conexao()
            cur = items[1]
            info(cmd)
            cur.execute(cmd)
        except Exception:
            raise ErroBancoDados("Não foi possível criar o banco.")

    def deleta_banco(self, banco):
        try:
            cmd = f"drop database {banco} WITH (FORCE)"
            items = self._cria_conexao()
            cur = items[1]
            info(cmd)
            cur.execute(cmd)
        except Exception as e:
            raise ErroBancoDados(f"Não foi possível deletar o banco.\n{str(e)}")

    def deleta_tabela(self, tabela):
        try:
            cmd = f"drop table if exists {tabela}"
            items = self._cria_conexao()
            cur = items[1]
            info(cmd)
            cur.execute(cmd)
        except Exception as e:
            raise ErroBancoDados(f"Não foi possível deletar a tabela.\n{str(e)}")

    def fecha_conexao_existente(self):
        try:
            con = type(self)._conexao
            con.close()
            type(self)._conexao = None
            return True
        except Exception:
            return False

    def _cria_conexao(self):
        try:
            con = type(self)._conexao
            con.autocommit = True
            cur = con.cursor()
            return [con, cur]
        except Exception:
            raise ErroBancoDados("Não foi possível criar a conexão de banco.")

    def cria_tabela(self, tabela, campos, complemento=""):
        if complemento:
            complemento = "," + complemento
        query = f"create table {tabela} (id SERIAL PRIMARY KEY, {campos} {complemento})"
        mensagem_erro = "Não foi possível criar a tabela."
        self._run(query, mensagem_erro, fetch=False)


    def atualiza_registro(self, tabela, sets, id_):
        query = f"""UPDATE {tabela}
                SET {sets}
                WHERE id = {id_};"""
        mensagem_erro = "Não foi possível atualizar o registro."
        self._run(query, mensagem_erro)

    def salva_registro(self, tabela, campos, valores):
        """Retorna a tupla com o maior id da tabela"""
        query = f"insert into {tabela} ({campos}) values ({valores})"
        mensagem_erro = "Não foi possiível salvar o registro."
        self._run(query, mensagem_erro, fetch=False)
        return self.pega_maior_id(tabela)

    def pega_maior_id(self, tabela):
        query = "SELECT * FROM {} WHERE id = ( SELECT MAX(id) FROM {} );".format(tabela, tabela)
        mensagem_erro = "Não foi possível pegar o ID máximo."
        return self._run(query, mensagem_erro)

    def pega_todos_registros(self, tabela, campos="*", distinct=False):
        query = "select"
        if distinct:
            query += " DISTINCT"
        query += f" {campos} from {tabela}"
        mensagem_erro = "Não foi possível pegar os registros."
        return self._run(query, mensagem_erro)

    def pega_por_query(self, query):
        mensagem_erro = "Não foi possível executar a query especificada."
        return self._run(query, mensagem_erro)

    def _run(self, query, mensagem_erro, fetch=True):
        """
        Args:
            query (str): consulta sql a ser executada
            mensagem_erro (str): menssagem retornada em caso de erro na execução

        Returns:
            (tuple): tupla com os registros do banco de dados
        """
        try:
            if DEBUG:
                info("QUERY: {}".format(query))
            items = self._cria_conexao()
            con = items[0]
            cur = items[1]
            cur.execute(query)
            con.commit()
            if fetch:
                return cur.fetchall()
            else:
                return True
        except Exception as e:
            print(str(e))
            info(str(e))
            raise ErroBancoDados(f"{mensagem_erro}\nquery: {query}\n{str(e)}")
