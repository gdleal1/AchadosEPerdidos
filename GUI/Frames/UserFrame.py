import customtkinter as ck
from GUI.GUIComponents.SharedComponents.BackButton import BackButton
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.UserFrameComponents.FoundItemsListBox import FoundItemsListBox


class UserFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_search_frame, switch_to_announce_frame, switch_to_report_frame):
        
        super().__init__(master)
        self.master = master

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
        self.user_name_label = ck.CTkLabel(self, text="Nome:", font=("Arial", 20))
        self.user_name_label.grid(row=2, column=0, padx=(20,0), pady= 10, sticky="ew")
        # TODO: Buscar nome do usuário no banco de dados

        # User email
        self.user_email_label = ck.CTkLabel(self, text="Email:", font=("Arial", 20))
        self.user_email_label.grid(row=2, column=2, padx=(20,0), pady= 10, sticky="ew")
        # TODO: Buscar email do usuário no banco de dados
        
        # User cellphone
        self.user_cellphone_label = ck.CTkLabel(self, text="Celular:", font=("Arial", 20))
        self.user_cellphone_label.grid(row=3, column=0, padx=(20,0), pady= 10, sticky="ew")
        # TODO: Buscar celular do usuário no banco de dados
        
        # User role
        self.user_role_label = ck.CTkLabel(self, text="Tipo:", font=("Arial", 20))
        self.user_role_label.grid(row=3, column=2, padx=(20,0), pady= 10, sticky="ew")
        # TODO: Buscar tipo do usuário no banco de dados

        # Found itens
        self.found_items_label = ck.CTkLabel(self, text="Itens Encontrados:", font=("Arial", 20))
        self.found_items_label.grid(row=4, column=0, padx=(20,0), pady= 10, sticky="ew")
        self.found_items_listbox = FoundItemsListBox(self)
        self.found_items_listbox.grid(row=4, column=1, columnspan=3, padx=(0,20), pady=10, sticky="nsew")

        # TODO: Buscar itens encontrados do usuário no banco de dados e adicionar na listbox
        # Exemplo:
        for items in ["Carteira preta", "Chave azul", "Celular branco"]:
            self.found_items_listbox.add_item(items)

        # Go to announce frame button
        self.goto_announce_frame__button = ck.CTkButton(self, text="Anunciar Item Encontrado", command=switch_to_announce_frame)
        self.goto_announce_frame__button.grid(row=5, column=0, columnspan=2,  padx=(100,10), pady=10, sticky="ew")

        # Go to report frame button
        self.goto_report_frame_button = ck.CTkButton(self, text="Denunciar Usuário", command=switch_to_report_frame)
        self.goto_report_frame_button.grid(row=5, column=2, columnspan=2, padx=(10,100), pady=10, sticky="ew")




       