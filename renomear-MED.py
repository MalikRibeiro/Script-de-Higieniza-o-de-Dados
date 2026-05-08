import os

pasta = r'C:\Users\malik.mourad\Downloads\MED003_2026_03_CONTABILIZACAO'
sufixo = 'MED003_mar_26'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith('MED003_Medicao_da_Geracao_e_Consumo_'):
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        
    if nome_arquivo.startswith('MED003_Medicao_da_Geracao_e_Consumo_'):
        nome_empresa = nome_arquivo.replace('MED003_Medicao_da_Geracao_e_Consumo_', '').replace('.pdf', '')

        # Novo nome no formato desejado: NOMEEMPRESA_MED003_mar_25.pdf
        novo_nome = f"{nome_empresa}_{sufixo}.pdf"
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
