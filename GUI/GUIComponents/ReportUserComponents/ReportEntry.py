import customtkinter as ck

class ReportEntry(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Denúncia", **kwargs)