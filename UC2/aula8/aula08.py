#>>>>>>>>>>>>>>> SCRIPT AULA (1) <<<<<<<<<<<<<<<<<<<<

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import mysql.connector

#### CONCEITOS ####
# Conjunto de dados
dados = [2, 4, 6, 8, 10]

# Passo 1: Calcular a média
media = sum(dados) / len(dados)
print(f"Dados: {dados}")
print(f"Média: {media}")

print("-" * 100)
# Passo 2: Calcular as diferenças entre cada valor e a média
diferencas = [x - media for x in dados]
print(f"Diferenças em relação à média: {diferencas}")

# Passo 3: Elevar as diferenças ao quadrado
quadrados_diferencas = [x ** 2 for x in diferencas]
print(f"Quadrados das diferenças: {quadrados_diferencas}")

# Passo 4: Calcular a média dos quadrados das diferenças
variancia = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f"Variância: {variancia:.2f}")

# Passo 5: Calcular a raiz quadrada da variância
desvio_padrao = math.sqrt(variancia)
print(f"Desvio Padrão: {desvio_padrao:.2f}")

print("-" * 100)

dados_serie = pd.Series([2, 4, 6, 8, 10])

print("--- Usando Pandas e NumPy ---")
print(f"\nMédia (usando Pandas .mean()): {dados_serie.mean():.2f}")

# NumPy por padrão usa N no denominador (população)
print(f"Variância (usando NumPy np.var()): {np.var(dados_serie):.2f}")

# Pandas por padrão usa N-1 (amostra), mas podemos forçar o cálculo da população:
# print(f"- Variância (usando Pandas .var(ddof=0)): {dados_serie.var(ddof=0):.2f}")

# NumPy por padrão usa N no denominador (população)
print(f"Desvio Padrão (usando NumPy np.std()): {np.std(dados_serie):.2f}")

# Pandas por padrão usa N-1 (amostra)
print(f"Desvio Padrão (usando Pandas .std(ddof=0)): {dados_serie.std(ddof=0):.2f}")

print("-" * 100)

# Coeficiente de Variação (CV)
cv = (desvio_padrao / media) * 100
print(f"Coeficiente de Variação (CV): {cv:.2f}%")

# Distância da Variância em relação à Média
distancia = variancia / (media ** 2)
print(f"Distância da Variância em relação à Média: {distancia:.2f}")

# Análise de Dispersão
if distancia <= 0.10:
    analise = "Baixa dispersão dos dados em relação à média."
elif distancia < 0.25:
    analise = "Dispersão moderada dos dados em relação à média."
else:
    analise = "Alta dispersão dos dados em relação à média."
    
print(f"Análise de Dispersão: {analise}")

print("-" * 100)

##################################################################

## NA PRÁTICA ###

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="vendas_online"
        )
        cursor = conexao.cursor()
        cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


query_pedidos = "SELECT * FROM Pedidos"
df_pedidos = pd.DataFrame(obter_dados_do_banco(query_pedidos),
                            columns=['id_pedido', 'id_cliente','data_pedido', 'valor_total', 
                                     'id_produto', 'quantidade'])

precos_pedidos_array = df_pedidos['valor_total'].to_numpy()

precos_pedidos_array_final = np.array(precos_pedidos_array).astype(float)

#Cálculo das medidas
media_vendas = precos_pedidos_array_final.mean()
#Usando np.var com ddof=0 para calcular a variância populacional
variancia_vendas = np.var(precos_pedidos_array_final, ddof=0)
#Usando np.std com ddof=0 para calcular o desvio padrão populacional
desvio_padrao_vendas = np.std(precos_pedidos_array_final, ddof=0)

#Coeficiente de Variação (CV)
cv_vendas = (desvio_padrao_vendas / media_vendas) * 100

#Distância da Variância em relação à Média
distancia_vendas = variancia_vendas / (media_vendas ** 2)

print(f"--- Análise dos Valores Totais dos Pedidos ---")
print(f"\nMédia dos Valores Totais: R$ {media_vendas:.2f}")
print(f"Variância dos Valores Totais: {variancia_vendas:.2f}")
print(f"Desvio Padrão dos Valores Totais: R$ {desvio_padrao_vendas:.2f}")
print("-" * 100)
print(f"Coeficiente de Variação (CV): {cv_vendas:.2f}%")
print(f"Distância da Variância / Média²: {distancia_vendas:.2f}")

#Análise de Dispersão
if distancia_vendas <= 0.10:
    analise_vendas = "Baixa dispersão dos dados em relação à média."
elif distancia_vendas < 0.25:
    analise_vendas = "Dispersão moderada dos dados em relação à média."
else:
    analise_vendas = "Alta dispersão dos dados em relação à média."
    print(f"Conclusão da Dispersão: {analise_vendas}")