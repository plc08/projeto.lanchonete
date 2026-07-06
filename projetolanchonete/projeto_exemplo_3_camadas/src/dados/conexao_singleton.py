from dados.conexao_factory import ConexaoFactory


class ConexaoSingleton:

    _conexao = None

    @classmethod
    def get_conexao(cls):

        if cls._conexao is None:
            cls._conexao = ConexaoFactory.criar_conexao()

        return cls._conexao