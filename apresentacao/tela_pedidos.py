import customtkinter as ctk
from tkinter import messagebox

from dados.pedido_repository import PedidoRepository
from negocio.pedido_service import PedidoService

from dados.mesa_repository import MesaRepository
from negocio.mesa_service import MesaService

from dados.produto_repository import ProdutoRepository

from dados.item_pedido_repository import ItemPedidoRepository
from negocio.item_pedido_service import ItemPedidoService
from dados.mesa_repository import MesaRepository


class TelaPedidos(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")

        self.repository = PedidoRepository()
        self.service = PedidoService(self.repository)

        self.mesa_repository = MesaRepository()
        self.mesa_service = MesaService(self.mesa_repository)
        self.mesas = {}

        self.produto_repository = ProdutoRepository()

        self.item_repository = ItemPedidoRepository()
        self.item_service = ItemPedidoService(
            self.item_repository,
            self.produto_repository
        )

        self.criar_componentes()
        self.listar_pedidos()

    def criar_componentes(self):

        titulo = ctk.CTkLabel(
            self,
            text="Pedidos",
            font=("Arial",30,"bold")
        )

        titulo.pack(pady=20)

        botoes = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        botoes.pack(pady=10)

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
        self.mesas = {}

    for mesa in self.mesa_repository.listar():
        self.mesas[mesa.id] = mesa.numero

        pedidos = self.service.listar_pedidos()

        if not pedidos:

            ctk.CTkLabel(
                self.lista,
                text="Nenhum pedido cadastrado."
            ).pack(pady=20)

            return

        for pedido in pedidos:

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
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                card,
                text=pedido.status,
                width=120
            ).pack(
                side="left"
            )

            ctk.CTkButton(
                card,
                text="Itens",
                width=90,
                command=lambda p=pedido: self.abrir_itens(p)
            ).pack(
                side="right",
                padx=10
            )

            if pedido.status == "Pendente":

                ctk.CTkButton(
                    card,
                    text="Preparar",
                    command=lambda p=pedido: self.alterar_status(
                        p,
                        "Preparando"
                    )
                ).pack(side="right", padx=5)

            elif pedido.status == "Preparando":

                ctk.CTkButton(
                    card,
                    text="Pronto",
                    command=lambda p=pedido: self.alterar_status(
                        p,
                        "Pronto"
                    )
                ).pack(side="right", padx=5)

            elif pedido.status == "Pronto":

                ctk.CTkButton(
                    card,
                    text="Receber",
                    command=lambda p=pedido: self.finalizar_pedido(p)
                ).pack(side="right", padx=5)
    def novo_pedido(self):

        mesas = self.mesa_service.listar_livres()

        if not mesas:
            messagebox.showwarning(
                "Aviso",
                "Não existem mesas livres."
            )
            return

        janela = ctk.CTkToplevel(self)

        janela.title("Novo Pedido")
        janela.geometry("350x220")

        ctk.CTkLabel(
            janela,
            text="Escolha a Mesa"
        ).pack(pady=(20, 10))

        valores = [
            f"Mesa {mesa.numero}"
            for mesa in mesas
        ]

        combo = ctk.CTkComboBox(
            janela,
            values=valores,
            width=220
        )

        combo.pack()

        combo.set(valores[0])

        def salvar():

            indice = valores.index(combo.get())

            mesa = mesas[indice]

            self.service.cadastrar_pedido(
                mesa.id
            )

            self.mesa_service.atualizar_status(
                mesa.id,
                "Ocupada"
            )

            janela.destroy()

            self.listar_pedidos()

            messagebox.showinfo(
                "Sucesso",
                "Pedido criado com sucesso."
            )

        ctk.CTkButton(
            janela,
            text="Salvar",
            command=salvar
        ).pack(pady=30)
    def finalizar_pedido(self, pedido):

        resposta = messagebox.askyesno(
            "Finalizar Pedido",
            "Deseja finalizar este pedido?"
        )

        if not resposta:
            return

        self.service.atualizar_status(
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
            "Pedido finalizado."
        )
    def alterar_status(self, pedido, novo_status):

        self.service.atualizar_status(
            pedido.id,
            novo_status
        )

        self.listar_pedidos()
    def abrir_itens(self, pedido):

        janela = ctk.CTkToplevel(self)

        janela.title(f"Itens do Pedido #{pedido.id}")
        janela.geometry("700x500")

        ctk.CTkLabel(
            janela,
            text=f"Pedido #{pedido.id}",
            font=("Arial", 22, "bold")
        ).pack(pady=15)

        lista = ctk.CTkScrollableFrame(
            janela,
            width=620,
            height=250
        )

        lista.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        itens = self.item_service.listar_itens(
            pedido.id
        )

        produtos = {
            produto.id: produto.nome
            for produto in self.produto_repository.listar()
        }

        if not itens:

            ctk.CTkLabel(
                lista,
                text="Nenhum produto adicionado."
            ).pack(pady=20)

        else:

            for item in itens:

                nome = produtos.get(
                    item.produto_id,
                    "Produto"
                )

                ctk.CTkLabel(
                    lista,
                    text=f"{nome} - Quantidade: {item.quantidade}"
                ).pack(
                    anchor="w",
                    padx=15,
                    pady=5
                )

        total = self.item_service.calcular_total(
            pedido.id
        )

        ctk.CTkLabel(
            janela,
            text=f"Total: R$ {total:.2f}",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        ctk.CTkButton(
            janela,
            text="Adicionar Produto",
            command=lambda: self.adicionar_item(
                pedido,
                janela
            )
        ).pack(pady=15)
    def adicionar_item(self, pedido, janela_pedido):

        janela = ctk.CTkToplevel(self)

        janela.title("Adicionar Produto")
        janela.geometry("400x320")

        produtos = self.produto_repository.listar()

        if not produtos:

            messagebox.showwarning(
                "Aviso",
                "Não existem produtos cadastrados."
            )

            janela.destroy()

            return

        nomes = [
            f"{produto.id} - {produto.nome}"
            for produto in produtos
        ]

        ctk.CTkLabel(
            janela,
            text="Produto"
        ).pack(pady=(20, 5))

        combo = ctk.CTkComboBox(
            janela,
            values=nomes,
            width=250
        )

        combo.pack()

        combo.set(nomes[0])

        ctk.CTkLabel(
            janela,
            text="Quantidade"
        ).pack(pady=(20, 5))

        entrada_quantidade = ctk.CTkEntry(
            janela,
            width=250
        )

        entrada_quantidade.pack()

        entrada_quantidade.insert(0, "1")

        def salvar():

            try:

                produto_id = int(
                    combo.get().split(" - ")[0]
                )

                quantidade = int(
                    entrada_quantidade.get()
                )

                self.item_service.adicionar_item(
                    pedido.id,
                    produto_id,
                    quantidade
                )

                janela.destroy()
                janela_pedido.destroy()

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
    def alterar_status(self, pedido, status):

        self.service.atualizar_status(
            pedido.id,
            status
        )

        self.listar_pedidos()
        