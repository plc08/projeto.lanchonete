import customtkinter as ctk
from tkinter import messagebox

from dados.mesa_repository import MesaRepository
from negocio.mesa_service import MesaService


class TelaMesas(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        self.repository = MesaRepository()
        self.service = MesaService(self.repository)

        self.criar_componentes()
        self.listar_mesas()

    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Mesas",
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
            text="Nova Mesa",
            command=self.nova_mesa
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar_mesas
        ).pack(side="left", padx=10)

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

    def listar_mesas(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        mesas = self.service.listar_mesas()

        if not mesas:
            ctk.CTkLabel(
                self.lista,
                text="Nenhuma mesa cadastrada."
            ).pack(pady=20)
            return

        for mesa in mesas:

            card = ctk.CTkFrame(self.lista)

            card.pack(
                fill="x",
                padx=10,
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=f"Mesa {mesa.numero}",
                font=("Arial",18,"bold")
            ).pack(
                side="left",
                padx=20,
                pady=15
            )

            cor = "green" if mesa.status == "Livre" else "red"

            ctk.CTkLabel(
                card,
                text=mesa.status,
                text_color=cor,
                font=("Arial",16,"bold")
            ).pack(
                side="right",
                padx=20
            )

            if mesa.status == "Livre":

                ctk.CTkButton(
                    card,
                    text="Ocupar",
                    width=100,
                    command=lambda m=mesa: self.ocupar_mesa(m)
                ).pack(side="right", padx=10)

            else:

                ctk.CTkButton(
                    card,
                    text="Liberar",
                    width=100,
                    command=lambda m=mesa: self.liberar_mesa(m)
                ).pack(side="right", padx=10)

    def nova_mesa(self):

        janela = ctk.CTkToplevel(self)

        janela.title("Nova Mesa")
        janela.geometry("300x180")

        ctk.CTkLabel(
            janela,
            text="Número da Mesa"
        ).pack(pady=(20, 5))

        entrada = ctk.CTkEntry(
            janela,
            width=200
        )

        entrada.pack()

        def salvar():

            try:

                numero = int(entrada.get())

                self.service.cadastrar_mesa(numero)

                janela.destroy()

                self.listar_mesas()

                messagebox.showinfo(
                    "Sucesso",
                    "Mesa cadastrada com sucesso."
                )

            except Exception as erro:

                messagebox.showerror(
                    "Erro",
                    str(erro)
                )

        ctk.CTkButton(
            janela,
            text="Salvar",
            command=salvar
        ).pack(pady=20)

    def ocupar_mesa(self, mesa):

        self.service.atualizar_status(
            mesa.id,
            "Ocupada"
        )

        self.listar_mesas()

    def liberar_mesa(self, mesa):

        self.service.atualizar_status(
            mesa.id,
            "Livre"
        )

        self.listar_mesas()

