import customtkinter as ck
from AplicationFunctionality.UserService import UserService
from tkinter import messagebox

class LoginButton(ck.CTkButton):
    def __init__(self, master, frame_ref, switch_to_search_frame, switch_to_admin_frame, **kwargs):
        super().__init__(master, text="Entrar", command=self.login_action, **kwargs)
        self.frame = frame_ref
        self.switch_to_search_frame = switch_to_search_frame
        self.switch_to_admin_frame = switch_to_admin_frame
        self.user_service = UserService()
    
    
    def login_action(self):

        email = self.frame.login_email_entry.get()
        password = self.frame.login_password_entry.get()

        if not email or not password:
            messagebox.showerror("Login inválido", "Preencha todos os campos!")
            return

        codu = self.user_service.verify_login(email, password)

        if codu is not None:
            user_infos = self.user_service.get_user_info(codu)

            if user_infos['role'] == 'moderador':
                self.switch_to_admin_frame()

            else: self.switch_to_search_frame()

        else: 
            messagebox.showerror("Login inválido", "Usuário não registrado!")
            return
