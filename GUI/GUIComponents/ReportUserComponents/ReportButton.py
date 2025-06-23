import customtkinter as ck
from AplicationFunctionality.DenounceService import DenounceService
from tkinter import messagebox

class ReportButton(ck.CTkButton):
    def __init__(self, master, frame_ref, session, **kwargs):
        super().__init__(master, text="Denunciar", command=self.report_action, **kwargs)
        self.frame = frame_ref
        self.session = session
        
    def report_action(self):
        denounce_service = DenounceService()
        title = self.frame.title_entry.get()
        description = self.frame.report_entry.get()
        reported_user_email = self.frame.reported_user_email_entry.get()
        user_codu = self.session.user_codu

        denouncedAdded = denounce_service.add_denounce(
            title=title,
            description=description,
            denouncer=user_codu,
            denounced=reported_user_email
        )
        if denouncedAdded:
            messagebox.showinfo("Denúncia Enviada", "Sua denúncia foi enviada com sucesso!")
            self.frame.master.recreate_admin_frame()
            
        else:
            messagebox.showerror("Erro", "Não foi possível enviar a denúncia. Verifique os dados e tente novamente.")

        


        

    