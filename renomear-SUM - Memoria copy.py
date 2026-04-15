import os
import shutil
import datetime

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO - Verifique apenas o prefixo do arquivo
# -----------------------------------------------------------------------------

# IMPORTANTE: Confirme se o prefixo EXATO dos arquivos PDF é este.
prefixo_arquivo_real = 'SUM001_Sumario_'

# -----------------------------------------------------------------------------
# CÁLCULO DE DATA AUTOMÁTICO 
# -----------------------------------------------------------------------------

hoje = datetime.date.today()
ano_atual = hoje.year

# Lógica para calcular o mês anterior (Mês de referência)
mes_ref = hoje.month - 1 if hoje.month > 1 else 12
ano_ref = ano_atual if hoje.month > 1 else ano_atual - 1

# -----------------------------------------------------------------------------
# DEFINIÇÃO DE NOMES E CAMINHOS
# -----------------------------------------------------------------------------

nomes_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
mes_abrev = nomes_meses[mes_ref - 1]
mes_formatado = f"{ano_ref}{mes_ref:02d}" # ex: 202510

# Sufixo para renomear o arquivo (ex: _out_25)
sufixo = f"SUM001_{mes_abrev}_{str(ano_ref)[2:]}"

# Caminho da pasta de origem (Downloads)
pasta_origem = fr"C:\Users\victor.rosa\Downloads\SUM001_{ano_ref}_{mes_ref:02d}_MEMORIA_CALCULO_GARANTIA_FINANCEIRA"

# Caminho base de destino
base_destino = r"C:\Users\victor.rosa\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE"

# --- AQUI ESTÁ A MUDANÇA SOLICITADA ---
# Caminho: ...\2025\202510\Sumário\SUM001 - Memória_de_Cálculo
pasta_destino = os.path.join(
    base_destino, 
    str(ano_ref), 
    mes_formatado, 
    'Sumário', 
    'SUM001 - Memória_de_Cálculo'
)

# Cria toda a árvore de pastas se não existir
os.makedirs(pasta_destino, exist_ok=True)

print(f"Data Ref: {mes_ref}/{ano_ref}")
print(f"📂 Origem: {pasta_origem}")
print(f"🎯 Destino: {pasta_destino}")

# -----------------------------------------------------------------------------
# EXECUÇÃO (MOVER E RENOMEAR)
# -----------------------------------------------------------------------------

arquivos_movidos = 0

if not os.path.exists(pasta_origem):
    print(f"\n❌ ERRO: A pasta de origem não foi encontrada em Downloads.")
else:
    print("\nIniciando processamento...")
    for nome_arquivo in os.listdir(pasta_origem):
        # Filtra apenas os PDFs com o prefixo correto
        if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith(prefixo_arquivo_real):
            caminho_antigo = os.path.join(pasta_origem, nome_arquivo)

            # Limpa o nome para pegar apenas a empresa
            nome_empresa = nome_arquivo.replace(prefixo_arquivo_real, '').replace('.pdf', '')

            # Define o novo nome do arquivo
            novo_nome = f"{nome_empresa}_{sufixo}.pdf"
            caminho_novo = os.path.join(pasta_destino, novo_nome)

            # Evita sobrescrever arquivos existentes (adiciona _1, _2, etc)
            contador = 1
            while os.path.exists(caminho_novo):
                nome_base, ext = os.path.splitext(novo_nome)
                if nome_base.endswith(f"_{contador-1}"):
                    nome_base = nome_base.rsplit('_', 1)[0]
                caminho_novo = os.path.join(pasta_destino, f"{nome_base}_{contador}{ext}")
                contador += 1

            # Move e renomeia
            shutil.move(caminho_antigo, caminho_novo)
            print(f"✅ OK: {nome_empresa}")
            arquivos_movidos += 1

# --- Relatório Final ---
print("-" * 50)
if arquivos_movidos > 0:
    print(f"🚀 Sucesso! {arquivos_movidos} arquivos processados.")
    print(f"Salvos em: ...\\Sumário\\SUM001 - Memória_de_Cálculo")
else:
    print("⚠️ Nenhum arquivo encontrado para mover.")
print("-" * 50)