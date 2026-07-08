import customtkinter as ctk
from tkinter import messagebox

from dados.pagamento_repository import PagamentoRepository
from negocio.pagamento_service import PagamentoService

from dados.pedido_repository import PedidoRepository
from negocio.pedido_service import PedidoService

from dados.item_pedido_repository import ItemPedidoRepository
from negocio.item_pedido_service import ItemPedidoService

from dados.produto_repository import ProdutoRepository

from dados.mesa_repository import MesaRepository
from negocio.mesa_service import MesaService


class TelaPagamentos(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, fg_color="#F5F5F5")

        self.pagamento_repository = PagamentoRepository()
        self.pagamento_service = PagamentoService(
            self.pagamento_repository
        )

        self.pedido_repository = PedidoRepository()
        self.pedido_service = PedidoService(
            self.pedido_repository
        )

        self.item_repository = ItemPedidoRepository()
        self.produto_repository = ProdutoRepository()

        self.item_service = ItemPedidoService(
            self.item_repository,
            self.produto_repository
        )

        self.mesa_repository = MesaRepository()

        self.mesa_service = MesaService(
            self.mesa_repository
        )

        self.criar_componentes()

        self.listar_pedidos()
    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Pagamentos",
            font=("Arial", 30, "bold")
        )

        titulo.pack(pady=20)

        botoes = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        botoes.pack(pady=10)

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar_pedidos
        ).pack()

        self.lista = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=500
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
    def listar_pedidos(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        pedidos = self.pedido_service.listar_pedidos()

        pedidos = [
            pedido
            for pedido in pedidos
            if pedido.status != "Pago"
        ]

        if not pedidos:

            ctk.CTkLabel(
                self.lista,
                text="Nenhum pagamento pendente."
            ).pack(pady=30)

            return

        for pedido in pedidos:

            total = self.item_service.calcular_total(
                pedido.id
            )

            card = ctk.CTkFrame(self.lista)

            card.pack(
                fill="x",
                padx=10,
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=f"Pedido #{pedido.id}",
                width=120
            ).pack(
                side="left",
                padx=10
            )

            ctk.CTkLabel(
                card,
                text=f"Mesa {pedido.mesa_id}",
                width=120
            ).pack(side="left")

            ctk.CTkLabel(
                card,
                text=f"R$ {total:.2f}",
                width=150
            ).pack(side="left")

            ctk.CTkButton(
                card,
                text="Receber",
                command=lambda p=pedido, t=total: self.receber_pagamento(
                    p,
                    t
                )
            ).pack(
                side="right",
                padx=10
            )
    def receber_pagamento(self, pedido, total):

        resposta = messagebox.askyesno(
            "Pagamento",
            f"Confirmar pagamento de R$ {total:.2f}?"
        )

        if not resposta:
            return

        self.pagamento_service.registrar_pagamento(
            pedido.id,
            total
        )

        self.pedido_service.atualizar_status(
            pedido.id,
            "Pago"
        )

        self.mesa_service.atualizar_status(
            pedido.mesa_id,
            "Livre"
        )

        self.listar_pedidos()

        messagebox.showinfo(
            "Sucesso",
            "Pagamento realizado."
        )
    def mostrar_pagamentos(self):

        self.titulo_topo.configure(
            text="Pagamentos"
        )

        self.limpar_corpo()

        tela = TelaPagamentos(
            self.corpo
        )

        tela.pack(
            fill="both",
            expand=True
        )