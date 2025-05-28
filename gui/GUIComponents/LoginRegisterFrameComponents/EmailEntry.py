import customtkinter as ck

class EmailEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="E-mail", **kwargs)