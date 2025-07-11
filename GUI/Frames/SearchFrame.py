import customtkinter as ck
from GUI.GUIComponents.SearchFrameComponents.SearchButton import SearchButton
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.SearchFrameComponents.SearchBar import SearchBar
from GUI.GUIComponents.SharedComponents.CategoryOptions import CategoryOptions
from GUI.GUIComponents.SharedComponents.LocationField import LocationField
from GUI.GUIComponents.SharedComponents.DateField import DateField
from GUI.GUIComponents.SharedComponents.BackButton import BackButton
from GUI.Frames.ItemFrame import ItemFrame

class SearchFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_login_frame, switch_to_user_frame):
        super().__init__(master)
        self.master = master

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=1, columnspan=4, padx=20, pady=10, sticky="ew")

        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=switch_to_login_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Change to user frame button
        self.change_to_user_frame_button = ck.CTkButton(self,  text="Ir para perfil", command=switch_to_user_frame)
        self.change_to_user_frame_button.grid(row=0, column=5, padx=20, pady=10, sticky="e")
            
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
    def add_item_results_frame(self, description, location, date, category, status, contact_phone, complete_description, email):
        item_data = {
            'description': description,
            'location': location,
            'date': date,
            'category': category,
            'status': status,
            'contact_phone': contact_phone,
            'completeDescription': complete_description,
            'email': email
        }
        
        # Create and add the item frame to results
        ItemFrame(
            master=self.results_frame,
            item_data=item_data,
            click_callback=self.master.search_to_item_frame
        )
    
    # Function to toggle the state of the date entry field when the checkbox is checked/unchecked
    def toggle_date_entry(self):
        if self.no_date_var.get():
            self.date_entry.delete(0, 'end')
            self.date_entry.config(state='disabled')
        else:
            self.date_entry.config(state='normal')
    