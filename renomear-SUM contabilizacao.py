import os

pasta = r'C:\Users\malik.mourad\Downloads\SUM001_2026_02_CONTABILIZACAO'
sufixo = 'SUM001_fev_26'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith('SUM001_Sumario_'):
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        
    if nome_arquivo.startswith('SUM001_Sumario_'):
        nome_empresa = nome_arquivo.replace('SUM001_Sumario_', '').replace('.pdf', '')

        # Novo nome no formato desejado: NOMEEMPRESA_SUM001_jan_26.pdf
        novo_nome = f"{nome_empresa}_{sufixo}.pdf"
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
