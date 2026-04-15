import random
# import os
# import shutil
# import datetime

# # --- Cálculo dinâmico do mês anterior ---
# hoje = datetime.date.today()
# ano = hoje.year
# mes = hoje.month - 1 if hoje.month > 1 else 12
# ano_ref = ano if hoje.month > 1 else ano - 1

# # Mapas para abreviações
# nomes_meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# mes_abrev = nomes_meses[mes - 1]
# mes_formatado = f"{ano_ref}{mes:02d}"  # ex: 202509

# print(f"Mes selelcionado: {mes_formatado}")
def calcular_imc():
    print("Calculadora de IMC")
    print("Digite seu peso em kg:")
    peso = float(input())
    print("Digite sua altura em metros:")
    altura = float(input())
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidade")

def advinhacao():

    print("Jogo de Adivinhação")
    
    numero_secreto = random.randint(1, 100)
    
    tentativas = 0
    
    while True:
        print("Digite um número entre 1 e 100:")
        palpite = int(input())
        tentativas += 1
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

def temperatura():
    print("Conversor de Temperatura")
    print("Digite a temperatura em Celsius:")
    celsius = float(input())
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")

def analisar_senhas():
    print("Analisador de Senhas")
    print("Digite uma senha para análise:")
    senha = input()
    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
    elif not any(c.isupper() for c in senha):
        print("Senha fraca: deve conter pelo menos uma letra maiúscula.")
    elif not any(c.islower() for c in senha):
        print("Senha fraca: deve conter pelo menos uma letra minúscula.")
    elif not any(c.isdigit() for c in senha):
        print("Senha fraca: deve conter pelo menos um número.")
    else:
        print("Senha forte.")

def tarefas():
    print("Gerenciador de Tarefas")
    tarefas = []
    while True:
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Sair")
        escolha = input("Digite sua escolha: ")
        if escolha == "1":
            print("Digite a descrição da tarefa:")
            tarefa = input()
            tarefas.append(tarefa)
            print("Tarefa adicionada.")
        elif escolha == "2":
            print("Tarefas:")
            for i, tarefa in enumerate(tarefas, 1):
                print(f"{i}. {tarefa}")
        elif escolha == "3":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")

def gerador_cpf_cnpj():
    print("Gerador de CPF e CNPJ")
    print("Digite 'cpf' para gerar um CPF ou 'cnpj' para gerar um CNPJ:")
    escolha = input().lower()
    if escolha == "cpf":
        cpf = [str(random.randint(0, 9)) for _ in range(9)]
        cpf.append(str((sum(int(cpf[i]) * (10 - i) for i in range(9)) * 10 % 11) % 10))
        cpf.append(str((sum(int(cpf[i]) * (11 - i) for i in range(10)) * 10 % 11) % 10))
        print(f"CPF gerado: {''.join(cpf)}")
    elif escolha == "cnpj":
        cnpj = [str(random.randint(0, 9)) for _ in range(12)]
        cnpj.append(str((sum(int(cnpj[i]) * (5 - i if i < 4 else 13 - i) for i in range(12)) * 10 % 11) % 10))
        cnpj.append(str((sum(int(cnpj[i]) * (6 - i if i < 5 else 14 - i) for i in range(13)) * 10 % 11) % 10))
        print(f"CNPJ gerado: {''.join(cnpj)}")

def main():
    print("Opa! O programa iniciou.")
    print("Escolha uma opção:")
    print("1 - Calcular IMC")
    print("2 - Jogo de Adivinhação")
    print("3 - Conversor de Temperatura")
    print("4 - Analisador de Senhas")
    print("5 - Gerenciador de Tarefas")
    print("6 - Gerador de CPF e CNPJ")
    
    escolha = input("Digite sua escolha (1 a 6): ")
    
    if escolha == "1":
        calcular_imc()
    elif escolha == "2":
        advinhacao()
    elif escolha == "3":
        temperatura()
    elif escolha == "4":
        analisar_senhas()
    elif escolha == "5":
        tarefas()
    elif escolha == "6":
        gerador_cpf_cnpj()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()