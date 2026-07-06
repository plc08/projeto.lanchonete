from dominio.pagamento import Pagamento


class PagamentoService:

    def __init__(self, pagamento_repository):
        self.pagamento_repository = pagamento_repository

    def registrar_pagamento(self, pedido_id, valor):

        if pedido_id <= 0:
            raise ValueError("Pedido inválido.")

        if valor <= 0:
            raise ValueError("Valor inválido.")

        pagamento = Pagamento(
            id=None,
            pedido_id=pedido_id,
            valor=valor
        )

        return self.pagamento_repository.adicionar(pagamento)