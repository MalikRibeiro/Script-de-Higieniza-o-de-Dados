import os
from pypdf import PdfReader, PdfWriter

pasta_origem = r'C:\Users\malik.mourad\Downloads'
pasta_destino = r'C:\Users\malik.mourad\Downloads\Relatorios_CCEE_Corrigidos'

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

for arquivo in os.listdir(pasta_origem):
    if arquivo.endswith('.pdf') and not arquivo.startswith('~$'):
        caminho_in = os.path.join(pasta_origem, arquivo)
        caminho_out = os.path.join(pasta_destino, arquivo)

        try:
            reader = PdfReader(caminho_in)
            writer = PdfWriter()

            for pagina in reader.pages:
                # gira 90 graus pra direita
                pagina.rotate(90)
                writer.add_page(pagina)

            with open(caminho_out, 'wb') as f:
                writer.write(f)

            print(f"✅ Girado: {arquivo}")

        except Exception as e:
            print(f"❌ Erro em {arquivo}: {e}")

print("\n--- Todos os PDFs foram girados 90° ---")