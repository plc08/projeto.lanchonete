from dados.conexao_singleton import ConexaoSingleton
from dominio.pedido import Pedido


class PedidoRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()

    def adicionar(self, pedido):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO pedidos
        (mesa_id, status)
        VALUES (%s, %s)
        """

        cursor.execute(
            sql,
            (
                pedido.mesa_id,
                pedido.status
            )
        )

        self.conexao.commit()

        pedido.id = cursor.lastrowid

        cursor.close()

        return pedido

    def atualizar_status(self, id_pedido, novo_status):

        cursor = self.conexao.cursor()

        sql = """
        UPDATE pedidos
        SET status = %s
        WHERE id = %s
        """

        cursor.execute(
            sql,
            (
                novo_status,
                id_pedido
            )
        )

        self.conexao.commit()

        cursor.close()

    def listar(self):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            mesa_id,
            status
        FROM pedidos
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()

        pedidos = []

        for resultado in resultados:

            pedidos.append(
                Pedido(
                    id=resultado[0],
                    mesa_id=resultado[1],
                    status=resultado[2]
                )
            )

        return pedidos