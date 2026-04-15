import shutil
from pathlib import Path

# Definição dos caminhos (usando 'r' antes da string para ignorar caracteres de escape)
caminho_origem = Path(r'C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE\2025\202510\Liquidação da Energia de Reserva\LFRES001')
caminho_destino = Path(r'C:\Users\malik.mourad\ELECTRA COMERCIALIZADORA DE ENERGIA S.A\GE - ECE\DGCA\DGA\CCEE\Relatórios CCEE\2025\202510\Liquidação da Energia de Reserva\LFRES001 (Pós)')

def mover_e_renomear_arquivos():
    # Verifica se a pasta de origem existe
    if not caminho_origem.exists():
        print(f"Erro: A pasta de origem não foi encontrada:\n{caminho_origem}")
        return

    # Cria a pasta de destino se ela não existir
    caminho_destino.mkdir(parents=True, exist_ok=True)
    
    arquivos_movidos = 0

    # Itera sobre todos os arquivos PDF na pasta que terminam com '_1.pdf'
    # O padrão '*_1.pdf' garante que pegaremos apenas os arquivos desejados
    for arquivo in caminho_origem.glob('*_1.pdf'):
        try:
            # Lógica do novo nome:
            # 1. Pega o nome sem extensão (ex: ARQUIVO_out_25_1)
            nome_original = arquivo.stem 
            
            # 2. Remove os últimos 2 caracteres ('_1') e adiciona ' (Pós)'
            # Resultado esperado: ARQUIVO_out_25 (Pós)
            novo_nome_stem = nome_original[:-2] + " (Pós)"
            
            # 3. Reconstrói o nome com a extensão (.pdf)
            novo_nome_completo = novo_nome_stem + arquivo.suffix
            
            # Define o caminho final completo
            destino_final = caminho_destino / novo_nome_completo

            # Move o arquivo
            shutil.move(str(arquivo), str(destino_final))
            
            print(f"Sucesso: '{arquivo.name}' -> movido e renomeado para '{novo_nome_completo}'")
            arquivos_movidos += 1
            
        except Exception as e:
            print(f"Erro ao mover '{arquivo.name}': {e}")

    if arquivos_movidos == 0:
        print("\nNenhum arquivo terminado em '_1.pdf' foi encontrado na pasta.")
    else:
        print(f"\nProcesso finalizado. Total de arquivos movidos: {arquivos_movidos}")

if __name__ == "__main__":
    mover_e_renomear_arquivos()