import os

pasta = r'C:\Users\malik.mourad\Downloads\VCA001_2026_04_APURACAO_DE_VOTOS'
prefixo_busca = 'VCA001_Memoria_do_Calculo_de_Votos_e_Contribuicao_Associativa_'
sufixo_final = 'VCA001 abr.26'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith(prefixo_busca):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        # Extrai o nome da empresa e substitui underscores por espaços
        nome_empresa = nome_arquivo.replace(prefixo_busca, '').replace('.pdf', '')
        nome_empresa_formatado = nome_empresa.replace('_', ' ')

        # Novo nome com padrão desejado
        novo_nome = f"{nome_empresa_formatado} {sufixo_final}.pdf"
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
