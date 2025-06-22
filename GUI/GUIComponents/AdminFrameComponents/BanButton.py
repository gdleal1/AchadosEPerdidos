import customtkinter as ck
from tkinter import messagebox
from AplicationFunctionality.UserService import UserService

class BanButton(ck.CTkButton):
    def __init__(self, master, reported_codu, reported_name,**kwargs):
        super().__init__(master, text="Banir Usuário", command= self._ban_user, **kwargs)
        self.reported_codu = reported_codu
        self.reported_name = reported_name
        self.window_to_close = master
        
        
    def _ban_user(self):
        user_service = UserService()
        user_banned = user_service.ban_user(self.reported_codu)
        if not user_banned:
            messagebox.showerror("Erro", f"Não foi possível banir o usuário '{self.reported_name}'.")
            return
        else:
            messagebox.showinfo("Banimento", f"Usuário '{self.reported_name}' foi banido com sucesso.")
        
        self.window_to_close.destroy()
        
        