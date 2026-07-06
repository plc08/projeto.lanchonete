from dados.usuario_repository import UsuarioRepository
from negocio.usuario_service import UsuarioService

try:
    usuario_repository = UsuarioRepository()

    usuario_service = UsuarioService(usuario_repository)

    usuario = usuario_service.cadastrar_usuario(
        nome="Administrador",
        login="admin2",
        senha="123456",
        cargo="Gerente"
    )

    print("Usuário cadastrado com sucesso!")
    print(f"ID: {usuario.id}")

except Exception as erro:
    print("Erro:")
    print(erro)