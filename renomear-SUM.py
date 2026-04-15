import os
import shutil
import datetime

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO - Verifique apenas o prefixo do arquivo
# -----------------------------------------------------------------------------

# IMPORTANTE: Confirme se o prefixo EXATO dos arquivos PDF é este.
# Verifique maiúsculas, minúsculas, acentos e underlines no nome do arquivo real.
prefixo_arquivo_real = 'SUM001_Sumario_'

# -----------------------------------------------------------------------------
# CÁLCULO DE DATA AUTOMÁTICO 
# -----------------------------------------------------------------------------

hoje = datetime.date.today()
ano_atual = hoje.year

# Lógica para calcular o mês anterior (se hoje for janeiro, volta para dezembro do ano anterior)
if hoje.month <= 2:
    mes_ref = hoje.month + 10
    ano_ref = hoje.year - 1
else:
    mes_ref = hoje.month - 2
    ano_ref = hoje.year

print(f"Data de hoje: {hoje}")
print(f"Mês de referência calculado: {mes_ref}/{ano_ref}")

# -----------------------------------------------------------------------------
# O restante do script usa as datas calculadas acima
# -----------------------------------------------------------------------------

# Mapas e formatações baseadas nas configurações
nomes_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
mes_abrev = nomes_meses[mes_ref - 1]
mes_formatado = f"{ano_ref}{mes_ref:02d}" # ex: 202509

# Sufixo dinâmico para o novo nome do arquivo (ex: SUM001_set_25)
sufixo = f"SUM001_{mes_abrev}_{str(ano_ref)[2:]}"

# Caminho dinâmico da pasta de origem (Downloads)
pasta_origem = fr"C:\Users\malik.mourad\Downloads\SUM001_{ano_ref}_{mes_ref:02d}_CONTABILIZACAO"

# Caminho base de destino
base_destino = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE"

# Pasta de destino dinâmica e estruturada (conforme solicitado)
# Padrão: ...\2025\202509\Sumário\SUM001
pasta_destino = os.path.join(base_destino, str(ano_ref), mes_formatado, 'Sumário', 'SUM001')

# Cria a estrutura de pastas de destino, se não existir
os.makedirs(pasta_destino, exist_ok=True)

print(f"\n🔎 Procurando arquivos em: {pasta_origem}")
print(f"🎯 Arquivos serão salvos em: {pasta_destino}")

# --- Renomear e mover os arquivos ---
arquivos_movidos = 0
if not os.path.exists(pasta_origem):
    print(f"\n❌ ERRO: A pasta de origem não foi encontrada. Verifique o caminho e as configurações de data.")
else:
    for nome_arquivo in os.listdir(pasta_origem):
        # Filtra apenas os arquivos PDF que começam com o prefixo correto
        if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith(prefixo_arquivo_real):
            caminho_antigo = os.path.join(pasta_origem, nome_arquivo)

            # Extrai o nome da empresa do nome original do arquivo
            nome_empresa = nome_arquivo.replace(prefixo_arquivo_real, '').replace('.pdf', '')

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
            print(f"✅ Movido e renomeado: {nome_arquivo} -> {os.path.basename(caminho_novo)}")
            arquivos_movidos += 1

# --- Mensagem final ---
print("\n" + "="*50)
if arquivos_movidos > 0:
    print(f"📁 Processo concluído com sucesso! {arquivos_movidos} arquivo(s) movido(s).")
    print(f"Arquivos salvos em:\n{pasta_destino}")
else:
    print("⚠️ Atenção: Nenhum arquivo correspondente foi encontrado na pasta de origem.")
    print("Por favor, verifique:")
    print(f"1. Se a pasta de origem existe: {pasta_origem}")
    print(f"2. Se os arquivos PDF realmente começam com o prefixo: '{prefixo_arquivo_real}'")
print("="*50)