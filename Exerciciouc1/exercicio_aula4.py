# <<<<<<<<<<<<<<<<<<EXERCICIO 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
# 3m² existe um bocal para uma lâmpada.

# potencia_lampada = 20
# largura = 2
# comprimento = 5

# area = largura * comprimento
# potencia_necessaria = area * 3
# lampadas = potencia_necessaria / potencia_lampada

# if lampadas <= 1:
#     print("Será necessária 1 lâmpada")
# elif lampadas <= 2:
#     print("Serão necessárias 2 lâmpadas")
# elif lampadas <= 3:
#     print("Serão necessárias 3 lâmpadas")
# else:
#     print("Serão necessárias mais de 3 lâmpadas")

            # EXERCICIO 2 >>>>>>>>>>>>>>

# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
# todas as suas paredes (considere que não será descontada a área ocupada por portas e 
# janelas). Cada caixa de azulejos possui 1,5 m² 


# comprimento = float(input("Digite o comprimento da cozinha: "))
# largura = float(input("Digite a largura da cozinha: "))
# altura = float(input("Digite a altura da cozinha: "))

# area_paredes = 2 * (comprimento * altura) + 2 * (largura * altura)
# caixas = area_paredes / 1.5

# if caixas <= 1:
#     print("Será necessária 1 caixa de azulejo")
# elif caixas <= 5:
#     print("Serão necessárias", round(caixas), "caixas de azulejo")
# elif caixas <= 10:
#     print("Serão necessárias", round(caixas), "caixas de azulejo")
# else:
#     print("Serão necessárias", round(caixas), "caixas de azulejo")

# print("Área total das paredes:", area_paredes, "m²") 

  # EXERCICIO 3  
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o 
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do 
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de 
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a 
# média do consumo em km/L e o lucro (líquido) do dia.



    
    # Exercicio 4>>>>>>>>>>>>>>>

# Escreva um programa que leia o código de origem de um produto e imprima na tela a região 
# de sua procedência, conforme a tabela abaixo: 

# nomes_regiao=int(input("digite um codigo de 1 a 11: "))

# match nomes_regiao:
#     case 1:
#         print("Sul")
#     case 2:
#         print("Norte")
#     case 3:
#         print("Leste")
#     case 4:
#         print("Oeste")
#     case 5 | 6:
#         print("Nordeste")
#     case 7|8|9:
#         print("Sudeste")
#     case 10:
#         print("centro-oeste")
#     case 11:
#         print("Noroeste")
#     case _:
#         print("Importado")

   #Exercicio 5 >>>>>>>>>>>>

#    Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação 
# optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve 
# ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa 
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e 
# mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em 
# recuperação, de acordo com as informações abaixo: 

# try:

#     nota1 = float(input("Digite a nota da primeira avaliação: "))
#     nota2 = float(input("Digite a nota da segunda avaliação: "))
#     optativa = float(input("Digite a nota da prova optativa (-1 se não fez): "))

#     if optativa != -1:
#         if nota1 < nota2:
#             nota1 = optativa
#     else:
#         nota2 = optativa


#     media = (nota1 + nota2) / 2
#     print("Média do semestre:", round(media, 2))

#     if media >= 6:
#         print("Aluno aprovado")
#     elif media >= 3:
#         print("Aluno em recuperação")
#     else:
#         print("Aluno reprovado")

# except ValueError:
#     print("Erro de digitação. Digite apenas números.")



    # Exercicio 6 >>>>>>>>>
# Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o 
# valor zero como positivo.

# valor_numero=int(input(" Digite o valor:"))

# if  valor_numero >= 0:
#     print("Positivo")
# else:
#     print("valor negativo")

                                #   ou

try:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Positivo")
    else:
        print("Negativo")

except ValueError:
    print("Digite apenas números.")
