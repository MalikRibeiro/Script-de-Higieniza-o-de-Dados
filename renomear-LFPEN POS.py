import os

pasta = r'C:\Users\malik.mourad\Downloads\LFPEN001_2026_03_LIQUIDACAO_DE_PENALIDADES'
sufixo = 'LFPEN001_mar_26 (pós)'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf'):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        # Remove prefixo "LFPEN001_Liquidacao_de_Penalidades_"
        if nome_arquivo.startswith('LFPEN001_Liquidacao_de_Penalidades_'):
            nome_empresa = nome_arquivo.replace('LFPEN001_Liquidacao_de_Penalidades_', '').replace('.pdf', '')
            novo_nome = f"{nome_empresa}_{sufixo}.pdf"
            caminho_novo = os.path.join(pasta, novo_nome)

            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {nome_arquivo} -> {novo_nome}')
