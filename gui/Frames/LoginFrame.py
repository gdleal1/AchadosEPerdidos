import customtkinter as ck
from gui.GUIComponents.SharedComponents.LogoImage import LogoImage
from gui.GUIComponents.LoginFrameComponents.UsernameEntry import UsernameEntry
from gui.GUIComponents.LoginFrameComponents.PasswordEntry import PasswordEntry


class LoginFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure((0,1,2), weight=1)
        #self.grid_rowconfigure((0,1,2,3,4), weight=1)

        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, columnspan=3, padx=20, pady=40)

        # Frame title
        self.title_frame_label = ck.CTkLabel(self, text="===================================================== Login =====================================================", font=("Arial", 20))
        self.title_frame_label.grid(row=1, columnspan=3, pady=10)

        # Username entry
        self.username_entry = UsernameEntry(self)
        self.username_entry.grid(row=2, columnspan=3, padx=20, pady=10)

        # Password entry
        self.password_entry = PasswordEntry(self)
        self.password_entry.grid(row=3, columnspan=3, padx=20, pady=10)
        
    
