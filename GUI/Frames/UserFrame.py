import customtkinter as ck
from GUI.GUIComponents.SharedComponents.BackButton import BackButton
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.UserFrameComponents.FoundItemsListBox import FoundItemsListBox


class UserFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_search_frame, switch_to_announce_frame, switch_to_report_frame, session):
        
        super().__init__(master)
        self.master = master
        self.session = session

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((1,5,6), weight=1)
        
        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=switch_to_search_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=1, columnspan = 2, padx=20, pady=10, sticky="ew")

        # Title label
        self.title_frame_label = ck.CTkLabel(self, text="===================================== Informações do Usuário =====================================", font=("Arial", 25))
        self.title_frame_label.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="ew")

        # User name
        self.user_name_label = ck.CTkLabel(self, text=f"Nome: {self.session.user_name}", font=("Arial", 20))
        self.user_name_label.grid(row=2, column=0, padx=(20,0), pady= 10, sticky="ew")

        # User email
        self.user_email_label = ck.CTkLabel(self, text=f"Email: {self.session.user_email}", font=("Arial", 20))
        self.user_email_label.grid(row=2, column=2, padx=(20,0), pady= 10, sticky="ew")
        
        # User cellphone
        self.user_cellphone_label = ck.CTkLabel(self, text=f"Celular: {self.session.user_cellphone}", font=("Arial", 20))
        self.user_cellphone_label.grid(row=3, column=0, padx=(20,0), pady= 10, sticky="ew")
        
        # User role
        self.user_role_label = ck.CTkLabel(self, text=f"Tipo: {self.session.user_role}", font=("Arial", 20))
        self.user_role_label.grid(row=3, column=2, padx=(20,0), pady= 10, sticky="ew")

        # Found itens
        self.found_items_label = ck.CTkLabel(self, text="Itens Encontrados:", font=("Arial", 20))
        self.found_items_label.grid(row=4, column=0, padx=(20,0), pady= 10, sticky="ew")
        self.found_items_listbox = FoundItemsListBox(self)
        self.found_items_listbox.grid(row=4, column=1, columnspan=3, padx=(0,20), pady=10, sticky="nsew")

        for item in self.session.found_items:
            self.found_items_listbox.add_item(item)

        # Go to announce frame button
        self.goto_announce_frame__button = ck.CTkButton(self, text="Anunciar Item Encontrado", command=switch_to_announce_frame)
        self.goto_announce_frame__button.grid(row=5, column=0, columnspan=2,  padx=(100,10), pady=10, sticky="ew")

        # Go to report frame button
        self.goto_report_frame_button = ck.CTkButton(self, text="Denunciar Usuário", command=switch_to_report_frame)
        self.goto_report_frame_button.grid(row=5, column=2, columnspan=2, padx=(10,100), pady=10, sticky="ew")

    def update_frame(self, session):

        self.session = session

        self.user_name_label.configure(text=f"Nome: {self.session.user_name}")
        self.user_email_label.configure(text=f"Email: {self.session.user_email}")
        self.user_cellphone_label.configure(text=f"Celular: {self.session.user_cellphone}")
        self.user_role_label.configure(text=f"Tipo: {self.session.user_role}")

        self.found_items_listbox.clear_items()

        for item in self.session.found_items:
            self.found_items_listbox.add_item(item)
       