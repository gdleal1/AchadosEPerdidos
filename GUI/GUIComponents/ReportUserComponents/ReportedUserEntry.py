import customtkinter as ck

class ReportedUserEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Usuário a reportar", **kwargs)