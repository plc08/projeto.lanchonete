import customtkinter as ctk

from dados.mesa_repository import MesaRepository
from negocio.mesa_service import MesaService


class TelaMesas(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.repository = MesaRepository()
        self.service = MesaService(self.repository)

        titulo = ctk.CTkLabel(
            self,
            text="Mesas",
            font=("Arial",28,"bold")
        )

        titulo.pack(pady=20)

        self.lista = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=500
        )

        self.lista.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.listar()

    def listar(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        mesas = self.service.listar_mesas()

        for mesa in mesas:

            card = ctk.CTkFrame(self.lista)

            card.pack(
                fill="x",
                padx=10,
                pady=8
            )

            ctk.CTkLabel(
                card,
                text=f"Mesa {mesa.numero}",
                font=("Arial",18)
            ).pack(
                side="left",
                padx=20,
                pady=15
            )