import matplotlib.pyplot as plt
from banco_dados import obter_dados
from collections import defaultdict

def mostrar_graficos():
    dados = obter_dados()
    if not dados:
        print("Sem dados registrados.")
        return

    por_materia = defaultdict(int)
    for linha in dados:
        materia = linha["materia"]
        duracao = int(linha["duracao"])
        por_materia[materia] += duracao

    materias = list(por_materia.keys())
    tempos = list(por_materia.values())

    plt.figure(figsize=(8,5))
    plt.bar(materias, tempos, color='skyblue')
    plt.title("Tempo Total de Estudo por Matéria")
    plt.xlabel("Matéria")
    plt.ylabel("Minutos")
    plt.tight_layout()
    plt.show()
