import customtkinter as ck
from GUI.GUIComponents.AdminFrameComponents.BanButton import BanButton

class ReportsListBox(ck.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.reports = []

    def add_report(self, report):
        # Add a report to the frame. Expects a dictionary with title, description, reporter, and reported.
        button = ck.CTkButton(
            self,
            text=f"Título da denúncia: {report['titulo']}",
            font=("Arial", 16),
            fg_color="transparent",

            command=lambda r=report: self._show_report_details(r)
        )
        button.pack(padx=10, pady=5)
        self.reports.append(report)

    def clear_reports(self):
        # Remove all reports from the listbox.
        for widget in self.winfo_children():
            widget.destroy()
        self.reports.clear()

    def _show_report_details(self, report):
        # Create a new window to show the details of the report.
        window = ck.CTkToplevel(self)
        window.title("Detalhes da Denúncia")
        window.geometry("400x300")

        ck.CTkLabel(window, text=f"Título: {report['titulo']}", font=("Arial", 16, "bold")).pack(pady=10)
        ck.CTkLabel(window, text=f"Descrição: {report['descricao']}", wraplength=380, justify="left").pack(pady=5)
        ck.CTkLabel(window, text=f"Denunciante: {report['denunciante']}").pack(pady=5)
        ck.CTkLabel(window, text=f"Denunciado: {report['denunciado']}").pack(pady=5)

        # Ban button
        ban_button = BanButton(window,report['denunciado'])
        ban_button.pack(pady=20)