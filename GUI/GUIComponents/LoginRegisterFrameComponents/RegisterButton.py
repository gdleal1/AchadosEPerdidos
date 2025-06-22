import customtkinter as ck
from AplicationFunctionality.UserService import UserService
from tkinter import messagebox

class RegisterButton(ck.CTkButton):
    def __init__(self, master, frame_ref, **kwargs):
        super().__init__(master, text="Registrar-se", command=self.register_action, **kwargs)
        self.frame = frame_ref
    
    
    def register_action(self):
        
        username = self.frame.register_name_entry.get()
        email = self.frame.register_email_entry.get()
        password = self.frame.register_password_entry.get()
        cellphone = self.frame.register_cellphone_entry.get()

        if not all([username.strip(), email.strip(), password.strip(), cellphone.strip()]):
            messagebox.showerror("Registro inválido", "Todos os campos são obrigatórios!")
            return

        user_service = UserService()

        if user_service.insert_new_user(username, email, cellphone, password):
            messagebox.showinfo("Registro completo", "Usuário foi registrado com sucesso!")

            self.frame.register_name_entry.delete(0, 'end')
            self.frame.register_email_entry.delete(0, 'end')
            self.frame.register_password_entry.delete(0, 'end')
            self.frame.register_cellphone_entry.delete(0, 'end')
            
            return

        else: 
            messagebox.showerror("Registro inválido", "Informações inválidas!")
            return
        