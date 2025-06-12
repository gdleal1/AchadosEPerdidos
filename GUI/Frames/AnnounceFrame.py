import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.SharedComponents.CategoryOptions import CategoryOptions
from GUI.GUIComponents.SharedComponents.LocationField import LocationField
from GUI.GUIComponents.SharedComponents.DateField import DateField
from GUI.GUIComponents.SharedComponents.CellphoneEntry import CellphoneEntry
from GUI.GUIComponents.AnnounceFrameComponents.FullItemDescriptionText import FullItemDescriptionText
from GUI.GUIComponents.AnnounceFrameComponents.ImageSelector import ImageSelector
from GUI.GUIComponents.AnnounceFrameComponents.AnnounceButton import AnnounceButton

class AnnounceFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7), weight=1)
        
        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, columnspan=5, padx=20, pady=40)

        # Announce label
        self.title_frame_label = ck.CTkLabel(self, text="===================================== Anunciar Item Encontrado =====================================", font=("Arial", 25))
        self.title_frame_label.grid(row=1, columnspan=5, padx =20, pady=(10,40), sticky="ew")

        # Description textbox
        self.description_label = ck.CTkLabel(self, text="Descrição detalhada do item:", font=("Arial", 18,"bold"))
        self.description_label.grid(row=2, columnspan=5, padx=20, pady=10, sticky="ew")
        self.description_text = FullItemDescriptionText(self)
        self.description_text.grid(row=3,  columnspan=5, padx=20, pady=10, sticky="ew")

        # Information label
        self.info_label = ck.CTkLabel(self, text="Informações adicionais:", font=("Arial", 18,"bold"))
        self.info_label.grid(row=4, columnspan=5, padx=20, pady=10, sticky="ew")

        # Category options
        self.category_combobox = CategoryOptions(self)
        self.category_combobox.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        # Location field
        self.location_label = ck.CTkLabel(self, text="Local/Bairro onde o item foi encontrado:")
        self.location_label.grid(row=5, column=1, padx=(20, 0),pady=10, sticky="ew")
        self.location_entry = LocationField(self)
        self.location_entry.grid(row=5, column=2, padx=(0, 20), pady=10,sticky="ew")

        # Date field
        self.date_label = ck.CTkLabel(self, text="Data em que o item foi encontrado:")
        self.date_label.grid(row=5, column=3, padx=(20, 0), pady=10, sticky="ew")
        self.date_entry = DateField(self)
        self.date_entry.grid(row=5, column=4, padx=(0, 20), pady=10, sticky="ew")

        # Cellphone entry
        self.cellphone_label = ck.CTkLabel(self, text="Telefone para contato:")
        self.cellphone_label.grid(row=6, column=0, padx=(20,0), pady=20, sticky="ew")
        self.cellphone_entry = CellphoneEntry(self)
        self.cellphone_entry.grid(row=6, column=1, padx=(0, 20), pady=20, sticky="ew")

        # Image entry
        self.image_label = ck.CTkLabel(self, text="Imagem do item encontrado (opcional):")
        self.image_label.grid(row=6, column=2, padx=(20,0), pady=20, sticky="ew")
        self.image_selector = ImageSelector(self)
        self.image_selector.grid(row=6, column=3, padx=(0, 20), pady=20, sticky="ew")

        # Announce button
        self.announce_button = AnnounceButton(self, frame_ref=self)
        self.announce_button.grid(row=7, column = 1, columnspan=3, padx=20, pady= 40, sticky="ew")



        





