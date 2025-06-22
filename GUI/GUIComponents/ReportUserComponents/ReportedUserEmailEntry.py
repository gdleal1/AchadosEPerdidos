import customtkinter as ck

class ReportedUserEmailEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Email do usuário a reportar", **kwargs)