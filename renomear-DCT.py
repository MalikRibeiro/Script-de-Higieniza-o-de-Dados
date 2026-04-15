import os
import shutil
from datetime import date

# ==========================
# CONFIGURAÇÕES AUTOMÁTICAS
# ==========================

codigo_relatorio = "DCT001"

# Data de referência: dois meses antes do mês atual
hoje = date.today()
mes_ref_num = hoje.month - 2
ano_ref = hoje.year

if mes_ref_num <= 0:
    mes_ref_num += 12
    ano_ref -= 1

# Abreviações dos meses (pt-br)
meses_abrev = ["jan", "fev", "mar", "abr", "mai", "jun",
               "jul", "ago", "set", "out", "nov", "dez"]
mes_ref = meses_abrev[mes_ref_num - 1]
ano_ref_curto = str(ano_ref)[-2:]  # Ex: "25"
ano_mes_folder = f"{ano_ref}{mes_ref_num:02d}"  # Ex: 202508

# ==========================
# CAMINHOS
# ==========================

# Pasta de origem (ex: Downloads\DCT001_2025_08_APURACAO_DO_DESCONTO_NA_TUSD_TUST)
pasta_origem = (
    fr"C:\Users\malik.mourad\Downloads\{codigo_relatorio}_{ano_ref}_{mes_ref_num:02d}_APURACAO_DO_DESCONTO_NA_TUSD_TUST"
)

# Pasta de destino final
pasta_destino = (
    fr"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A"
    fr"\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE\{ano_ref}\{ano_mes_folder}"
    fr"\Desconto na TUSD TUST\{codigo_relatorio}"
)

# Sufixo que será adicionado no nome do arquivo
sufixo = f"{codigo_relatorio}_{mes_ref}_{ano_ref_curto}"

# ==========================
# PROCESSAMENTO
# ==========================

if not os.path.exists(pasta_origem):
    raise FileNotFoundError(f"❌ Pasta de origem não encontrada:\n{pasta_origem}")

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)
    print(f"📁 Pasta de destino criada: {pasta_destino}")

for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith(".pdf") and nome_arquivo.startswith(f"{codigo_relatorio}_Desconto_Mensal_de_Energia_Incentivada_"):
        caminho_antigo = os.path.join(pasta_origem, nome_arquivo)

        # Extrai o nome da empresa
        nome_empresa = (
            nome_arquivo
            .replace(f"{codigo_relatorio}_Desconto_Mensal_de_Energia_Incentivada_", "")
            .replace(".pdf", "")
        )

        # Novo nome padronizado
        novo_nome = f"{nome_empresa}_{sufixo}.pdf"
        caminho_novo = os.path.join(pasta_destino, novo_nome)

        # Evita sobrescrever se já existir
        if os.path.exists(caminho_novo):
            print(f"⚠️ Arquivo já existe, pulando: {novo_nome}")
            continue

        # Renomeia e move
        shutil.move(caminho_antigo, caminho_novo)
        print(f"✅ {nome_arquivo} -> {novo_nome}")

print("\n✅ Processo concluído com sucesso!")
