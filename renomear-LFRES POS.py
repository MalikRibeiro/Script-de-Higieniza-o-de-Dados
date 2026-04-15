import os

pasta = r'C:\Users\malik.mourad\Downloads\LFRES001_2025_11_LIQUIDACAO_ENERGIA_DE_RESERVA'
sufixo = 'LFRES_nov_25 (Pós)'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf'):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        # Remove prefixo "LFRES001_Liquidacao_da_Energia_de_Reserva_"
        if nome_arquivo.startswith('LFRES001_Liquidacao_da_Energia_de_Reserva_'):
            nome_empresa = nome_arquivo.replace('LFRES001_Liquidacao_da_Energia_de_Reserva_', '').replace('.pdf', '')
            novo_nome = f"{nome_empresa}_{sufixo}.pdf"
            caminho_novo = os.path.join(pasta, novo_nome)

            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {nome_arquivo} -> {novo_nome}')
