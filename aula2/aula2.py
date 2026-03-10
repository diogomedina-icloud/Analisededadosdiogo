nome = "João"
idade = 25
print(nome, idade)

a = 10
b = 5
print(f"Soma: {a + b}\n")
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)

primeiro_nome = "Maria"
sobrenome = "Silva"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)

print("o tipo armazenado \n"
f"na variavel 'primeiro  nome' ")



x = 21
y = 21.0
print("x é maior que y?", x > y)
print("x é igual a y?", x == y)

tem_carteira = False
idade = 18
tem_carro = False
bebe=False
pode_dirigir = (idade >= 18 and tem_carteira) and bebe== False
print("Pode dirigir?", pode_dirigir)
print("Pode dirigir e tem carro?", pode_dirigir or tem_carro)

frase = "Python é divertido"
print(frase.upper())
nova_frase = frase.replace("divertido", "inteligente")
print(nova_frase)

contador = 0
contador += 5
contador=contador+5  # contador=contador+5 <<<<<< incremento
contador -= 2 # contador=contador-2 <<<<<<<<<<<<<< decremento
contador *= 3 # contador=contador*3
print("Valor final do contador:", contador)


a = int(input("digite uma nota:"))
b = 20
c = 30
media = (a + b + c) / 3
print("Média:", media)
print("A média é maior que 15 e menor que 25?", 15 < media < 25)

nota = int(input("Nota:"))
print(nota)
