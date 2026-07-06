from dados.conexao_singleton import ConexaoSingleton
from dominio.produto import Produto


class ProdutoRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()

    def adicionar(self, produto):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO produtos
        (nome, preco)
        VALUES (%s, %s)
        """

        cursor.execute(
            sql,
            (
                produto.nome,
                produto.preco
            )
        )

        self.conexao.commit()

        produto.id = cursor.lastrowid

        cursor.close()

        return produto

    def listar(self):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            nome,
            preco
        FROM produtos
        ORDER BY nome
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()

        produtos = []

        for resultado in resultados:

            produtos.append(
                Produto(
                    id=resultado[0],
                    nome=resultado[1],
                    preco=resultado[2]
                )
            )

        return produtos

    def buscar_por_id(self, id_produto):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            nome,
            preco
        FROM produtos
        WHERE id = %s
        """

        cursor.execute(sql, (id_produto,))

        resultado = cursor.fetchone()

        cursor.close()

        if resultado is None:
            return None

        return Produto(
            id=resultado[0],
            nome=resultado[1],
            preco=resultado[2]
        )

    def atualizar(self, produto):

        cursor = self.conexao.cursor()

        sql = """
        UPDATE produtos
        SET
            nome = %s,
            preco = %s
        WHERE id = %s
        """

        cursor.execute(
            sql,
            (
                produto.nome,
                produto.preco,
                produto.id
            )
        )

        self.conexao.commit()

        cursor.close()

    def remover(self, id_produto):

        cursor = self.conexao.cursor()

        sql = """
        DELETE FROM produtos
        WHERE id = %s
        """

        cursor.execute(sql, (id_produto,))

        self.conexao.commit()

        cursor.close()