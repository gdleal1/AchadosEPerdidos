import customtkinter as ck

class CategoryOptions(ck.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=[
                "Todos",
                "Vestuário",
                "Eletrônicos",
                "Documentos",
                "Acessórios",
                "Materiais de escritório",
                "Materiais escolares",
                "Chaves",
                "Outros"
            ],
            **kwargs
        )
        self.set("Categorias")
        self.bind("<Key>", lambda e: "break")