import customtkinter as ck

class TitleEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Título", **kwargs)