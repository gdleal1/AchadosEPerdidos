import customtkinter as ck

class LocationField(ck.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, placeholder_text="Ex: Centro", **kwargs)
        self.grid(row=3, column=2, sticky="ew")