import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# Variáveis globais para armazenar as entradas
entidades = []
processos = []
depositos = []

def criar_campos_relacionamento():
    global entidades, processos, depositos

    # Limpar campos anteriores de relacionamentos
    for widget in frame_relacionamentos.winfo_children():
        widget.destroy()
    
    # Relacionamento Entidade x Processo
    ttk.Label(frame_relacionamentos, text="Relacionamento Entidade x Processo", font=("Arial", 16), background="#0D1B2A", foreground="white").pack(pady=10)
    for entidade in entidades:
        ttk.Label(frame_relacionamentos, text=f"Entidade: {entidade.get()}", font=("Arial", 14), background="#0D1B2A", foreground="white").pack(pady=5)
        for processo in processos:
            frame = tk.Frame(frame_relacionamentos, background="#0D1B2A")
            frame.pack(pady=5)
            ttk.Label(frame, text=f"Processo: {processo.get()}", font=("Arial", 12), background="#0D1B2A", foreground="white").grid(row=0, column=0, padx=5)
            ctk.CTkComboBox(frame, values=["in", "out"], fg_color="#1B263B").grid(row=0, column=1, padx=5)
            ctk.CTkEntry(frame, placeholder_text="Nome da Relação", fg_color="white", placeholder_text_color="black", text_color="black").grid(row=0, column=2, padx=5)
    
    # Relacionamento Processo x Depósito
    ttk.Label(frame_relacionamentos, text="Relacionamento Processo x Depósito", font=("Arial", 16), background="#0D1B2A", foreground="white").pack(pady=10)
    for processo in processos:
        print("processo")
        ttk.Label(frame_relacionamentos, text=f"Processo: {processo.get()}", font=("Arial", 14), background="#0D1B2A", foreground="white").pack(pady=5)
        for deposito in depositos:
            frame = tk.Frame(frame_relacionamentos, background="#0D1B2A")
            frame.pack(pady=5)
            ttk.Label(frame, text=f"Depósito: {deposito.get()}", font=("Arial", 12), background="#0D1B2A", foreground="white").grid(row=0, column=0, padx=5)
            ctk.CTkComboBox(frame, values=["in", "out"], fg_color="#1B263B").grid(row=0, column=1, padx=5)
            ctk.CTkEntry(frame, placeholder_text="Nome da Relação", fg_color="white", placeholder_text_color="black", text_color="black").grid(row=0, column=2, padx=5)

def criar_campos(tipo, quantidade, frame):
    global entidades, processos, depositos
    if tipo == "entidade":
        entidades = []
        for i in range(quantidade):
            entry = ctk.CTkEntry(frame, placeholder_text=f"Nome Entidade {i+1}", fg_color="white", placeholder_text_color="black", text_color="black")
            entry.pack(pady=5)
            entidades.append(entry)
    elif tipo == "processo":
        processos = []
        for i in range(quantidade):
            entry = ctk.CTkEntry(frame, placeholder_text=f"Nome Processo {i+1}", fg_color="white", placeholder_text_color="black", text_color="black")
            entry.pack(pady=5)
            processos.append(entry)
    elif tipo == "deposito":
        depositos = []
        for i in range(quantidade):
            entry = ctk.CTkEntry(frame, placeholder_text=f"Nome Depósito {i+1}", fg_color="white", placeholder_text_color="black", text_color="black")
            entry.pack(pady=5)
            depositos.append(entry)

def atualizar_campos(event=None):
    # Limpar campos anteriores
    for widget in frame_entidades.winfo_children():
        widget.destroy()
    for widget in frame_processos.winfo_children():
        widget.destroy()
    for widget in frame_depositos.winfo_children():
        widget.destroy()
    
    try:
        qtd_entidades = int(entry_qtd_entidades.get())
        qtd_processos = int(entry_qtd_processos.get())
        qtd_depositos = int(entry_qtd_depositos.get())
    except ValueError:
        return
    
    criar_campos("entidade", qtd_entidades, frame_entidades)
    criar_campos("processo", qtd_processos, frame_processos)
    criar_campos("deposito", qtd_depositos, frame_depositos)

def mostrar_relacionamentos():
    criar_campos_relacionamento()

def alterar_tema(valor):
    ctk.set_appearance_mode(valor)
    if valor == "dark":
        app.configure(bg="black")
        scrollable_frame.configure(bg="black")
        frame_entidades.configure(bg="black")
        frame_processos.configure(bg="black")
        frame_depositos.configure(bg="black")
        frame_relacionamentos.configure(bg="black")
        tema_var.set("dark")
    else:
        app.configure(bg="white")
        scrollable_frame.configure(bg="white")
        frame_entidades.configure(bg="white")
        frame_processos.configure(bg="white")
        frame_depositos.configure(bg="white")
        frame_relacionamentos.configure(bg="white")
        tema_var.set("light")

# Configuração Inicial do CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Interface de Relacionamento de Objetos")
app.geometry("1200x800")

# Menu fixado à esquerda
frame_menu = ctk.CTkFrame(app, corner_radius=0, fg_color="#1B263B")
frame_menu.place(relx=0, rely=0, relheight=1, relwidth=0.2)

# Adicionar opções ao menu
ctk.CTkButton(frame_menu, text="Opção 1", corner_radius=0).pack(fill="x", padx=10, pady=10)
ctk.CTkButton(frame_menu, text="Opção 2", corner_radius=0).pack(fill="x", padx=10, pady=10)
ctk.CTkButton(frame_menu, text="Opção 3", corner_radius=0).pack(fill="x", padx=10, pady=10)
ctk.CTkButton(frame_menu, text="Opção 4", corner_radius=0).pack(fill="x", padx=10, pady=10)

# Adicionar logo
logo = Image.open("bannerc.png")
logo = logo.resize((240, 135), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(app, image=logo, bg="#0D1B2A")
logo_label.place(relx=0.2, rely=0, anchor="nw", y=20, x=20)

frame_principal = ctk.CTkFrame(app, corner_radius=0)
frame_principal.place(relx=0.2, rely=0.25, relwidth=0.8, relheight=0.65)
canvas = tk.Canvas(frame_principal, bg="black")
scrollbar = ctk.CTkScrollbar(frame_principal, orientation="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="black")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Permitir rolagem com o scroll do mouse
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

# Adicionar widget de mudança de tema
tema_var = tk.StringVar(value="dark")
ttk.Label(scrollable_frame, text="Alterar Tema", font=("Arial", 16), background="black", foreground="white").pack(padx=(frame_principal.winfo_width()*2))
ttk.Combobox(scrollable_frame, textvariable=tema_var, values=["dark", "light"], state="readonly", postcommand=lambda: alterar_tema(tema_var.get())).pack(pady=5)

# Entrada de Quantidade de Entidades
ttk.Label(scrollable_frame, text="Quantidade de Entidades", font=("Arial", 16), background="black", foreground="white").pack(pady=10)
entry_qtd_entidades = ctk.CTkEntry(scrollable_frame, fg_color="white", placeholder_text_color="black", text_color="black")
entry_qtd_entidades.pack(pady=5)
entry_qtd_entidades.bind("<Return>", atualizar_campos)

frame_entidades = tk.Frame(scrollable_frame, bg="black")
frame_entidades.pack(pady=10)

# Entrada de Quantidade de Processos
ttk.Label(scrollable_frame, text="Quantidade de Processos", font=("Arial", 16), background="black", foreground="white").pack(pady=10)
entry_qtd_processos = ctk.CTkEntry(scrollable_frame, fg_color="white", placeholder_text_color="black", text_color="black")
entry_qtd_processos.pack(pady=5)
entry_qtd_processos.bind("<Return>", atualizar_campos)

frame_processos = tk.Frame(scrollable_frame, bg="black")
frame_processos.pack(pady=20, padx=20, fill="both", expand=True)

# Entrada de Quantidade de Depósitos
ttk.Label(scrollable_frame, text="Quantidade de Depósitos", font=("Arial", 16), background="black", foreground="white").pack(pady=10)
entry_qtd_depositos = ctk.CTkEntry(scrollable_frame, fg_color="white", placeholder_text_color="black", text_color="black")
entry_qtd_depositos.pack(pady=5)
entry_qtd_depositos.bind("<Return>", atualizar_campos)



frame_depositos = tk.Frame(scrollable_frame, bg="black")
frame_depositos.pack(pady=20, padx=20, fill="both", expand=True)
frame_relacionamentos = tk.Frame(scrollable_frame, bg="black")

frame_relacionamentos.pack(pady=20, padx=20, fill="both", expand=True)



canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Botão para criar relacionamentos
ctk.CTkButton(app, text="Criar Relacionamentos", command=mostrar_relacionamentos).place(relx=0.75, rely=0.95, anchor="center")

# Botão para criar
ctk.CTkButton(app, text="Criar", command=lambda: print("Botão Criar clicado!")).place(relx=0.85, rely=0.95, anchor="center")

# Corrigir o bug de rolagem
def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)

app.mainloop()
