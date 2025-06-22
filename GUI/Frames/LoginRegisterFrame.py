import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.LoginRegisterFrameComponents.EmailEntry import EmailEntry
from GUI.GUIComponents.LoginRegisterFrameComponents.PasswordEntry import PasswordEntry
from GUI.GUIComponents.LoginRegisterFrameComponents.LoginButton import LoginButton
from GUI.GUIComponents.LoginRegisterFrameComponents.NameEntry import NameEntry
from GUI.GUIComponents.SharedComponents.CellphoneEntry import CellphoneEntry
from GUI.GUIComponents.LoginRegisterFrameComponents.RegisterButton import RegisterButton


class LoginRegisterFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_search_frame, switch_to_admin_frame):
        super().__init__(master)
        self.switch_to_search_frame = switch_to_search_frame
        self.switch_to_admin_frame = switch_to_admin_frame
        
        self.grid_columnconfigure((0,1), weight=1)
        
        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, columnspan=2, padx=20, pady=40)

        # Login label
        self.title_frame_label = ck.CTkLabel(self, text="LOGIN", font=("Arial", 25))
        self.title_frame_label.grid(row=1, column=0, padx =40, pady=10, sticky="ew")

        # Login E-mail entry
        self.login_email_entry = EmailEntry(self)
        self.login_email_entry.grid(row=2, column=0, padx=40, pady=10, sticky="ew")

        # Password entry
        self.login_password_entry = PasswordEntry(self)
        self.login_password_entry.grid(row=3, column=0, padx=40, pady=10, sticky="ew")

        # Login button
        self.login_button = LoginButton(self, frame_ref=self, switch_to_search_frame=self.switch_to_search_frame, switch_to_admin_frame=self.switch_to_admin_frame)
        self.login_button.grid(row=4, column=0, padx=40, pady=10, sticky="ew")

        # Register label
        self.register_label = ck.CTkLabel(self, text="REGISTRAR-SE", font=("Arial", 25))
        self.register_label.grid(row=1, column=1, padx=40, pady=10, sticky="ew")

        # Name entry
        self.register_name_entry = NameEntry(self)
        self.register_name_entry.grid(row=2, column=1, padx=40, pady=10, sticky="ew")

        # Register E-mail entry
        self.register_email_entry = EmailEntry(self)
        self.register_email_entry.grid(row=3, column=1, padx=40, pady=10, sticky="ew")

        # Cellphone entry
        self.register_cellphone_entry = CellphoneEntry(self)
        self.register_cellphone_entry.grid(row=4, column=1, padx=40, pady=10, sticky="ew")

        # Register Password entry
        self.register_password_entry = PasswordEntry(self)
        self.register_password_entry.grid(row=5, column=1, padx=40, pady=10, sticky="ew")

        # Register button
        self.register_button = RegisterButton(self, frame_ref=self)
        self.register_button.grid(row=6, column=1, padx=40, pady=10, sticky="ew")


        



        
    
