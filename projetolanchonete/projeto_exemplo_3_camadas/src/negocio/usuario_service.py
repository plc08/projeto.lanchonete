from dominio.usuario import Usuario

class UsuarioService:

    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def cadastrar_usuario(self, nome, login, senha, cargo):

        if not nome:
            raise ValueError("O nome é obrigatório.")

        if not login:
            raise ValueError("O login é obrigatório.")

        if not senha:
            raise ValueError("A senha é obrigatória.")

        if not cargo:
            raise ValueError("O cargo é obrigatório.")
         
        usuario = Usuario(
            id=None,
            nome=nome,
            login=login,
            senha=senha,
            cargo=cargo,
            ativo=True
        )

        return self.usuario_repository.adicionar(usuario)
    
    def autenticar(self, login, senha):

    usuario = self.usuario_repository.buscar_por_login(login)

    if usuario is None:
        raise ValueError("Usuário não encontrado.")

    if usuario.senha != senha:
        raise ValueError("Senha incorreta.")

    if not usuario.ativo:
        raise ValueError("Usuário inativo.")

    return usuario