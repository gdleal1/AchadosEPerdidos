import customtkinter as ck
from tkcalendar import DateEntry
from PIL import Image
from DataAcess.Request import ItemSearch
from DataAcess.Response import FoundItemProcessor

class SearchFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Logo
        self.logoimage = ck.CTkImage(Image.open("gui/images/logo.png"),
                                  size=(480, 134))
        self.logo_label = ck.CTkLabel(self, text="", image=self.logoimage)
        self.logo_label.grid(row=0, column=0,columnspan=6, padx= 20, pady=10)

        # Frame title
        self.title_frame_label = ck.CTkLabel(self, text="===================================================== Buscar Itens Perdidos =====================================================", font=("Arial", 20))
        self.title_frame_label.grid(row=1, column=0, columnspan=6,pady=(20, 10))

        # Search bar
        self.search_entry = ck.CTkEntry(self, placeholder_text="Digite a descrição do item ...")
        self.search_entry.grid(row=2, column=0,columnspan=5,padx=20,pady=20,sticky="ew")

        # Search button
        self.search_button = ck.CTkButton(self, text="Buscar", command=self.search_button_action)
        self.search_button.grid(row=2, column=5, padx=20, pady=20, sticky="ew")

        # Cartegory options
        self.category_combobox = ck.CTkComboBox(self, values=["Todos", "Roupas", "Eletrônicos", "Documentos pessoais", "Acessórios e itens pessoais", "Materiais de escritório","Outros"])
        self.category_combobox.set("Categorias")
        self.category_combobox.grid(row=3, column=0, padx=(20, 0),sticky="ew")
        self.category_combobox.bind("<Key>", lambda e: "break") # Unable keyboard input

        # Location field
        self.location_label = ck.CTkLabel(self, text="Local/Bairro da perda:")
        self.location_label.grid(row=3, column=1)
        self.location_entry = ck.CTkEntry(self, placeholder_text="Ex: Centro")
        self.location_entry.grid(row=3, column=2,sticky="ew")

        # Date field
        self.date_label = ck.CTkLabel(self, text="Data da perda:")
        self.date_label.grid(row=3, column=3)
        self.date_entry = DateEntry(self, date_pattern='dd/mm/yyyy', background='gray', foreground='white')
        self.date_entry.grid(row=3, column=4,padx = (0,20),sticky="ew")
        self.date_entry.bind("<Key>", lambda e: "break") # Unable keyboard input

        # CheckBox "Sem data"
        self.no_date_var = ck.BooleanVar()
        self.no_date_checkbox = ck.CTkCheckBox(
            self,
            text="Sem data",
            variable=self.no_date_var,
            command=self.toggle_date_entry
        )
        self.no_date_checkbox.grid(row=3, column=5, padx=(0, 20))

        # Placeholder: No results found
        #self.no_results_label = ck.CTkLabel(self, text="🔍 Nenhum item encontrado", font=("Arial", 16), text_color="gray")
        #self.no_results_label.grid(row=4, column=0, columnspan=5, pady=(40, 10))

        # Frame to display search results
        self.results_frame = ck.CTkScrollableFrame(self)
        self.results_frame.grid(row=4, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")
    
    def search_button_action(self):

        # Handle empty/general inputs
        category = self.category_combobox.get().strip()
        if (category== "Categorias" or category== "Todos"): 
            category = None
        
        location = self.location_entry.get().strip()
        if (location == ""): 
            location = None
        
        date = self.date_entry.get()
        if(date == ""): 
            date = None

        item_description = self.search_entry.get().strip()
        if (item_description == ""):
            item_description = None

        # Database search
        searcher = ItemSearch("DB/AchadosEPerdidos.db")
        search_results = searcher.search_item(item_description, category, location, date) 
        processor = FoundItemProcessor(search_results)

        # Remove previous results
        self.results_frame.destroy()
        self.results_frame = ck.CTkScrollableFrame(self)
        self.results_frame.grid(row=4, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")

        # Add items to the results frame
        for item in processor.get_all_items():
            self.add_item_results_frame(item['description'], item['location'], item['date'], item['category'])
        
    # Function to add searched items to the results frame
    def add_item_results_frame(self, description, location, date, category):
        item_frame = ck.CTkFrame(self.results_frame, corner_radius=10)
        item_frame.pack(fill="x", padx=10, pady=10)

        item_name_label = ck.CTkLabel(item_frame, text=f"📦 {description.title()}", font=("Arial", 14, "bold"))
        item_name_label.pack(anchor="w", padx=10, pady=(5, 0))

        info_label = ck.CTkLabel(
            item_frame,
            text=f"Local: {location.title()}  |  Data: {date} |  Categoria: {category}",
            font=("Arial", 12)
        )
        info_label.pack(anchor="w", padx=10, pady=(0, 5))
    
    # Function to toggle the state of the date entry field when the checkbox is checked/unchecked
    def toggle_date_entry(self):
        if self.no_date_var.get():
            self.date_entry.delete(0, 'end')
            self.date_entry.config(state='disabled')
        else:
            self.date_entry.config(state='normal')

