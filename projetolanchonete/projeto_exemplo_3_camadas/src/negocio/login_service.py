from dominio.usuario import Usuario

class LoginService:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def autenticar(self, login, senha):

        if not login:
            raise ValueError("O login é obrigatório.")

        if not senha:
            raise ValueError("A senha é obrigatória.")
       
        usuario = self.usuario_repository.buscar_por_login(login)

        if usuario is None:
            raise ValueError("Usuário não encontrado.")

        if usuario.senha != senha:
            raise ValueError("Senha incorreta.")

        return usuario