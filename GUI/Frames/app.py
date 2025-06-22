# App.py
import customtkinter
from GUI.Frames.SearchFrame import SearchFrame
from GUI.Frames.LoginRegisterFrame import LoginRegisterFrame
from GUI.Frames.AnnounceFrame import AnnounceFrame
from GUI.Frames.ExpandedItemFrame import ExpandedItemFrame
from GUI.Frames.UserFrame import UserFrame
from GUI.Frames.ReportUserFrame import ReportUserFrame
from GUI.Frames.AdminFrame import AdminFrame
from GUI.GUIManager.Session import Session

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Resolution
        full_screen_width = self.winfo_screenwidth()
        full_screen_height = self.winfo_screenheight()

        screen_width = int(full_screen_width * 0.8)   
        screen_height = int(full_screen_height * 0.7) 

        x_offset = (full_screen_width - screen_width) // 2
        y_offset = (full_screen_height - screen_height) // 2

        self.geometry(f"{screen_width}x{screen_height}+{x_offset}+{y_offset}")
        self.title("Sistema de Achados e Perdidos")

        # Style
        self._set_appearance_mode("dark") 

        # Session
        self.session = Session()

        # Creating frames
        self.search_frame = SearchFrame(self, self.search_to_login_frame, self.search_to_user_frame)
        self.login_frame = LoginRegisterFrame(self, self.login_to_search_frame, self.login_to_admin_frame, self.session)
        self.announce_frame = AnnounceFrame(self, self.announce_to_search_frame)
        self.expanded_item_frame = ExpandedItemFrame(self, self.item_to_search_frame)
        self.user_frame = UserFrame(self, self.user_to_search_frame, self.user_to_announce_frame, self.user_to_report_frame, self.session)
        self.report_frame = ReportUserFrame(self, self.report_to_search_frame)
        self.admin_frame = AdminFrame(self)
        
        
        self.login_frame.pack(fill="both", expand=True)
        

    # Function to switch from login frame to search frame
    def login_to_search_frame(self):
        self.login_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)

    # Function to switch from login frame to admin frame
    def login_to_admin_frame(self):
        self.login_frame.pack_forget()
        self.admin_frame.pack(fill="both", expand=True)
    
    # Function to switch from search frame to login frame
    def search_to_login_frame(self):
        self.search_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    # Function to switch from Announce frame to Search frame
    def announce_to_search_frame(self):
        self.announce_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)

    # Function to switch from search frame to item frame
    def search_to_item_frame(self, item_data):
        self.search_frame.pack_forget()
        self.expanded_item_frame.pack(fill="both", expand=True)
        self.expanded_item_frame.display_item(item_data)
    
    # Function to switch from item frame to search frame
    def item_to_search_frame(self):
        self.expanded_item_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)
    
    # Function to switch from user frame to search frame
    def user_to_search_frame(self):
        self.user_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)
    
    # Function to switch from user frame to announce frame
    def user_to_announce_frame(self):
        self.user_frame.pack_forget()
        self.announce_frame.pack(fill="both", expand=True)
    
    # Function to switch from Search frame to user frame
    def search_to_user_frame(self):
        self.search_frame.pack_forget()
        self.user_frame.pack(fill="both", expand=True)
        self.user_frame.update_frame(self.session)
    
    # Function to switch from report frame to search frame
    def report_to_search_frame(self):
        self.report_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)
    
    # Function to switch from user frame to report frame
    def user_to_report_frame(self):
        self.user_frame.pack_forget()
        self.report_frame.pack(fill="both", expand=True)
    
    