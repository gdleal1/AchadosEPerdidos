import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.AdminFrameComponents.ReportsListBox import ReportsListBox
from AplicationFunctionality.DenounceService import DenounceService
from AplicationFunctionality.ItemService import ItemService
from GUI.GUIComponents.SharedComponents.BackButton import BackButton
from GUI.GUIComponents.AdminFrameComponents.ReturnedItemsListBox import ReturnedItemsListBox

class AdminFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_login_frame):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1, 2,3), weight=1)

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, columnspan=4, padx=20, pady=10)

        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=switch_to_login_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Title label
        self.title_label = ck.CTkLabel(self, text="===================================== Administração do Sistema =====================================", font=("Arial", 25))
        self.title_label.grid(row=1,columnspan=4, padx=20, pady=20, sticky="ew")

        # Reports ListBox
        self.reports_label = ck.CTkLabel(self, text="Denúncias de usuários:", font=("Arial", 20))
        self.reports_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.reports_box = ReportsListBox(self)
        self.reports_box.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Returned items label
        self.returned_items_label = ck.CTkLabel(self, text="Itens devolvidos:", font=("Arial", 20))
        self.returned_items_label.grid(row=2, column=2, columnspan=2, padx=20, pady=10, sticky="ew")

        # Returned items ListBox
        self.retuned_items_box = ReturnedItemsListBox(self)
        self.retuned_items_box.grid(row=3, column=2, columnspan=2, padx=20, pady=10, sticky="nsew")

        # Add returned items to the ReturnedItemsListBox
        itemService = ItemService()
        returned_items = itemService.see_finalized_items()
        for item in returned_items:
            self.retuned_items_box.add_returned_item(item)

        # Add reports to the ReportsListBox
        denounceService = DenounceService()
        denounces = denounceService.get_denounces()
        for d in denounces:
            self.reports_box.add_report(d)