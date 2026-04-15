import os

pasta = r'C:\Users\malik.mourad\Downloads\LFN001_2026_02_LIQUIDACAO_MCP'
prefixo_busca = 'LFN001_Liquidacao_Financeira_'
mes_ano = 'fev_26'

for nome_arquivo in os.listdir(pasta):
    if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith(prefixo_busca):
        caminho_antigo = os.path.join(pasta, nome_arquivo)

        # Extrai o nome da empresa
        nome_empresa = nome_arquivo.replace(prefixo_busca, '').replace('.pdf', '')

        # Novo nome no padrão [EMPRESA]_LFN001_mar_25.pdf
        novo_nome = f"{nome_empresa}_LFN001_{mes_ano}.pdf"
        caminho_novo = os.path.join(pasta, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")