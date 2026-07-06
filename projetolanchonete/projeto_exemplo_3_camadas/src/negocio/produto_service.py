from dominio.produto import Produto


class ProdutoService:

    def __init__(self, produto_repository):
        self.produto_repository = produto_repository

    def cadastrar_produto(self, nome, preco):

        if not nome.strip():
            raise ValueError("O nome do produto é obrigatório.")

        if preco <= 0:
            raise ValueError("Preço inválido.")

        produto = Produto(
            id=None,
            nome=nome,
            preco=preco
        )

        return self.produto_repository.adicionar(produto)

    def listar_produtos(self):

        return self.produto_repository.listar()

    def atualizar_produto(self, id_produto, nome, preco):

        if not nome.strip():
            raise ValueError("O nome é obrigatório.")

        if preco <= 0:
            raise ValueError("Preço inválido.")

        produto = Produto(
            id=id_produto,
            nome=nome,
            preco=preco
        )

        self.produto_repository.atualizar(produto)

    def remover_produto(self, id_produto):

        if id_produto <= 0:
            raise ValueError("Produto inválido.")

        self.produto_repository.remover(id_produto)

    def buscar_por_id(self, id_produto):

        return self.produto_repository.buscar_por_id(id_produto)