"""Unir PDF - aplicativo simples para juntar arquivos PDF em um só."""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from pypdf import PdfWriter


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Unir PDF")
        self.geometry("560x420")
        self.minsize(460, 320)

        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Arquivos PDF (a ordem da lista é a ordem final):").pack(anchor="w")

        meio = ttk.Frame(frame)
        meio.pack(fill="both", expand=True, pady=6)

        self.lista = tk.Listbox(meio, selectmode="extended", activestyle="none")
        barra = ttk.Scrollbar(meio, command=self.lista.yview)
        self.lista.config(yscrollcommand=barra.set)
        self.lista.pack(side="left", fill="both", expand=True)
        barra.pack(side="left", fill="y")

        botoes = ttk.Frame(meio)
        botoes.pack(side="left", fill="y", padx=(8, 0))
        for texto, cmd in [
            ("Adicionar...", self.adicionar),
            ("Remover", self.remover),
            ("Subir", lambda: self.mover(-1)),
            ("Descer", lambda: self.mover(1)),
            ("Limpar", lambda: self.lista.delete(0, "end")),
        ]:
            ttk.Button(botoes, text=texto, command=cmd).pack(fill="x", pady=2)

        ttk.Button(frame, text="Unir e salvar...", command=self.unir).pack(fill="x", ipady=4)

    def adicionar(self):
        arquivos = filedialog.askopenfilenames(
            title="Selecione os PDFs", filetypes=[("PDF", "*.pdf")]
        )
        for a in arquivos:
            self.lista.insert("end", a)

    def remover(self):
        for i in reversed(self.lista.curselection()):
            self.lista.delete(i)

    def mover(self, direcao):
        sel = self.lista.curselection()
        if not sel:
            return
        indices = sel if direcao < 0 else reversed(sel)
        for i in indices:
            j = i + direcao
            if j < 0 or j >= self.lista.size():
                return
            if j in sel:
                continue
            texto = self.lista.get(i)
            self.lista.delete(i)
            self.lista.insert(j, texto)
        self.lista.selection_clear(0, "end")
        for i in sel:
            self.lista.selection_set(i + direcao)

    def unir(self):
        arquivos = self.lista.get(0, "end")
        if len(arquivos) < 2:
            messagebox.showwarning("Unir PDF", "Adicione pelo menos 2 arquivos.")
            return
        destino = filedialog.asksaveasfilename(
            title="Salvar como", defaultextension=".pdf", filetypes=[("PDF", "*.pdf")],
            initialfile="unido.pdf",
        )
        if not destino:
            return
        try:
            with PdfWriter() as w:
                for a in arquivos:
                    w.append(a)
                w.write(destino)
        except Exception as e:
            messagebox.showerror("Unir PDF", f"Erro ao unir os arquivos:\n{e}")
            return
        messagebox.showinfo("Unir PDF", f"PDF criado com sucesso:\n{destino}")


if __name__ == "__main__":
    App().mainloop()
