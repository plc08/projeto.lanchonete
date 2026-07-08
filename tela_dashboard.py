import customtkinter as ctk

from dados.produto_repository import ProdutoRepository
from dados.mesa_repository import MesaRepository
from dados.pedido_repository import PedidoRepository
from dados.pagamento_repository import PagamentoRepository


class TelaDashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        self.produto_repository = ProdutoRepository()
        self.mesa_repository = MesaRepository()
        self.pedido_repository = PedidoRepository()
        self.pagamento_repository = PagamentoRepository()

        self.criar_dashboard()

    def criar_dashboard(self):

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )

        titulo.pack(pady=20)

        cards = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cards.pack(pady=10)

        produtos = len(self.produto_repository.listar())
        mesas = len(self.mesa_repository.listar())
        pedidos = len(self.pedido_repository.listar())
        pagamentos = len(self.pagamento_repository.listar())

        self.criar_card(cards, "🍔 Produtos", produtos, 0, 0)
        self.criar_card(cards, "🪑 Mesas", mesas, 0, 1)
        self.criar_card(cards, "📋 Pedidos", pedidos, 1, 0)
        self.criar_card(cards, "💳 Pagamentos", pagamentos, 1, 1)

        self.criar_resumo()

    def criar_card(self, master, titulo, valor, linha, coluna):

        card = ctk.CTkFrame(
            master,
            width=250,
            height=140,
            corner_radius=15
        )

        card.grid(
            row=linha,
            column=coluna,
            padx=20,
            pady=20
        )

        card.grid_propagate(False)

        ctk.CTkLabel(
            card,
            text=titulo,
            font=("Arial",18,"bold")
        ).pack(pady=(25,10))

        ctk.CTkLabel(
            card,
            text=str(valor),
            font=("Arial",36,"bold")
        ).pack()

    def criar_resumo(self):

        frame = ctk.CTkFrame(self)

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        ctk.CTkLabel(
            frame,
            text="Resumo do Sistema",
            font=("Arial",22,"bold")
        ).pack(pady=15)

        mesas_livres = len(
            self.mesa_repository.listar_livres()
        )

        total_mesas = len(
            self.mesa_repository.listar()
        )

        pedidos = len(
            self.pedido_repository.listar()
        )

        pagamentos = len(
            self.pagamento_repository.listar()
        )

        texto = f"""
Mesas Livres: {mesas_livres}

Total de Mesas: {total_mesas}

Pedidos Registrados: {pedidos}

Pagamentos Efetuados: {pagamentos}
"""

        ctk.CTkLabel(
            frame,
            text=texto,
            justify="left",
            font=("Arial",17)
        ).pack(anchor="w", padx=25, pady=15)