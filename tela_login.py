from tkinter import messagebox

from dados.usuario_repository import UsuarioRepository
from negocio.usuario_service import UsuarioService
from apresentacao.main_window import MainWindow

def entrar(self):

    try:

        login = self.entry_login.get()
        senha = self.entry_senha.get()

        self.service.autenticar(login, senha)

        self.destroy()

        app = MainWindow()
        app.mainloop()

    except Exception as erro:

        messagebox.showerror(
            "Erro",
            str(erro)
        )