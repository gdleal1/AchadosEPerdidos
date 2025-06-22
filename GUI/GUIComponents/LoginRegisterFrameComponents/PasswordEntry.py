import customtkinter as ck

class PasswordEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Senha", show="*", **kwargs)