import customtkinter as ck

class UsernameEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Nome de usuário", **kwargs)