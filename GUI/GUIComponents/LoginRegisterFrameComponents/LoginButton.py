import customtkinter as ck
from AplicationFunctionality.UserService import UserService
from tkinter import messagebox

class LoginButton(ck.CTkButton):
    def __init__(self, master, frame_ref, switch_to_search_frame, switch_to_admin_frame, session, **kwargs):
        super().__init__(master, text="Entrar", command=self.login_action, **kwargs)
        self.frame = frame_ref
        self.switch_to_search_frame = switch_to_search_frame
        self.switch_to_admin_frame = switch_to_admin_frame
        self.session = session
        self.user_service = UserService()
    
    
    def login_action(self):

        email = self.frame.login_email_entry.get()
        password = self.frame.login_password_entry.get()

        if not email or not password:
            messagebox.showerror("Login inválido", "Preencha todos os campos!")
            return

        user_codu = self.user_service.verify_login(email, password)

        if user_codu is not None:
            self.session.initialize_session(user_codu)

            if self.session.is_moderator():
                self.switch_to_admin_frame()

            else: self.switch_to_search_frame()

        else: 
            messagebox.showerror("Login inválido", "Usuário não registrado!")
            return
