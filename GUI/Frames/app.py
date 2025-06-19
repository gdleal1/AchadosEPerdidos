import customtkinter
from GUI.Frames.SearchFrame import SearchFrame
from GUI.Frames.LoginRegisterFrame import LoginRegisterFrame
from GUI.Frames.AnnounceFrame import AnnounceFrame
from GUI.Frames.ItemFrame import ItemFrame


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

        # Creating frames
        self.search_frame = SearchFrame(self, self.search_to_login_frame)
        self.login_frame = LoginRegisterFrame(self,self.login_to_search_frame)
        self.announce_frame = AnnounceFrame(self, self.announce_to_search_frame)
        self.item_frame = ItemFrame(self)


        #self.announce_frame.pack(fill="both", expand=True)
        self.login_frame.pack(fill="both", expand=True)

    # Function to switch from login frame to search frame
    def login_to_search_frame(self):
        self.login_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)
    
    # Function to switch from search frame to login frame
    def search_to_login_frame(self):
        self.search_frame.pack_forget()
        self.login_frame.pack(fill="both", expand=True)

    # Function to switch from Announce frame to Search frame
    def announce_to_search_frame(self):
        self.announce_frame.pack_forget()
        self.search_frame.pack(fill="both", expand=True)