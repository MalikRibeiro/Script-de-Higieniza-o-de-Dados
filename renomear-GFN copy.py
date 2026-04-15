import os
import shutil
import datetime

# --- Cálculo dinâmico do mês anterior ---
hoje = datetime.date.today()
ano = hoje.year
# Lógica para calcular o mês anterior (se for janeiro, volta para dezembro do ano anterior)
mes = hoje.month - 1 if hoje.month > 1 else 12
ano_ref = ano if hoje.month > 1 else ano - 1

# Mapa para obter a abreviação do mês (ex: 'set' para setembro)
nomes_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
mes_abrev = nomes_meses[mes - 1]
# Formata o mês para o nome da pasta (ex: 202509)
mes_formatado = f"{ano_ref}{mes:02d}"

# --- Sufixo dinâmico para o novo nome do arquivo ---
# Exemplo: GFN001_set_25
sufixo = f"GFN001_{mes_abrev}_{str(ano_ref)[2:]}"

# --- Caminho dinâmico da pasta de origem (onde os arquivos são baixados) ---
# CORREÇÃO APLICADA AQUI para corresponder ao nome da pasta de download
pasta_origem = fr"C:\Users\victor.rosa\Downloads\GFN001_{ano_ref}_{mes:02d}_APORTE_DE_GARANTIAS"

# --- Caminho base de destino (mesma base do LFRES) ---
base_destino = r"C:\Users\victor.rosa\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE"

# --- Pasta de destino dinâmica e estruturada ---
# Exemplo: ...\Relatórios CCEE\2025\202509\Garantia Financeira\GFN001
pasta_destino = os.path.join(base_destino, str(ano_ref), mes_formatado, 'Garantia Financeira', 'GFN001')

# Cria a estrutura de pastas de destino, se não existir
os.makedirs(pasta_destino, exist_ok=True)

# --- Renomear e mover os arquivos ---
# Verifica se a pasta de origem realmente existe antes de prosseguir
if not os.path.exists(pasta_origem):
    print(f"❌ Atenção: A pasta de origem não foi encontrada:\n{pasta_origem}")
else:
    for nome_arquivo in os.listdir(pasta_origem):
        # Filtra apenas os arquivos PDF relevantes
        if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith('GFN001_Garantia_Financeira_'):
            caminho_antigo = os.path.join(pasta_origem, nome_arquivo)

            # Extrai o nome da empresa do nome original do arquivo
            nome_empresa = nome_arquivo.replace('GFN001_Garantia_Financeira_', '').replace('.pdf', '')

            # Monta o novo nome e o caminho de destino
            novo_nome = f"{nome_empresa}_{sufixo}.pdf"
            caminho_novo = os.path.join(pasta_destino, novo_nome)

            # Lógica para evitar sobrescrever um arquivo que já existe
            contador = 1
            while os.path.exists(caminho_novo):
                nome_base, ext = os.path.splitext(novo_nome)
                if nome_base.endswith(f"_{contador-1}"):
                    nome_base = nome_base.rsplit('_', 1)[0]
                caminho_novo = os.path.join(pasta_destino, f"{nome_base}_{contador}{ext}")
                contador += 1

            # Move o arquivo da origem para o destino com o novo nome
            shutil.move(caminho_antigo, caminho_novo)
            print(f"✅ Movido e renomeado: {nome_arquivo} -> {caminho_novo}")

    print(f"\n📁 Processo concluído com sucesso!\nArquivos salvos em:\n{pasta_destino}")