import csv
import os

ARQUIVO = "dados_estudo.csv"

def salvar_sessao(materia, duracao, data):
    existe = os.path.exists(ARQUIVO)
    with open(ARQUIVO, mode="a", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        if not existe:
            escritor.writerow(["materia", "duracao", "data"])  # Cabeçalho
        escritor.writerow([materia, duracao, data])

def obter_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)
