"""
Cria estrutura de pastas para Reapuração de Desconto e os relatórios DCT001, DCT004, DCT006.

Estrutura criada:
{BASE}\{ano}\{ano}{MM}\Desconto TUSD-TUST\{texto_evento}\{DCTxxx}

Comentários em PT-BR. Use DRY_RUN=True para simular.
"""
from pathlib import Path
import re
import logging
from typing import List, Tuple

# Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

def limpar_nome_pasta(nome: str) -> str:
    # Remove caracteres inválidos em nomes de pasta do Windows
    caracteres_invalidos = r'[<>:"/\\|?*]'
    nome_limpo = re.sub(caracteres_invalidos, '_', nome)
    nome_limpo = nome_limpo.strip()
    nome_limpo = nome_limpo.rstrip('.')  # remove ponto final se houver
    return nome_limpo

def criar_estrutura_dct(
    caminho_base: str,
    eventos: List[Tuple[int, int, str]],
    codigos_dct: List[str] = None,
    dry_run: bool = True
) -> None:
    base = Path(caminho_base)
    if codigos_dct is None:
        codigos_dct = ['DCT001', 'DCT004', 'DCT006']

    logger.info(f"{'[DRY RUN] ' if dry_run else ''}Iniciando criação de estrutura DCT")
    logger.info(f"Caminho base: {base}")
    logger.info(f"Total de eventos: {len(eventos)}")

    pastas_criadas = 0
    pastas_existentes = 0
    erros = 0

    for ano, mes, texto_evento in eventos:
        ano_mes = f"{ano}{int(mes):02d}"
        texto_limpo = limpar_nome_pasta(texto_evento)

        caminho_evento = base / str(ano) / ano_mes / "Desconto na TUSD TUST" / texto_limpo

        # Primeiro garante que a pasta do evento exista (sem os DCTs)
        try:
            if not dry_run:
                caminho_evento.mkdir(parents=True, exist_ok=True)
            logger.info(f"  [EVENTO] Garantido: {caminho_evento}")
        except Exception as e:
            logger.error(f"  [ERRO] Não foi possível criar pasta do evento {caminho_evento}: {e}")
            erros += 1
            continue

        # Cria as pastas DCT dentro do evento
        for codigo_dct in codigos_dct:
            caminho_completo = caminho_evento / codigo_dct
            try:
                if caminho_completo.exists():
                    logger.info(f"    [EXISTE] {caminho_completo}")
                    pastas_existentes += 1
                else:
                    if not dry_run:
                        caminho_completo.mkdir(parents=True, exist_ok=True)
                        logger.info(f"    [CRIADA] {caminho_completo}")
                        pastas_criadas += 1
                    else:
                        logger.info(f"    [DRY RUN] Seria criada: {caminho_completo}")
                        pastas_criadas += 1
            except Exception as e:
                logger.error(f"    [ERRO] Falha ao criar {caminho_completo}: {e}")
                erros += 1

    # Resumo
    logger.info("\n" + "="*60)
    logger.info(f"Resumo{' (DRY RUN)' if dry_run else ''}: Criadas/Simuladas={pastas_criadas}  Existentes={pastas_existentes}  Erros={erros}")
    logger.info("="*60)

if __name__ == "__main__":
    # Caminho base (conforme seu padrão)
    CAMINHO_BASE = r"C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE"

    # Lista de eventos (ano, mês, texto_evento)
    EVENTOS = [
        (2013, 11, "13ª REAPURAÇÃO DE DESCONTO"),
        (2013, 12, "13ª REAPURAÇÃO DE DESCONTO"),
        (2014, 2,  "13ª REAPURAÇÃO DE DESCONTO"),
        (2015, 2,  "20ª REAPURAÇÃO DE DESCONTO"),
        (2016, 2,  "18ª REAPURAÇÃO DE DESCONTO"),
        (2017, 2,  "16ª REAPURAÇÃO DE DESCONTO"),
        (2018, 2,  "10ª REAPURAÇÃO DE DESCONTO"),
        (2019, 2,  "07ª REAPURAÇÃO DE DESCONTO"),
        (2020, 2,  "06ª REAPURAÇÃO DE DESCONTO"),
        (2021, 2,  "09ª REAPURAÇÃO DE DESCONTO"),
        (2023, 11, "03ª REAPURAÇÃO DE DESCONTO"),
        (2023, 12, "05ª REAPURAÇÃO DE DESCONTO"),
        (2024, 1,  "05ª REAPURAÇÃO DE DESCONTO"),
        (2024, 2,  "04ª REAPURAÇÃO DE DESCONTO"),
        (2025, 1,  "03ª REAPURAÇÃO DE DESCONTO"),
        (2025, 2,  "02ª REAPURAÇÃO DE DESCONTO"),
        (2025, 10,  "01ª REAPURAÇÃO DE DESCONTO"),
    ]

    # Relatórios (caso queira mudar a lista)
    CODIGOS_DCT = ['DCT001', 'DCT004', 'DCT006']

    # Segurança: True apenas simula
    DRY_RUN = False

    print("\n=== SCRIPT CRIAR PASTAS DE REAPURAÇÃO (DCT) ===\n")
    if DRY_RUN:
        print("⚠️  MODO DRY RUN: Nenhuma pasta será criada. Ajuste DRY_RUN = False para aplicar.\n")

    criar_estrutura_dct(
        caminho_base=CAMINHO_BASE,
        eventos=EVENTOS,
        codigos_dct=CODIGOS_DCT,
        dry_run=DRY_RUN
    )
    print("\n=== FINALIZADO ===\n")
