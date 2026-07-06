from dados.conexao_singleton import ConexaoSingleton
from dominio.mesa import Mesa


class MesaRepository:

    def __init__(self):
        self.conexao = ConexaoSingleton.get_conexao()

    def adicionar(self, mesa):

        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO mesas
        (numero)
        VALUES (%s)
        """

        cursor.execute(
            sql,
            (
                mesa.numero,
            )
        )

        self.conexao.commit()

        mesa.id = cursor.lastrowid

        cursor.close()

        return mesa

    def listar(self):

        cursor = self.conexao.cursor()

        sql = """
        SELECT
            id,
            numero
        FROM mesas
        ORDER BY numero
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        cursor.close()

        mesas = []

        for resultado in resultados:

            mesas.append(
                Mesa(
                    id=resultado[0],
                    numero=resultado[1]
                )
            )

        return mesas