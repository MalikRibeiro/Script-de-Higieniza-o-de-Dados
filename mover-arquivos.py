"""
Organizar Relatórios CCEE
Move arquivos Excel para suas respectivas pastas com base no nome do relatório.
"""

import os
import shutil
from pathlib import Path

# ─── CONFIGURAÇÃO ────────────────────────────────────────────────────────────

BASE_PATH = Path(r'C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGC\Macro\Relatorios CCEE')

# Pastas de destino (o script busca esses nomes dentro do nome do arquivo)
PASTAS = [
    "GFN001",
    "LFN001",
    "LFRCEN001",
    "LFRCGF001",
    "LFRES001",
    "RCAP002",
    "SUM001",
]

# Extensões Excel aceitas
EXTENSOES_EXCEL = {".xlsx", ".xlsm", ".xls", ".xlsb"}

# ─── EXECUÇÃO ─────────────────────────────────────────────────────────────────

def organizar():
    if not BASE_PATH.exists():
        print(f"[ERRO] Caminho base não encontrado:\n  {BASE_PATH}")
        return

    movidos = 0
    sem_match = []

    # Lista apenas arquivos diretos na pasta base (não entra em subpastas)
    arquivos = [
        f for f in BASE_PATH.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSOES_EXCEL
    ]

    print(f"{'─'*60}")
    print(f"  Relatórios CCEE — Organizador de Arquivos")
    print(f"{'─'*60}")
    print(f"  Arquivos Excel encontrados na raiz: {len(arquivos)}\n")

    for arquivo in arquivos:
        nome = arquivo.name
        destino_encontrado = None

        # Verifica qual pasta corresponde ao nome do arquivo (case-insensitive)
        for pasta in PASTAS:
            if pasta.upper() in nome.upper():
                destino_encontrado = pasta
                break  # Usa o primeiro match (mais específico primeiro via ordem da lista)

        if destino_encontrado:
            pasta_destino = BASE_PATH / destino_encontrado
            pasta_destino.mkdir(exist_ok=True)  # Garante que a pasta existe

            destino_arquivo = pasta_destino / nome

            # Evita sobrescrever arquivo existente
            if destino_arquivo.exists():
                print(f"  [PULADO]  Já existe → {destino_encontrado}\\{nome}")
                continue

            shutil.move(str(arquivo), str(destino_arquivo))
            print(f"  [OK]      {nome}")
            print(f"            → {destino_encontrado}\\")
            movidos += 1
        else:
            sem_match.append(nome)

    # ─── RESUMO ───────────────────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  ✅ Arquivos movidos:  {movidos}")
    print(f"  ⚠️  Sem correspondência: {len(sem_match)}")

    if sem_match:
        print(f"\n  Arquivos que não foram movidos (nenhuma pasta compatível):")
        for nome in sem_match:
            print(f"    • {nome}")

    print(f"{'─'*60}")


if __name__ == "__main__":
    resposta = input("\n⚠️  Isso irá mover arquivos. Deseja continuar? (s/n): ").strip().lower()
    if resposta == "s":
        organizar()
    else:
        print("Operação cancelada.")