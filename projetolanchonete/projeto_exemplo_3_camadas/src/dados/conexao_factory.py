import mysql.connector


class ConexaoFactory:

    @staticmethod
    def criar_conexao():

        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="P4022",
            database="lanchonete"
        )

        return conexao