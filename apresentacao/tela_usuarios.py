import customtkinter as ctk
from tkinter import messagebox

from dados.usuario_repository import UsuarioRepository
from negocio.usuario_service import UsuarioService


class TelaUsuarios(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        self.repository = UsuarioRepository()
        self.service = UsuarioService(self.repository)

        self.criar_componentes()
        self.listar_usuarios()
    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Usuários",
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
            text="Novo Usuário",
            command=self.novo_usuario
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar_usuarios
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
    def listar_usuarios(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        usuarios = self.repository.listar()

        if not usuarios:

            ctk.CTkLabel(
                self.lista,
                text="Nenhum usuário cadastrado."
            ).pack(pady=30)

            return

        for usuario in usuarios:

            card = ctk.CTkFrame(self.lista)

            card.pack(
                fill="x",
                padx=10,
                pady=5
            )

            ctk.CTkLabel(
                card,
                text=usuario.nome,
                width=220
            ).pack(side="left", padx=15)

            ctk.CTkLabel(
                card,
                text=usuario.login,
                width=150
            ).pack(side="left")

            ctk.CTkLabel(
                card,
                text=usuario.cargo,
                width=150
            ).pack(side="left")

            status = "Ativo" if usuario.ativo else "Inativo"

            cor = "green" if usuario.ativo else "red"

            ctk.CTkLabel(
                card,
                text=status,
                text_color=cor,
                width=100
            ).pack(side="left")
        if usuario.ativo:

            ctk.CTkButton(
                card,
                text="Desativar",
                fg_color="red",
                command=lambda u=usuario: self.desativar_usuario(u)
            ).pack(side="right", padx=10)

        else:

            ctk.CTkButton(
                card,
                text="Ativar",
                fg_color="green",
                command=lambda u=usuario: self.ativar_usuario(u)
            ).pack(side="right", padx=10)
    def novo_usuario(self):

        janela = ctk.CTkToplevel(self)

        janela.title("Novo Usuário")
        janela.geometry("400x420")

        ctk.CTkLabel(
            janela,
            text="Nome"
        ).pack(pady=(15,5))

        nome = ctk.CTkEntry(janela, width=250)
        nome.pack()

        ctk.CTkLabel(
            janela,
            text="Login"
        ).pack(pady=(15,5))

        login = ctk.CTkEntry(janela, width=250)
        login.pack()

        ctk.CTkLabel(
            janela,
            text="Senha"
        ).pack(pady=(15,5))

        senha = ctk.CTkEntry(
            janela,
            width=250,
            show="*"
        )
        senha.pack()

        ctk.CTkLabel(
            janela,
            text="Cargo"
        ).pack(pady=(15,5))

        cargo = ctk.CTkComboBox(
            janela,
            width=250,
            values=[
                "Gerente",
                "Garçom",
                "Caixa",
                "Cozinheiro"
            ]
        )

        cargo.pack()

        cargo.set("Garçom")
        def salvar():

            try:

                self.service.cadastrar_usuario(
                    nome.get(),
                    login.get(),
                    senha.get(),
                    cargo.get()
                )

                janela.destroy()

                self.listar_usuarios()

                messagebox.showinfo(
                    "Sucesso",
                    "Usuário cadastrado."
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
        ).pack(pady=25)
    def desativar_usuario(self, usuario):

        self.repository.atualizar_status(
            usuario.id,
            False
        )

        self.listar_usuarios()


    def ativar_usuario(self, usuario):

        self.repository.atualizar_status(
            usuario.id,
            True
        )

        self.listar_usuarios()