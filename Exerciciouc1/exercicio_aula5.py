#   Exercicio 1>>>>>
# Use o laço for para repetir a lógica de cálculo de média e status
# (Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

# for i in range(1, 11):

#     try:
#         print("\nEstudante", i)

#         nota1 = float(input("Digite a nota da primeira avaliação: "))
#         nota2 = float(input("Digite a nota da segunda avaliação: "))
#         optativa = float(input("Digite a nota da optativa (-1 se não fez): "))

        
#         if optativa != -1:
#             if nota1 < nota2:
#                 nota1 = optativa
#             else:
#                 nota2 = optativa

#         media = (nota1 + nota2) / 2

#         print("Média:", round(media, 2))

#         if media >= 6:
#             print("Status: Aprovado")
#         elif media >= 3:
#             print("Status: Recuperação")
#         else:
#             print("Status: Reprovado")

#     except ValueError:
#         print("Erro de digitação. Digite apenas números.")

# EXERCICIO 2 

# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.
# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.

# ano_atual = 2026
# for i in range(1, 13):
#     try:
#         print("\nCandidato", i)

#         ano_nascimento = int(input("Digite o ano de nascimento: "))
#         idade = ano_atual - ano_nascimento

#         if idade < 18:
#             print("Candidato menor de 18 anos. Não pode participar.")
           
#         telefone = input("Digite o telefone: ")
#         email = input("Digite o email: ")

#         print("Cadastro realizado com sucesso!")
#         print("Idade:", idade)

#     except ValueError:
#         print("Erro de digitação. Digite valores válidos.")

#    EXERCICIO 3>>>>>>>>>>>>>>>>>>

# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio


# usuario_correto = "diogo"
# senha_correta= "8757"

# tentativas= 3

# for i in range (tentativas):
#     usuario=input("digite o usuario:")
#     senha=input("digite a senha:")

#     if usuario == usuario_correto and senha == senha_correta:
#         print("login realizado com sucesso")
#         break
#     else:
#         tentativas_restante = tentativas - (i +1)
#         print("usuario ou senha errados!")
    
#     if tentativas_restante > 0:
#         print("Tentativas restantes:", tentativas_restante)
#     else:
#             print("Conta bloqueada.")

    

    


