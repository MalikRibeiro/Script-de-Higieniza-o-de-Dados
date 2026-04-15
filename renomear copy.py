import os

caminho_pasta = r'C:\Users\malik.mourad\Downloads'

for nome_arquivo in os.listdir(caminho_pasta):
    nome_sem_extensao, extensao = os.path.splitext(nome_arquivo)
    
    # Substituir espaços e pontos por "_" no nome, exceto a extensão
    novo_nome = nome_sem_extensao.replace(' ', '_').replace('.', '_')
    
    # Adicionar a extensão '.pdf'
    novo_nome += '.pdf'
    
    caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
    caminho_novo = os.path.join(caminho_pasta, novo_nome)
    
    os.rename(caminho_antigo, caminho_novo)

print("Renomeação concluída.")
