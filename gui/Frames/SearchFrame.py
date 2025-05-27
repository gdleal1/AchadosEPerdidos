import customtkinter as ck
from gui.GUIComponents.SearchFrameComponents.SearchButton import SearchButton
from gui.GUIComponents.SharedComponents.LogoImage import LogoImage
from gui.GUIComponents.SearchFrameComponents.SearchBar import SearchBar
from gui.GUIComponents.SearchFrameComponents.CategoryOptions import CategoryOptions
from gui.GUIComponents.SearchFrameComponents.LocationField import LocationField
from gui.GUIComponents.SearchFrameComponents.DateField import DateField

class SearchFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=0, columnspan=6, padx=20, pady=10)

        # Frame title
        self.title_frame_label = ck.CTkLabel(self, text="===================================================== Buscar Itens Perdidos =====================================================", font=("Arial", 20))
        self.title_frame_label.grid(row=1, column=0, columnspan=6,pady=(20, 10))

        # Search bar
        self.search_entry = SearchBar(self)
        self.search_entry.grid(row=2, column=0, columnspan=5, padx=20, pady=20, sticky="ew")

        # Search button
        self.search_button = SearchButton(self, frame_ref=self)
        self.search_button.grid(row=2, column=5, padx=20, pady=20, sticky="ew")

        # Cartegory options
        self.category_combobox = CategoryOptions(self)
        self.category_combobox.grid(row=3, column=0, padx=(20, 0), sticky="ew")
        

        # Location field
        self.location_label = ck.CTkLabel(self, text="Local/Bairro da perda:")
        self.location_label.grid(row=3, column=1)
        self.location_entry = LocationField(self)
        self.location_entry.grid(row=3, column=2,sticky="ew")

        # Date field
        self.date_label = ck.CTkLabel(self, text="Data da perda:")
        self.date_label.grid(row=3, column=3)
        self.date_entry = DateField(self)
        self.date_entry.grid(row=3, column=4,padx = (0,20),sticky="ew")

        # CheckBox "Sem data"
        self.no_date_var = ck.BooleanVar()
        self.no_date_checkbox = ck.CTkCheckBox(
            self,
            text="Sem data",
            variable=self.no_date_var,
            command=self.toggle_date_entry
        )
        self.no_date_checkbox.grid(row=3, column=5, padx=(0, 20))


        # Frame to display search results
        self.results_frame = ck.CTkScrollableFrame(self)
        self.results_frame.grid(row=4, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")
    
        
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

