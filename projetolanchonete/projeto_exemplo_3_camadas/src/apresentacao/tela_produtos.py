import customtkinter as ctk
from tkinter import messagebox

from dados.produto_repository import ProdutoRepository
from negocio.produto_service import ProdutoService


class TelaProdutos(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        self.repository = ProdutoRepository()
        self.service = ProdutoService(self.repository)

        self.criar_componentes()
        self.listar_produtos()

    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Produtos",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=20)

        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(pady=10)

        ctk.CTkButton(
            frame_botoes,
            text="Novo Produto",
            command=self.novo_produto
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            frame_botoes,
            text="Atualizar",
            command=self.listar_produtos
        ).pack(side="left", padx=10)

        self.lista = ctk.CTkScrollableFrame(
            self,
            width=850,
            height=450
        )
        self.lista.pack(fill="both", expand=True, padx=20, pady=20)

    def listar_produtos(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        produtos = self.service.listar_produtos()

        if not produtos:

            ctk.CTkLabel(
                self.lista,
                text="Nenhum produto cadastrado."
            ).pack(pady=30)

            return

        for produto in produtos:

            card = ctk.CTkFrame(self.lista)
            card.pack(fill="x", padx=10, pady=8)

            ctk.CTkLabel(
                card,
                text=f"{produto.nome}"
            ).pack(side="left", padx=20)

            ctk.CTkLabel(
                card,
                text=f"R$ {produto.preco:.2f}"
            ).pack(side="left", padx=20)

            ctk.CTkButton(
                card,
                text="Editar",
                width=80,
                command=lambda p=produto: self.editar_produto(p)
            ).pack(side="right", padx=5)

            ctk.CTkButton(
                card,
                text="Excluir",
                width=80,
                fg_color="red",
                hover_color="#AA0000",
                command=lambda p=produto: self.excluir_produto(p)
            ).pack(side="right", padx=5)

    def novo_produto(self):

        janela = ctk.CTkToplevel(self)
        janela.title("Novo Produto")
        janela.geometry("350x250")

        ctk.CTkLabel(janela, text="Nome").pack(pady=(20,5))
        nome = ctk.CTkEntry(janela, width=250)
        nome.pack()

        ctk.CTkLabel(janela, text="Preço").pack(pady=(15,5))
        preco = ctk.CTkEntry(janela, width=250)
        preco.pack()

        def salvar():

            try:

                self.service.cadastrar_produto(
                    nome.get(),
                    float(preco.get())
                )

                janela.destroy()

                self.listar_produtos()

                messagebox.showinfo(
                    "Sucesso",
                    "Produto cadastrado."
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

    def editar_produto(self, produto):

        janela = ctk.CTkToplevel(self)
        janela.title("Editar Produto")
        janela.geometry("350x250")

        ctk.CTkLabel(janela, text="Nome").pack(pady=(20,5))
        nome = ctk.CTkEntry(janela, width=250)
        nome.insert(0, produto.nome)
        nome.pack()

        ctk.CTkLabel(janela, text="Preço").pack(pady=(15,5))
        preco = ctk.CTkEntry(janela, width=250)
        preco.insert(0, str(produto.preco))
        preco.pack()

        def salvar():

            try:

                self.service.atualizar_produto(
                    produto.id,
                    nome.get(),
                    float(preco.get())
                )

                janela.destroy()

                self.listar_produtos()

                messagebox.showinfo(
                    "Sucesso",
                    "Produto atualizado."
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

    def excluir_produto(self, produto):

        if messagebox.askyesno(
            "Excluir",
            f"Deseja excluir '{produto.nome}'?"
        ):

            self.service.remover_produto(produto.id)

            self.listar_produtos()

            messagebox.showinfo(
                "Sucesso",
                "Produto removido."
            )