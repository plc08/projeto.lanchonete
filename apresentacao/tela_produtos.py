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

        botoes = ctk.CTkFrame(self, fg_color="transparent")
        botoes.pack(pady=10)

        ctk.CTkButton(
            botoes,
            text="Novo Produto",
            command=self.novo_produto
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            botoes,
            text="Atualizar Lista",
            command=self.listar_produtos
        ).pack(side="left", padx=10)

        self.lista = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=420
        )
        self.lista.pack(pady=20, padx=20, fill="both", expand=True)

    def listar_produtos(self):

        for widget in self.lista.winfo_children():
            widget.destroy()

        produtos = self.repository.listar()

        if not produtos:
            ctk.CTkLabel(
                self.lista,
                text="Nenhum produto cadastrado."
            ).pack(pady=20)
            return

        for produto in produtos:

            card = ctk.CTkFrame(self.lista)
            card.pack(fill="x", padx=10, pady=8)

            ctk.CTkLabel(card, text=produto.nome).pack(side="left", padx=10)
            ctk.CTkLabel(card, text=f"R$ {produto.preco:.2f}").pack(side="left")
        ctk.CTkButton(
            card,
            text="Editar",
            width=90,
            command=lambda p=produto: self.editar_produto(p)
        ).pack(side="right", padx=5)

        ctk.CTkButton(
            card,
            text="Excluir",
            width=90,
            fg_color="red",
            hover_color="#b00020",
            command=lambda p=produto: self.excluir_produto(p)
        ).pack(side="right", padx=5)
    def novo_produto(self):

        janela = ctk.CTkToplevel(self)
        janela.title("Novo Produto")
        janela.geometry("300x200")

        entry_nome = ctk.CTkEntry(janela)
        entry_nome.pack(pady=10)

        entry_preco = ctk.CTkEntry(janela)
        entry_preco.pack(pady=10)

        def salvar():
            try:
                self.service.cadastrar_produto(
                    entry_nome.get(),
                    float(entry_preco.get())
                )

                janela.destroy()
                self.listar_produtos()

            except Exception as e:
                messagebox.showerror("Erro", str(e))

        ctk.CTkButton(janela, text="Salvar", command=salvar).pack(pady=10)
        def excluir_produto(self, produto):

            resposta = messagebox.askyesno(
                "Excluir",
                f"Deseja excluir '{produto.nome}'?"
            )

            if not resposta:
                return

            self.repository.excluir(produto.id)

            self.listar_produtos()

            messagebox.showinfo(
                "Sucesso",
                "Produto excluído."
            )
def editar_produto(self, produto):

    janela = ctk.CTkToplevel(self)

    janela.title("Editar Produto")

    janela.geometry("400x320")

    ctk.CTkLabel(
        janela,
        text="Nome"
    ).pack(pady=(20,5))

    nome = ctk.CTkEntry(
        janela,
        width=250
    )

    nome.insert(0, produto.nome)

    nome.pack()

    ctk.CTkLabel(
        janela,
        text="Preço"
    ).pack(pady=(15,5))

    preco = ctk.CTkEntry(
        janela,
        width=250
    )

    preco.insert(0, str(produto.preco))

    preco.pack()