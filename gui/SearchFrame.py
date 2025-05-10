import customtkinter as ck
from tkcalendar import DateEntry
from PIL import Image

class SearchFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0,1,2,3,4), weight=1)

        # Logo
        self.logoimage = ck.CTkImage(Image.open("gui/images/logo.png"),
                                  size=(480, 134))
        self.logo_label = ck.CTkLabel(self, text="", image=self.logoimage)
        self.logo_label.grid(row=0, column=0,columnspan=5, padx= 20, pady=10)

        # Frame title
        self.title_frame_label = ck.CTkLabel(self, text="===================================================== Buscar Itens Perdidos =====================================================", font=("Arial", 20))
        self.title_frame_label.grid(row=1, column=0, columnspan=5,pady=(20, 10))

        # Search bar
        self.search_entry = ck.CTkEntry(self, placeholder_text="Digite o nome do item ...")
        self.search_entry.grid(row=2, column=0,columnspan=4,padx=20,pady=20,sticky="ew")

        # Search button
        self.search_button = ck.CTkButton(self, text="Buscar", command=self.search_button_action)
        self.search_button.grid(row=2, column=4, padx=20, pady=20, sticky="ew")

        # Cartegory options
        self.category_combobox = ck.CTkComboBox(self, values=["Todos", "Roupas", "Eletrônicos", "Documentos pessoais", "Acessórios e itens pessoais", "Materiais de escritório","Outros"])
        self.category_combobox.set("Categorias")
        self.category_combobox.grid(row=3, column=0, padx=(20, 0),sticky="ew")
        self.category_combobox.bind("<Key>", lambda e: "break") # Unable keyboard input

        # Neighborhood field
        self.neighborhood_label = ck.CTkLabel(self, text="Local/Bairro da perda:")
        self.neighborhood_label.grid(row=3, column=1)
        self.neighborhood_entry = ck.CTkEntry(self, placeholder_text="Ex: Centro")
        self.neighborhood_entry.grid(row=3, column=2,sticky="ew")

        # Date field
        self.date_label = ck.CTkLabel(self, text="Data da perda:")
        self.date_label.grid(row=3, column=3)
        self.date_entry = DateEntry(self, date_pattern='dd/mm/yyyy', background='gray', foreground='white')
        self.date_entry.grid(row=3, column=4,padx = (0,20),sticky="ew")
        self.date_entry.bind("<Key>", lambda e: "break") # Unable keyboard input

        # Placeholder: No results found
        self.no_results_label = ck.CTkLabel(self, text="🔍 Nenhum item encontrado", font=("Arial", 16), text_color="gray")
        self.no_results_label.grid(row=4, column=0, columnspan=5, pady=(40, 10))
        # To remove: self.no_results_label.grid_remove()
        # To show: self.no_results_label.grid()
    
    def search_button_action(self):
        category = self.category_combobox.get().strip().lower()
        if (category== "categorias"): # if no category is selected, set it to "todos"
            category = "todos"
        
        neighborhood = self.neighborhood_entry.get().strip().lower()
        date = self.date_entry.get()
        item_name = self.search_entry.get().strip().lower()
