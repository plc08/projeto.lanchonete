from dominio.item_pedido import ItemPedido


class ItemPedidoService:

    def __init__(self, item_repository, produto_repository):

        self.item_repository = item_repository
        self.produto_repository = produto_repository

    def adicionar_item(self, pedido_id, produto_id, quantidade):

        if pedido_id <= 0:
            raise ValueError("Pedido inválido.")

        if produto_id <= 0:
            raise ValueError("Produto inválido.")

        if quantidade <= 0:
            raise ValueError("Quantidade inválida.")

        item = ItemPedido(
            id=None,
            pedido_id=pedido_id,
            produto_id=produto_id,
            quantidade=quantidade
        )

        return self.item_repository.adicionar(item)

    def listar_itens(self, pedido_id):

        return self.item_repository.listar_por_pedido(
            pedido_id
        )

    def calcular_total(self, pedido_id):

        itens = self.listar_itens(pedido_id)

        total = 0

        for item in itens:

            produto = self.produto_repository.buscar_por_id(
                item.produto_id
            )

            total += produto.preco * item.quantidade

        return total