import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.AdminFrameComponents.ReportsListBox import ReportsListBox
from AplicationFunctionality.DenounceService import DenounceService
from GUI.GUIComponents.SharedComponents.BackButton import BackButton

class AdminFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_login_frame):
        super().__init__(master)
        
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=1, padx=20, pady=10)

        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=switch_to_login_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Title label
        self.title_label = ck.CTkLabel(self, text="===================================== Administração do Sistema =====================================", font=("Arial", 25))
        self.title_label.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky="ew")

        # Reports ListBox
        self.reports_label = ck.CTkLabel(self, text="Denúncias de usuários:", font=("Arial", 20))
        self.reports_label.grid(row=2, column=0, columnspan=3, padx=20, pady=10, sticky="ew")
        self.reports_box = ReportsListBox(self)
        self.reports_box.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

        denounceService = DenounceService()
        denounces = denounceService.get_denounces()
    
        # Add reports to the ReportsListBox
        for d in denounces:
            self.reports_box.add_report(d)