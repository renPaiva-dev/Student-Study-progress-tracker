import tkinter as tk
from registro import abrir_janela_registro
from graficos import mostrar_graficos

def main():
    janela = tk.Tk()
    janela.title("Sistema de Controle de Estudos")
    janela.geometry("300x200")

    titulo = tk.Label(janela, text="Controle de Estudos", font=("Arial", 14, "bold"))
    titulo.pack(pady=15)

    tk.Button(janela, text="Registrar Estudo", width=25, command=abrir_janela_registro).pack(pady=5)
    tk.Button(janela, text="Ver Gráficos", width=25, command=mostrar_graficos).pack(pady=5)

    janela.mainloop()

if __name__ == "__main__":
    main()
