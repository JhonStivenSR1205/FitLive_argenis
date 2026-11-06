# app_cliente.py
# Punto de entrada principal
import tkinter as tk
from interfaz_visual import FitLiveProApp

if __name__ == "__main__":
    root = tk.Tk()
    app = FitLiveProApp(root)
    root.mainloop()