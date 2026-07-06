from dados.conexao_singleton import ConexaoSingleton
from dominio.item_pedido import ItemPedido


class ItemPedidoRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()

    def adicionar(self, item_pedido):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO itens_pedido
        (pedido_id, produto_id, quantidade)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            sql,
            (
                item_pedido.pedido_id,
                item_pedido.produto_id,
                item_pedido.quantidade
            )
        )

        self.conexao.commit()

        item_pedido.id = cursor.lastrowid

        cursor.close()

        return item_pedido

    def listar_por_pedido(self, pedido_id):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            pedido_id,
            produto_id,
            quantidade
        FROM itens_pedido
        WHERE pedido_id=%s
        """

        cursor.execute(sql, (pedido_id,))

        resultados = cursor.fetchall()

        cursor.close()

        itens = []

        for resultado in resultados:

            itens.append(
                ItemPedido(
                    id=resultado[0],
                    pedido_id=resultado[1],
                    produto_id=resultado[2],
                    quantidade=resultado[3]
                )
            )

        return itens