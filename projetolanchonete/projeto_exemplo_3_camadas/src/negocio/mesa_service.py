from dominio.mesa import Mesa


class MesaService:

    def __init__(self, mesa_repository):
        self.mesa_repository = mesa_repository

    def cadastrar_mesa(self, numero):

        if numero <= 0:
            raise ValueError("Número inválido.")

        mesa = Mesa(
            id=None,
            numero=numero
        )

        return self.mesa_repository.adicionar(mesa)

    def listar_mesas(self):

        return self.mesa_repository.listar()