import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from PIL import Image, ImageTk

class ObjectFormApp:
    def __init__(self, root):
        self.root = root
        self.style = Style(theme='superhero')
        self.root.title("Criação de Objetos")
        self.root.geometry("800x600")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.create_form()
        
        self.entities_frame = ttk.Frame(self.root, padding="10")
        self.entities_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.processes_frame = ttk.Frame(self.root, padding="10")
        self.processes_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.deposits_frame = ttk.Frame(self.root, padding="10")
        self.deposits_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.relationship_frame = ttk.Frame(self.root, padding="10")
        self.relationship_frame.pack(fill=tk.X, padx=10, pady=5)
    
    def create_form(self):
        form_frame = ttk.Frame(self.root, padding="10")
        form_frame.pack(fill=tk.X, padx=10, pady=10)

        # Banner Image
        banner_image = Image.open("bannerc.png")  # Coloque o caminho da sua imagem
        banner_image = banner_image.resize((780, 150))
        self.banner_photo = ImageTk.PhotoImage(banner_image)
        banner_label = ttk.Label(form_frame, image=self.banner_photo)
        banner_label.grid(row=0, column=0, columnspan=3, pady=10)


        # Quantidade de Entidades
        ttk.Label(form_frame, text="Quantidade de Entidades:").grid(row=1, column=0, pady=5, sticky=tk.W)
        self.entity_count = tk.StringVar(value='0')
        entity_entry = ttk.Entry(form_frame, textvariable=self.entity_count)
        entity_entry.grid(row=1, column=1, pady=5)
        self.entity_count.trace('w', self.update_entity_fields)

        # Quantidade de Processos
        ttk.Label(form_frame, text="Quantidade de Processos:").grid(row=2, column=0, pady=5, sticky=tk.W)
        self.process_count = tk.StringVar(value='0')
        process_entry = ttk.Entry(form_frame, textvariable=self.process_count)
        process_entry.grid(row=2, column=1, pady=5)
        self.process_count.trace('w', self.update_process_fields)

        # Quantidade de Depósitos
        ttk.Label(form_frame, text="Quantidade de Depósitos:").grid(row=3, column=0, pady=5, sticky=tk.W)
        self.deposit_count = tk.StringVar(value='0')
        deposit_entry = ttk.Entry(form_frame, textvariable=self.deposit_count)
        deposit_entry.grid(row=3, column=1, pady=5)
        self.deposit_count.trace('w', self.update_deposit_fields)
        
        # Submit Button
        ttk.Button(form_frame, text="Criar Relacionamentos", command=self.create_relationships).grid(row=4, column=0, columnspan=2, pady=10)
    
    def update_entity_fields(self, *args):
        try:
            entity_count = int(self.entity_count.get())
        except ValueError:
            entity_count = 0
        
        for widget in self.entities_frame.winfo_children():
            widget.destroy()
            
        self.entity_names = []
        
        for i in range(entity_count):
            entity_label = ttk.Label(self.entities_frame, text=f"Nome Entidade {i+1}:")
            entity_label.grid(row=i, column=0, pady=5, sticky=tk.W)
            entity_name = tk.StringVar(value=f"Entidade{i+1}")
            self.entity_names.append(entity_name)
            entity_entry = ttk.Entry(self.entities_frame, textvariable=entity_name)
            entity_entry.grid(row=i, column=1, pady=5)
    
    def update_process_fields(self, *args):
        try:
            process_count = int(self.process_count.get())
        except ValueError:
            process_count = 0
        
        for widget in self.processes_frame.winfo_children():
            widget.destroy()
        
        self.process_names = []
        
        for i in range(process_count):
            process_label = ttk.Label(self.processes_frame, text=f"Nome Processo {i+1}:")
            process_label.grid(row=i, column=0, pady=5, sticky=tk.W)
            process_name = tk.StringVar(value=f"Processo{i+1}")
            self.process_names.append(process_name)
            process_entry = ttk.Entry(self.processes_frame, textvariable=process_name)
            process_entry.grid(row=i, column=1, pady=5)
    
    def update_deposit_fields(self, *args):
        try:
            deposit_count = int(self.deposit_count.get())
        except ValueError:
            deposit_count = 0
        
        for widget in self.deposits_frame.winfo_children():
            widget.destroy()
        
        self.deposit_names = []
        
        for i in range(deposit_count):
            deposit_label = ttk.Label(self.deposits_frame, text=f"Nome Depósito {i+1}:")
            deposit_label.grid(row=i, column=0, pady=5, sticky=tk.W)
            deposit_name = tk.StringVar(value=f"Depósito{i+1}")
            self.deposit_names.append(deposit_name)
            deposit_entry = ttk.Entry(self.deposits_frame, textvariable=deposit_name)
            deposit_entry.grid(row=i, column=1, pady=5)
    
    def create_relationships(self):
        for widget in self.relationship_frame.winfo_children():
            widget.destroy()

        # Entidade x Processo
        ttk.Label(self.relationship_frame, text="Relacionamento Entidade x Processo").grid(row=0, column=0, columnspan=4, pady=10, sticky=tk.W)

        self.entity_process_relationships = []
        row = 1
        for entity_name in self.entity_names:
            ttk.Label(self.relationship_frame, text=f"{entity_name.get()}").grid(row=row, column=0, pady=5, sticky=tk.W)
            for process_name in self.process_names:
                rel_var = tk.StringVar()
                self.entity_process_relationships.append(rel_var)
                ttk.Label(self.relationship_frame, text=f"com {process_name.get()}").grid(row=row, column=1, pady=5, sticky=tk.W)
                ttk.Entry(self.relationship_frame, textvariable=rel_var).grid(row=row, column=2, pady=5)
                in_out_var = tk.StringVar(value="in")
                in_out_var.trace("w", lambda *args, var=in_out_var: self.validate_in_out(var))
                ttk.Combobox(self.relationship_frame, textvariable=in_out_var, values=["in", "out"], state="readonly").grid(row=row, column=3, pady=5)
                row += 1

        # Processo x Depósito
        ttk.Label(self.relationship_frame, text="Relacionamento Processo x Depósito").grid(row=row, column=0, columnspan=4, pady=10, sticky=tk.W)

        self.process_deposit_relationships = []
        row += 1
        for process_name in self.process_names:
            ttk.Label(self.relationship_frame, text=f"{process_name.get()}").grid(row=row, column=0, pady=5, sticky=tk.W)
            for deposit_name in self.deposit_names:
                rel_var = tk.StringVar()
                self.process_deposit_relationships.append(rel_var)
                ttk.Label(self.relationship_frame, text=f"com {deposit_name.get()}").grid(row=row, column=1, pady=5, sticky=tk.W)
                ttk.Entry(self.relationship_frame, textvariable=rel_var).grid(row=row, column=2, pady=5)
                in_out_var = tk.StringVar(value="in")
                in_out_var.trace("w", lambda *args, var=in_out_var: self.validate_in_out(var))
                ttk.Combobox(self.relationship_frame, textvariable=in_out_var, values=["in", "out"], state="readonly").grid(row=row, column=3, pady=5)
                row += 1

    def validate_in_out(self, var):
        if var.get() not in ["in", "out"]:
            messagebox.showerror("Erro de Entrada", "O valor de in/out deve ser 'in' ou 'out'.")
            var.set("in")

if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectFormApp(root)
    root.mainloop()
