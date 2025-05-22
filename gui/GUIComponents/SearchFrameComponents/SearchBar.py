import customtkinter as ck

class SearchBar(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Digite a descrição do item ...", **kwargs)
