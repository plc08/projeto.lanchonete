import customtkinter as ctk
from tkinter import messagebox

from dados.pedido_repository import PedidoRepository
from negocio.pedido_service import PedidoService
from dados.item_pedido_repository import ItemPedidoRepository
from negocio.item_pedido_service import ItemPedidoService

from dados.produto_repository import ProdutoRepository


class TelaPedidos(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, fg_color="#F5F5F5")

        self.repository = PedidoRepository()
        self.service = PedidoService(self.repository)

        self.criar_componentes()

        self.listar_pedidos()

    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Pedidos",
            font=("Arial",28,"bold")
        )

        titulo.pack(pady=20)

        botoes = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        botoes.pack()

        ctk.CTkButton(
            botoes,
            text="Novo Pedido",
            command=self.novo_pedido
        ).pack(side="left", padx=10)

        ctk.CTkButton(
            botoes,
            text="Atualizar",
            command=self.listar_pedidos
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

    def listar_pedidos(self):
     for widget in self.lista.winfo_children():
        widget.destroy()

    pedidos = self.service.listar_pedidos()

    if not pedidos:

        ctk.CTkLabel(
            self.lista,
            text="Nenhum pedido cadastrado."
        ).pack(pady=30)

    

    for pedido in pedidos:

        card = ctk.CTkFrame(self.lista)

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        ctk.CTkLabel(
            card,
            text=f"Pedido #{pedido.id}"
        ).pack(
            side="left",
            padx=20,
            pady=15
        )

        ctk.CTkLabel(
            card,
            text=f"Mesa {pedido.mesa_id}"
        ).pack(
            side="left",
            padx=20
        )

        ctk.CTkLabel(
            card,
            text=pedido.status
        ).pack(
            side="right",
            padx=20
        )
        ctk.CTkButton(
          card,
          text="Itens",
          width=80,
         command=lambda p=pedido: self.abrir_itens(p)
 ).pack(
    side="right",
    padx=10
 

    def novo_pedido(self):

      janela = ctk.CTkToplevel(self)

      janela.title("Novo Pedido")

      janela.geometry("300x220")

    ctk.CTkLabel(
        janela,
        text="Número da Mesa"
    ).pack(pady=(20,5))

    mesa = ctk.CTkEntry(janela)

    mesa.pack()

    def salvar():

        try:

            self.service.cadastrar_pedido(
                int(mesa.get())
            )

            janela.destroy()

            self.listar_pedidos()

            messagebox.showinfo(
                "Sucesso",
                "Pedido criado!"
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

    def abrir_itens(self, pedido):

     janela = ctk.CTkToplevel(self)

     janela.title(f"Pedido #{pedido.id}")

     janela.geometry("700x500")

    ctk.CTkLabel(
        janela,
        text=f"Pedido {pedido.id} - Mesa {pedido.mesa_id}",
        font=("Arial",22,"bold")
    ).pack(pady=20)
    ctk.CTkButton(
        janela,
        text="Adicionar Produto",
        command=lambda: self.adicionar_item(pedido, lista)
).pack(pady=10)

    lista = ctk.CTkScrollableFrame(
        janela,
        width=620,
        height=250
    )

    lista.pack(padx=20, pady=10)

    itens = self.item_service.listar_itens(pedido.id)

    if not itens:

        ctk.CTkLabel(
            lista,
            text="Nenhum produto adicionado."
        ).pack(pady=20)

    else:

        produtos = {
            produto.id: produto.nome
            for produto in self.produto_repository.listar()
        }

        for item in itens:

            nome = produtos.get(
                item.produto_id,
                "Produto"
            )

            ctk.CTkLabel(
                lista,
                text=f"{nome} - Quantidade: {item.quantidade}"
            ).pack(anchor="w", padx=15, pady=5)

    def adicionar_item(self, pedido, lista_frame):

     janela = ctk.CTkToplevel(self)

     janela.title("Adicionar Produto")

     janela.geometry("400x320")

    produtos = self.produto_repository.listar()

    nomes = [
        f"{produto.id} - {produto.nome}"
        for produto in produtos
    ]

    ctk.CTkLabel(
        janela,
        text="Produto"
    ).pack(pady=(20,5))

    combo = ctk.CTkComboBox(
        janela,
        values=nomes,
        width=250
    )

    combo.pack()

    ctk.CTkLabel(
        janela,
        text="Quantidade"
    ).pack(pady=(20,5))

    quantidade = ctk.CTkEntry(
        janela,
        width=250
    )

    quantidade.pack()

    def salvar():

        try:

            produto_id = int(
                combo.get().split(" - ")[0]
            )

            self.item_service.adicionar_item(
                pedido.id,
                produto_id,
                int(quantidade.get())
            )

            janela.destroy()

            self.abrir_itens(pedido)

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    ctk.CTkButton(
        janela,
        text="Salvar",
        command=salvar
    ).pack(pady=30)