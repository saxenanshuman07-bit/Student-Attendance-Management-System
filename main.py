"""
main.py — Application Entry Point
"""

import tkinter as tk
import customtkinter as ctk
from database.db_manager import initialize_database
from gui.login import LoginPage
from gui.app import AttendanceApp
from gui.styles import SIZES

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainApplication:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Attendance Management System — VIT Pune")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#0A0A15")

        w, h = SIZES['window_width'], SIZES['window_height']
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self._show_login()

    def _show_login(self):
        for w in self.root.winfo_children(): w.destroy()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        try:
            self.root.grid_columnconfigure(1, weight=0)
        except Exception:
            pass
        LoginPage(self.root, self._on_login).pack(fill="both", expand=True)

    def _on_login(self, role, user_info):
        self.current_app = AttendanceApp(self.root, role, user_info, self._show_login)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    initialize_database()
    print("[OK] Application running!")
    MainApplication().run()
