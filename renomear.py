import os

caminho_pasta = r'C:\Users\malik.mourad\Downloads\ilovepdf_rotated'

print(f"Procurando arquivos em: {caminho_pasta}\n")
arquivos_renomeados = 0

# Verifica se o caminho existe antes de continuar
if not os.path.isdir(caminho_pasta):
    print("ERRO: O diretório não foi encontrado.")
else:
    # Itera sobre cada arquivo no diretório especificado
    for nome_arquivo in os.listdir(caminho_pasta):
        
        # Verifica se o texto '_rotated' está no nome do arquivo
        if '_rotated' in nome_arquivo:
            
            # Substitui '_rotated' por ''
            novo_nome = nome_arquivo.replace('_rotated', '')
            
            # Monta os caminhos completos
            caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
            caminho_novo = os.path.join(caminho_pasta, novo_nome)
            
            try:
                os.rename(caminho_antigo, caminho_novo)
                print(f"SUCESSO: '{nome_arquivo}' foi renomeado para '{novo_nome}'")
                arquivos_renomeados += 1
            except Exception as e:
                print(f"ERRO ao renomear '{nome_arquivo}': {e}")

print("\n--- Renomeação concluída. ---")
if arquivos_renomeados == 0:
    print("Nenhum arquivo contendo 'jun' foi encontrado para renomear.")
else:
    print(f"Total de {arquivos_renomeados} arquivo(s) renomeado(s).")
