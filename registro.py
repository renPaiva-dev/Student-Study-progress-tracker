import tkinter as tk
from tkinter import messagebox
from banco_dados import salvar_sessao
import datetime

def abrir_janela_registro():
    reg = tk.Toplevel()
    reg.title("Registrar Estudo")
    reg.geometry("300x200")

    tk.Label(reg, text="Matéria:").pack()
    entrada_materia = tk.Entry(reg)
    entrada_materia.pack()

    tk.Label(reg, text="Duração (min):").pack()
    entrada_duracao = tk.Entry(reg)
    entrada_duracao.pack()

    def salvar():
        materia = entrada_materia.get().strip()
        duracao = entrada_duracao.get().strip()
        data = datetime.date.today().isoformat()

        if materia and duracao.isdigit():
            salvar_sessao(materia, int(duracao), data)
            messagebox.showinfo("Sucesso", "Sessão registrada!")
            reg.destroy()
        else:
            messagebox.showerror("Erro", "Preencha corretamente.")

    tk.Button(reg, text="Salvar", command=salvar).pack(pady=10)
