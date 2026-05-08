import os

# Caminho da pasta
pasta = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Boletos Bancários - Contribuição\2026\202604"

# Lista todos os arquivos na pasta
for arquivo in os.listdir(pasta):
    # Verifica se é um arquivo (não uma subpasta)
    if os.path.isfile(os.path.join(pasta, arquivo)):
        # Substitui espaços por underscores
        novo_nome = arquivo.replace(" ", "_")
        # Corrige o sufixo _pdf para .pdf
        if novo_nome.endswith("_pdf"):
            novo_nome = novo_nome[:-4] + ".pdf"
        caminho_original = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        # Renomeia o arquivo diretamente
        os.rename(caminho_original, caminho_novo)
        print(f"Renomeado: {arquivo} -> {novo_nome}")