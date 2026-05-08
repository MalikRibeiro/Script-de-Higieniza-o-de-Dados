import re

def extrair_lista_eventos(texto_bruto):
    padrao = r"Ano/Mês = (\d{4})/(\d{2}) > Evento = .*? [–-] (.*?)> Selecionar agente"
    
    correspondencias = re.findall(padrao, texto_bruto)
    
    eventos_formatados = []
    
    for ano, mes, descricao in correspondencias:
        tupla_evento = (int(ano), int(mes), descricao.strip())
        eventos_formatados.append(tupla_evento)
        
    return eventos_formatados

texto_entrada = """
Ano/Mês = 2014/03 > Evento = 2014_03 – 13ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2015/03 > Evento = 2015_03 – 20ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2016/03 > Evento = 2016_03 – 17ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2017/03 > Evento = 2017_03 - 16ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2018/03 > Evento = 2018_03 - 11ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2019/03 > Evento = 2019_03 - 06ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2020/03 > Evento = 2020_03 - 06ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2021/03 > Evento = 2021_03 - 08ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2024/03 > Evento = 2024_03 - 04ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2024/04 > Evento = 2024_04 - 04ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2024/05 > Evento = 2024_05 - 04ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2024/06 > Evento = 2024_06 - 04ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2025/03 > Evento = 2025_03 - 02ª REAPURAÇÃO DE DESCONTO> Selecionar agente
Ano/Mês = 2025/11 > Evento = 2025_11 - 01ª REAPURAÇÃO DE DESCONTO> Selecionar agente
"""

lista_final = extrair_lista_eventos(texto_entrada)

print("    EVENTOS = [")
for ano, mes, texto in lista_final:
    print(f'        ({ano}, {mes}, "{texto}"),')
print("    ]")