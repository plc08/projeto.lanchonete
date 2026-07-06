class Usuario:
    def __init__(self, id, nome, login, senha, cargo, ativo=True):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha
        self.cargo = cargo
        self.ativo = ativo