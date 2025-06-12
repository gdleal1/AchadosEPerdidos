import customtkinter as ck

class NameEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Nome", **kwargs)