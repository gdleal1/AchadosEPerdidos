import customtkinter as ck
from AplicationFunctionality.BuildResponse import FoundItemProcessor
from GUIManager.InputVerification import InputVerification


class SearchButton(ck.CTkButton):
    def __init__(self, master, frame_ref, **kwargs):
        super().__init__(master, text="Buscar", command=self.search_action, **kwargs)
        self.frame = frame_ref

    def search_action(self):
        category = self.frame.category_combobox.get().strip()
        if category == "Categorias" or category == "Todos":
            category = None

        location = self.frame.location_entry.get().strip()
        date = None if self.frame.no_date_var.get() else self.frame.date_entry.get()
        item_description = self.frame.search_entry.get().strip()

        search_results = InputVerification.safe_search_and_process(item_description, category, location, date)
        processor = FoundItemProcessor(search_results)

        # Remove previous results
        self.frame.results_frame.destroy()
        self.frame.results_frame = ck.CTkScrollableFrame(self.frame)
        self.frame.results_frame.grid(row=4, column=0, columnspan=6, padx=20, pady=20, sticky="nsew")

        # Adiciona itens processados no frame
        for item in processor.get_all_items():
            self.frame.add_item_results_frame(
                item['description'],
                item['location'],
                item['date'],
                item['category']
            )
