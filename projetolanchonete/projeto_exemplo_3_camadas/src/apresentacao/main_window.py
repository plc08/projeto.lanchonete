import customtkinter as ctk

from apresentacao.tela_dashboard import TelaDashboard
from apresentacao.tela_produtos import TelaProdutos
from apresentacao.tela_mesas import TelaMesas
from apresentacao.tela_pedidos import TelaPedidos


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema da Lanchonete")
        self.geometry("1200x700")
        self.minsize(1000, 650)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.criar_layout()

    def criar_layout(self):

        # ================= MENU =================

        self.menu = ctk.CTkFrame(
            self,
            width=220,
            fg_color="#1F2937",
            corner_radius=0
        )

        self.menu.pack(side="left", fill="y")

        titulo = ctk.CTkLabel(
            self.menu,
            text="🍔 Lanchonete",
            font=("Arial", 22, "bold"),
            text_color="white"
        )

        titulo.pack(pady=(30, 40))

        self.btn_dashboard = ctk.CTkButton(
            self.menu,
            text="🏠 Dashboard",
            width=180,
            command=self.mostrar_dashboard
        )

        self.btn_dashboard.pack(pady=8)

        self.btn_produtos = ctk.CTkButton(
            self.menu,
            text="🍔 Produtos",
            width=180,
            command=self.mostrar_produtos
        )

        self.btn_produtos.pack(pady=8)

        self.btn_mesas = ctk.CTkButton(
            self.menu,
            text="🪑 Mesas",
            width=180,
            command=self.mostrar_mesas
        )

        self.btn_mesas.pack(pady=8)

        self.btn_pedidos = ctk.CTkButton(
            self.menu,
            text="📋 Pedidos",
            width=180,
            command=self.mostrar_pedidos
        )

        self.btn_pedidos.pack(pady=8)

        self.btn_pagamentos = ctk.CTkButton(
            self.menu,
            text="💳 Pagamentos",
            width=180,
            command=self.mostrar_pagamentos
        )

        self.btn_pagamentos.pack(pady=8)

        self.btn_usuarios = ctk.CTkButton(
            self.menu,
            text="👤 Usuários",
            width=180,
            command=self.mostrar_usuarios
        )

        self.btn_usuarios.pack(pady=8)

        self.btn_sair = ctk.CTkButton(
            self.menu,
            text="🚪 Sair",
            width=180,
            fg_color="#DC2626",
            hover_color="#B91C1C",
            command=self.destroy
        )

        self.btn_sair.pack(side="bottom", pady=30)

        # ================= CONTEÚDO =================

        self.conteudo = ctk.CTkFrame(
            self,
            fg_color="#F5F5F5"
        )

        self.conteudo.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.topo = ctk.CTkFrame(
            self.conteudo,
            height=70,
            fg_color="white"
        )

        self.topo.pack(fill="x")

        self.titulo_topo = ctk.CTkLabel(
            self.topo,
            text="Dashboard",
            font=("Arial", 24, "bold")
        )

        self.titulo_topo.pack(
            side="left",
            padx=25
        )

        usuario = ctk.CTkLabel(
            self.topo,
            text="Administrador",
            font=("Arial", 15)
        )

        usuario.pack(
            side="right",
            padx=25
        )

        self.corpo = ctk.CTkFrame(
            self.conteudo,
            fg_color="#F5F5F5"
        )

        self.corpo.pack(
            fill="both",
            expand=True
        )

        self.mostrar_dashboard()

    # =========================================

    def limpar_corpo(self):

        for widget in self.corpo.winfo_children():
            widget.destroy()

    # =========================================

    def mostrar_dashboard(self):

        self.titulo_topo.configure(text="Dashboard")

        self.limpar_corpo()

        tela = TelaDashboard(self.corpo)

        tela.pack(
            fill="both",
            expand=True
        )

    # =========================================

    def mostrar_produtos(self):

        self.titulo_topo.configure(text="Produtos")

        self.limpar_corpo()

        tela = TelaProdutos(self.corpo)

        tela.pack(
            fill="both",
            expand=True
        )

    # =========================================

    def mostrar_mesas(self):

        self.titulo_topo.configure(text="Mesas")

        self.limpar_corpo()

        tela = TelaMesas(self.corpo)

        tela.pack(
            fill="both",
            expand=True
        )

    # =========================================

    def mostrar_pedidos(self):
     self.titulo_topo.configure(
        text="Pedidos"
    )

    self.limpar_corpo()

    tela = TelaPedidos(
        self.corpo
    )

    tela.pack(
        fill="both",
        expand=True
    )
    # =========================================

    def mostrar_pagamentos(self):

        self.titulo_topo.configure(text="Pagamentos")

        self.limpar_corpo()

        ctk.CTkLabel(
            self.corpo,
            text="Tela de Pagamentos",
            font=("Arial", 28, "bold")
        ).pack(pady=50)

    # =========================================

    def mostrar_usuarios(self):

        self.titulo_topo.configure(text="Usuários")

        self.limpar_corpo()

        ctk.CTkLabel(
            self.corpo,
            text="Tela de Usuários",
            font=("Arial", 28, "bold")
        ).pack(pady=50)