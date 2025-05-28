import customtkinter as ck

class CellphoneEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Telefone", **kwargs)