import customtkinter as ck
from GUI.GUIComponents.SharedComponents.LogoImage import LogoImage
from GUI.GUIComponents.ReportUserComponents.ReportButton import ReportButton
from GUI.GUIComponents.ReportUserComponents.ReportedUserEmailEntry import ReportedUserEmailEntry
from GUI.GUIComponents.ReportUserComponents.ReportEntry import ReportEntry
from GUI.GUIComponents.ReportUserComponents.TitleEntry import TitleEntry
from GUI.GUIComponents.SharedComponents.BackButton import BackButton


class ReportUserFrame(ck.CTkFrame):
    def __init__(self, master, switch_to_search_frame, session):
        super().__init__(master)
        self.switch_to_search_frame = switch_to_search_frame
        
        self.grid_columnconfigure((0,1,2), weight=1)
        
        # Logo
        self.logo_label = LogoImage(self)
        self.logo_label.grid(row=0, column=1, padx=20, pady=40)

        # Back button
        self.back_button = BackButton(self, frame_ref=self, switch_to_previous_frame=self.switch_to_search_frame)
        self.back_button.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Create report label
        self.title_frame_label = ck.CTkLabel(self, text="Criar Denúncia", font=("Arial", 25))
        self.title_frame_label.grid(row=1, column=1, padx =40, pady=10, sticky="ew")

        # Reported user email entry
        self.reported_user_entry = ReportedUserEmailEntry(self)
        self.reported_user_entry.grid(row=2, column=1, padx=40, pady=10, sticky="ew")

        # Title entry
        self.title_entry = TitleEntry(self)
        self.title_entry.grid(row=3, column=1, padx=40, pady=10, sticky="ew")

        # Report entry
        self.report_entry = ReportEntry(self)
        self.report_entry.grid(row=4, column=1, padx=40, pady=10, sticky="ew")

        # Report button
        self.report_button = ReportButton(self, frame_ref=self, session=session)
        self.report_button.grid(row=5, column=1, padx=40, pady=10, sticky="ew")


        



        
    
