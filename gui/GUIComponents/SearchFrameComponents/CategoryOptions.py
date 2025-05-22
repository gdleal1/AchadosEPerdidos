import customtkinter as ck

class CategoryOptions(ck.CTkComboBox):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            values=[
                "Todos",
                "Roupas",
                "Eletrônicos",
                "Documentos pessoais",
                "Acessórios e itens pessoais",
                "Materiais de escritório",
                "Outros"
            ],
            **kwargs
        )
        self.set("Categorias")
        self.bind("<Key>", lambda e: "break")