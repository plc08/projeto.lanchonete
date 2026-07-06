from dominio.usuario import Usuario
from dados.conexao_singleton import ConexaoSingleton


class UsuarioRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()
        
    def adicionar(self, usuario):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO usuarios
        (nome, login, senha, cargo, ativo)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                usuario.nome,
                usuario.login,
                usuario.senha,
                usuario.cargo,
                usuario.ativo
            )
        )

        self.conexao.commit()

        usuario.id = cursor.lastrowid

        cursor.close()

        return usuario

    def buscar_por_login(self, login):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            nome,
            login,
            senha,
            cargo,
            ativo
        FROM usuarios
        WHERE login = %s
        """

        cursor.execute(sql, (login,))

        resultado = cursor.fetchone()

        cursor.close()

        if resultado is None:
            return None

        return Usuario(
            id=resultado[0],
            nome=resultado[1],
            login=resultado[2],
            senha=resultado[3],
            cargo=resultado[4],
            ativo=resultado[5]
        )