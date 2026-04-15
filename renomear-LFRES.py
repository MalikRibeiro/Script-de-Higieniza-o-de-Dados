import os
import shutil
import datetime

# --- Cálculo dinâmico do mês anterior ---
hoje = datetime.date.today()
ano = hoje.year
mes = hoje.month - 1 if hoje.month > 1 else 12
ano_ref = ano if hoje.month > 1 else ano - 1

# Mapas para abreviações
nomes_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
mes_abrev = nomes_meses[mes - 1]
mes_formatado = f"{ano_ref}{mes:02d}"  # ex: 202509

# --- Sufixo dinâmico ---
sufixo = f"LFRES001_{mes_abrev}_{str(ano_ref)[2:]}"

# --- Caminho dinâmico da pasta de origem ---
pasta_origem = fr"C:\Users\malik.mourad\Downloads\LFRES001_{ano_ref}_{mes:02d}_LIQUIDACAO_ENERGIA_DE_RESERVA"

# --- Caminho base de destino ---
base_destino = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE"

# --- Pasta de destino dinâmica ---                                                                           # (Pós)
pasta_destino = os.path.join(base_destino, str(ano_ref), mes_formatado, 'Liquidação da Energia de Reserva', 'LFRES001')
os.makedirs(pasta_destino, exist_ok=True)

# --- Renomear e mover ---
for nome_arquivo in os.listdir(pasta_origem):
    if nome_arquivo.endswith('.pdf') and nome_arquivo.startswith('LFRES001_Liquidacao_da_Energia_de_Reserva_'):
        caminho_antigo = os.path.join(pasta_origem, nome_arquivo)

        nome_empresa = nome_arquivo.replace('LFRES001_Liquidacao_da_Energia_de_Reserva_', '').replace('.pdf', '')
        novo_nome = f"{nome_empresa}_{sufixo}.pdf"
        #novo_nome = f"{nome_empresa}_{sufixo} (Pós).pdf"
        caminho_novo = os.path.join(pasta_destino, novo_nome)

        # Evita sobrescrever caso já exista
        contador = 1
        while os.path.exists(caminho_novo):
            nome_base, ext = os.path.splitext(novo_nome)
            caminho_novo = os.path.join(pasta_destino, f"{nome_base}_{contador}{ext}")
            contador += 1

        shutil.move(caminho_antigo, caminho_novo)
        print(f"✅ Movido e renomeado: {nome_arquivo} -> {caminho_novo}")

print(f"\n📁 Processo concluído com sucesso!\nArquivos salvos em:\n{pasta_destino}")
