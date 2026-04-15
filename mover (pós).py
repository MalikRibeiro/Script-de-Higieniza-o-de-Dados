import os
import shutil

pasta_origem = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE\2025\202505\Liquidação de Penalidades\LFPEN001"
pasta_destino = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE\2025\202505\Liquidação de Penalidades\LFPEN001 (Pós)"

# Criar pasta de destino se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Iterar pelos arquivos na pasta de origem
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith("(PÓS).pdf"):
        caminho_origem = os.path.join(pasta_origem, nome_arquivo)
        caminho_destino = os.path.join(pasta_destino, nome_arquivo)
        shutil.move(caminho_origem, caminho_destino)
        print(f"Movido {nome_arquivo} para {pasta_destino}")