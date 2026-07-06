from dominio.pedido import Pedido

class PedidoService:

    def __init__(self, pedido_repository):
        self.pedido_repository = pedido_repository

    def cadastrar_pedido(self, mesa_id):

        if mesa_id <= 0:
            raise ValueError("Mesa inválida.")

        pedido = Pedido(
            id=None,
            mesa_id=mesa_id,
            status="Pendente"
        )

        return self.pedido_repository.adicionar(pedido)
    def atualizar_status(self, id_pedido, novo_status):

        if id_pedido <= 0:
            raise ValueError("Pedido inválido.")

        status_validos = [
            "Pendente",
            "Preparando",
            "Pronto",
            "Pago"
        ]

        if novo_status not in status_validos:
            raise ValueError("Status inválido.")

        return self.pedido_repository.atualizar_status(
            id_pedido,
            novo_status
        )
    
    def listar_pedidos(self):

     return self.pedido_repository.listar()