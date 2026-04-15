import os
import pandas as pd

# Caminhos fornecidos
caminho_csv = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\Analistas\Malik\Template DRI - Book"
caminho_pasta_boletos = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Boletos Bancários - Contribuição\2025\202506"

# Lê o CSV com os nomes dos agentes
arquivo_csv = os.path.join(caminho_csv, "dri-book-relatorio-agentes-template.csv")
df = pd.read_csv(arquivo_csv, sep=';', encoding='utf-8')

# Normaliza nomes para facilitar a busca
def normaliza(texto):
    return ''.join(e for e in texto.upper() if e.isalnum())

nomes_agentes = df['Agentes'].dropna().unique()
nomes_normalizados = {normaliza(nome): nome for nome in nomes_agentes}

# Renomeia os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta_boletos):
    if not nome_arquivo.lower().endswith(".pdf"):
        continue

    nome_sem_ext = os.path.splitext(nome_arquivo)[0]
    partes = nome_sem_ext.split(" CONTRIBUIÇÃO_CCEE")[0]  # Pega só o nome da empresa

    nome_match = normaliza(partes)
    nome_formatado = nomes_normalizados.get(nome_match)

    if nome_formatado:
        novo_nome = nome_arquivo.replace(partes, nome_formatado)
        caminho_antigo = os.path.join(caminho_pasta_boletos, nome_arquivo)
        caminho_novo = os.path.join(caminho_pasta_boletos, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
    else:
        print(f"[!] Nome não encontrado no CSV: {nome_arquivo}")
