import customtkinter as ctk


class TelaDashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        titulo = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 30, "bold")
        )
        titulo.pack(pady=20)

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.pack(pady=20)

        self.criar_card(cards, "🍔 Produtos", "0", 0, 0)
        self.criar_card(cards, "🪑 Mesas", "0", 0, 1)
        self.criar_card(cards, "📋 Pedidos", "0", 1, 0)
        self.criar_card(cards, "💳 Pagamentos", "0", 1, 1)

    def criar_card(self, master, titulo, valor, linha, coluna):

        card = ctk.CTkFrame(
            master,
            width=250,
            height=140
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
            text=valor,
            font=("Arial",36,"bold")
        ).pack()