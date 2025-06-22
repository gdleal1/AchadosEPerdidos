import customtkinter as ck
from AplicationFunctionality.DenounceService import DenounceService

class ReportButton(ck.CTkButton):
    def __init__(self, master, frame_ref, session, **kwargs):
        super().__init__(master, text="Denunciar", command=self.report_action, **kwargs)
        self.frame = frame_ref
        
    
    def report_action(self):
        denounce_service = DenounceService()
        title = self.frame.title_entry.get()
        description = self.frame.report_entry.get()
        reported_user_email = self.frame.reported_user_email_entry.get()

        


        

    