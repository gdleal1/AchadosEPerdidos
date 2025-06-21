import customtkinter as ck
from tkinter import messagebox

class BanButton(ck.CTkButton):
    def __init__(self, master, reported_name,**kwargs):
        super().__init__(master, text="Banir Usuário", command= self._ban_user, **kwargs)
        self.reported_name = reported_name
        self.window_to_close = master
        
        
    def _ban_user(self):
        # TODO: Implementar a lógica de banimento do usuário
        messagebox.showinfo("Banimento", f"Usuário '{self.reported_name}' foi banido com sucesso.")
        self.window_to_close.destroy()
        
        