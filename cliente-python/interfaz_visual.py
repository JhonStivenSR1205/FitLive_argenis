# interfaz_visual.py
# Capa de Presentación (Frontend Tkinter Moderno)
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
import requests
import config
import servicios_api

class FitLiveProApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FitLive Pro - Arquitectura Modular V2")
        self.root.geometry("950x700")
        
        # Paleta de colores modernos (Dark Mode)
        self.bg_color = "#1e272e"
        self.fg_color = "#d2dae2"
        self.accent_color = "#0fbcf9"
        self.success_color = "#0be881"
        self.link_color = "#0abde3"
        
        self.root.configure(bg=self.bg_color)
        
        style = ttk.Style()
        style.theme_use("clam")
        
        # Configurar estilos
        style.configure("TNotebook", background=self.bg_color, borderwidth=0)
        style.configure("TNotebook.Tab", font=("Segoe UI", 12, "bold"), padding=[20, 10], background="#485460", foreground="white", borderwidth=0)
        style.map("TNotebook.Tab", background=[("selected", self.accent_color)], foreground=[("selected", "white")])
        
        style.configure("TFrame", background=self.bg_color)
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color, font=("Segoe UI", 11))
        style.configure("Header.TLabel", font=("Segoe UI", 20, "bold"), foreground=self.accent_color)
        style.configure("SubHeader.TLabel", font=("Segoe UI", 20, "bold"), foreground=self.success_color)
        
        # Estilo para botones de acción principales
        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=10, background=self.accent_color, foreground="white", borderwidth=0)
        style.map("TButton", background=[("active", "#0984e3")])
        
        style.configure("Reg.TButton", font=("Segoe UI", 11, "bold"), padding=10, background=self.success_color, foreground="#1e272e", borderwidth=0)
        style.map("Reg.TButton", background=[("active", "#05c46b")])
        
        # Estilo para botón tipo "Enlace" (Link)
        style.configure("Link.TButton", font=("Segoe UI", 10, "underline"), padding=5, background=self.bg_color, foreground=self.link_color, borderwidth=0)
        style.map("Link.TButton", background=[("active", self.bg_color)], foreground=[("active", "white")])

        style.configure("Treeview", font=("Segoe UI", 10), rowheight=30, background="#2c3e50", fieldbackground="#2c3e50", foreground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"), background="#485460", foreground="white")

        # Banner Superior
        header = tk.Frame(root, bg=self.accent_color, height=80)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)
        tk.Label(header, text=" FITLIVE PRO", font=("Segoe UI", 22, "bold"), bg=self.accent_color, fg="white").pack(pady=20)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=20, pady=20)

        self.tab_auth = ttk.Frame(self.notebook)
        self.tab_ent = ttk.Frame(self.notebook)
        self.tab_ia = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_auth, text=" 🔒 Acceso Seguro ")

        # Inicializar vistas de autenticación
        self.frame_login_view = None
        self.frame_reg_view = None
        
        self.construir_auth()
        self.construir_ent()
        self.construir_ia()

    def construir_auth(self):
        # Contenedor principal centrado
        self.container_auth = ttk.Frame(self.tab_auth)
        self.container_auth.place(relx=0.5, rely=0.4, anchor="center")

        # ================= VISTA: LOGIN =================
        self.frame_login_view = ttk.Frame(self.container_auth)
        
        ttk.Label(self.frame_login_view, text="Inicie Sesión", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=15)
        
        ttk.Label(self.frame_login_view, text="Usuario:").grid(row=1, column=0, pady=10, sticky="e")
        self.ent_user = ttk.Entry(self.frame_login_view, width=25, font=("Segoe UI", 11))
        self.ent_user.grid(row=1, column=1, pady=10, padx=5)
        
        ttk.Label(self.frame_login_view, text="Clave:").grid(row=2, column=0, pady=10, sticky="e")
        self.ent_pass = ttk.Entry(self.frame_login_view, show="*", width=25, font=("Segoe UI", 11))
        self.ent_pass.grid(row=2, column=1, pady=10, padx=5)
        
        ttk.Button(self.frame_login_view, text="Conectar a Django", command=self.login).grid(row=3, columnspan=2, pady=20, ipadx=10)
        
        # Botón sutil tipo enlace para ir a registro
        ttk.Button(self.frame_login_view, text="¿No tienes cuenta? Regístrate aquí", style="Link.TButton", command=self.mostrar_registro).grid(row=4, columnspan=2, pady=5)

        # ================= VISTA: REGISTRO =================
        self.frame_reg_view = ttk.Frame(self.container_auth)

        ttk.Label(self.frame_reg_view, text="Crear Cuenta Nueva", style="SubHeader.TLabel").grid(row=0, column=0, columnspan=2, pady=15)

        ttk.Label(self.frame_reg_view, text="Usuario:").grid(row=1, column=0, pady=8, sticky="e")
        self.reg_user = ttk.Entry(self.frame_reg_view, width=25, font=("Segoe UI", 11))
        self.reg_user.grid(row=1, column=1, pady=8, padx=5)

        ttk.Label(self.frame_reg_view, text="Correo:").grid(row=2, column=0, pady=8, sticky="e")
        self.reg_email = ttk.Entry(self.frame_reg_view, width=25, font=("Segoe UI", 11))
        self.reg_email.grid(row=2, column=1, pady=8, padx=5)

        ttk.Label(self.frame_reg_view, text="Contraseña:").grid(row=3, column=0, pady=8, sticky="e")
        self.reg_pass = ttk.Entry(self.frame_reg_view, show="*", width=25, font=("Segoe UI", 11))
        self.reg_pass.grid(row=3, column=1, pady=8, padx=5)

        ttk.Button(self.frame_reg_view, text="Registrarse", style="Reg.TButton", command=self.registrar).grid(row=4, columnspan=2, pady=20, ipadx=10)
        
        # Botón sutil tipo enlace para volver a login
        ttk.Button(self.frame_reg_view, text="¿Ya tienes cuenta? Inicia sesión", style="Link.TButton", command=self.mostrar_login).grid(row=5, columnspan=2, pady=5)

        # Mostrar por defecto la vista de login
        self.frame_login_view.grid(row=0, column=0)

    # Lógicas de cambio de vista
    def mostrar_registro(self):
        self.frame_login_view.grid_forget()
        self.frame_reg_view.grid(row=0, column=0)

    def mostrar_login(self):
        self.frame_reg_view.grid_forget()
        self.frame_login_view.grid(row=0, column=0)

    def registrar(self):
        usuario = self.reg_user.get().strip()
        correo = self.reg_email.get().strip()
        clave = self.reg_pass.get().strip()

        if not usuario or not correo or not clave:
            messagebox.showwarning("Atención", "Todos los campos de registro son obligatorios.")
            return

        try:
            resp = servicios_api.registrar_usuario_django(usuario, clave, correo)
            if resp.status_code == 201:
                messagebox.showinfo("Éxito", "Usuario creado correctamente. Ya puedes iniciar sesión.")
                self.reg_user.delete(0, 'end')
                self.reg_email.delete(0, 'end')
                self.reg_pass.delete(0, 'end')
                self.mostrar_login() # Vuelve automáticamente a la pantalla de login
            else:
                messagebox.showerror("Error de Registro", f"El servidor respondió:\n{resp.text}")
        except requests.exceptions.ConnectionError:
            messagebox.showwarning("Error de Conexión", "No se detecta el servidor Django en 127.0.0.1:8000 para registrar usuarios.")

    def login(self):
        try:
            resp = servicios_api.login_django(self.ent_user.get(), self.ent_pass.get())
            if resp.status_code == 200:
                config.TOKEN_JWT = resp.json().get("access")
                messagebox.showinfo("OK", "Conexión exitosa a Django.")
                
                self.notebook.add(self.tab_ent, text=" 🏋️ Entrenamiento ")
                self.notebook.add(self.tab_ia, text=" 🧠 IA Asistente ")
                
                self.notebook.hide(self.tab_auth)
                self.notebook.select(self.tab_ent)
                self.cargar_rutinas()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas.")
        except requests.exceptions.ConnectionError:
            messagebox.showwarning("Modo Simulación", "Servidor Django no detectado.\nActivando solo el módulo IA.")
            self.notebook.add(self.tab_ia, text=" 🧠 IA Asistente ")
            self.notebook.hide(self.tab_auth)
            self.notebook.select(self.tab_ia)

    def construir_ent(self):
        btn_frame = ttk.Frame(self.tab_ent)
        btn_frame.pack(fill="x", pady=10)
        ttk.Button(btn_frame, text="🔄 Cargar Rutinas", command=self.cargar_rutinas).pack(side="left", padx=10)
        self.tabla = ttk.Treeview(self.tab_ent, columns=("ID", "Nombre", "Fecha", "Estado"), show="headings")
        for col in self.tabla["columns"]: self.tabla.heading(col, text=col)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=10)

    def cargar_rutinas(self):
        if not config.TOKEN_JWT: return
        try:
            resp = servicios_api.listar_rutinas()
            if resp.status_code == 200:
                for item in self.tabla.get_children(): self.tabla.delete(item)
                for r in resp.json():
                    estado = "Completada" if r.get("completada") else "Pendiente"
                    self.tabla.insert("", "end", values=(r.get("id_rutina"), r.get("nombre_rutina"), r.get("fecha_programada"), estado))
        except: messagebox.showerror("Error", "Fallo de conexión.")

    def construir_ia(self):
        frame = ttk.Frame(self.tab_ia)
        frame.place(relx=0.5, rely=0.4, anchor="center")
        ttk.Label(frame, text="Diagnóstico Biométrico IA", style="Header.TLabel").grid(row=0, column=0, columnspan=2, pady=20)
        
        ttk.Label(frame, text="Peso (kg):").grid(row=1, column=0, pady=5, sticky="e")
        self.peso = ttk.Entry(frame, font=("Segoe UI", 11))
        self.peso.grid(row=1, column=1, pady=5)
        
        ttk.Label(frame, text="Estatura (m):").grid(row=2, column=0, pady=5, sticky="e")
        self.est = ttk.Entry(frame, font=("Segoe UI", 11))
        self.est.grid(row=2, column=1, pady=5)
        
        ttk.Label(frame, text="Calorías:").grid(row=3, column=0, pady=5, sticky="e")
        self.cal = ttk.Entry(frame, font=("Segoe UI", 11))
        self.cal.grid(row=3, column=1, pady=5)
        
        ttk.Button(frame, text="⚡ Ejecutar Modelo IA", command=self.ejecutar_ia).grid(row=4, columnspan=2, pady=25, ipadx=20)

    def ejecutar_ia(self):
        try:
            payload = {"peso": float(self.peso.get()), "estatura": float(self.est.get()), "calorias_consumidas": float(self.cal.get()), "nivel_actividad": "moderado"}
            resp = servicios_api.analizar_salud_ia(payload)
            if resp.status_code == 200:
                r = resp.json()
                res = f"IMC: {r.get('imc')} ({r.get('clasificacion_imc')})\nBalance: {r.get('estado_balance')}\n\nRecomendación IA:\n{r.get('recomendacion')}"
                messagebox.showinfo("Resultados IA", res)
            else:
                messagebox.showerror("Error", "Validación Pydantic falló.")
        except Exception: 
            messagebox.showerror("Error", "Ingrese números válidos y asegúrese de que FastAPI esté corriendo.")