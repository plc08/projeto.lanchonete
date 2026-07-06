from dados.conexao_singleton import ConexaoSingleton
from dominio.pagamento import Pagamento


class PagamentoRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()

    def adicionar(self, pagamento):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO pagamentos
        (pedido_id, valor)
        VALUES (%s, %s)
        """

        cursor.execute(
            sql,
            (
                pagamento.pedido_id,
                pagamento.valor
            )
        )

        self.conexao.commit()

        pagamento.id = cursor.lastrowid

        cursor.close()

        return pagamento

    def listar(self):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            pedido_id,
            valor
        FROM pagamentos
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()

        pagamentos = []

        for resultado in resultados:

            pagamentos.append(
                Pagamento(
                    id=resultado[0],
                    pedido_id=resultado[1],
                    valor=resultado[2]
                )
            )

        return pagamentos