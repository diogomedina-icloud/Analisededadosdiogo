import numpy as np
import pandas as pd
from scipy import stats

def calcular_medidas_descritivas(dados):

    media = np.mean(dados)
    mediana = np.median(dados)
    moda = stats.mode(dados, keepdims=True)
    desvio_padrao = np.std(dados)

    q1 = np.percentile(dados, 25)
    q2 = np.percentile(dados, 50)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1

    distancia_media_mediana = (media - mediana) / mediana

    print("\n===== MEDIDAS DESCRITIVAS =====")

    print(f"Média: {media:.2f}")

    print(f"Mediana: {mediana:.2f}")

    print(f"Moda: {moda.mode[0]:.2f}")

    print(f"Desvio Padrão: {desvio_padrao:.2f}")

    print(f"Q1: {q1:.2f}")

    print(f"Q2 (Mediana): {q2:.2f}")

    print(f"Q3: {q3:.2f}")

    print(f"IQR: {iqr:.2f}")

    print(f"Distância entre Média e Mediana: {distancia_media_mediana * 100:.2f}%")

    if abs(distancia_media_mediana) <= 0.10:
        print("A média tende a ser uma medida confiável.")
    elif abs(distancia_media_mediana) < 0.25:
        print("A média pode sofrer influência moderada de valores extremos.")
    else:
        print("A média tende a não ser confiável.")

    return {
        'media': media,
        'mediana': mediana,
        'moda': moda.mode[0],
        'desvio_padrao': desvio_padrao,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'iqr': iqr,
        'distancia_media_mediana': distancia_media_mediana
    }

def calcular_outliers(dados):

    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    iqr = q3 - q1

    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    outliers_inferiores = dados[dados < limite_inferior]
    outliers_superiores = dados[dados > limite_superior]

    print("\n===== OUTLIERS =====")
    print(f"Q1: {q1:.2f}")
    print(f"Q3: {q3:.2f}")
    print(f"IQR: {iqr:.2f}")
    print(f"Limite Inferior: {limite_inferior:.2f}")
    print(f"Limite Superior: {limite_superior:.2f}")
    print(f"\nQuantidade de outliers inferiores: {len(outliers_inferiores)}")
    print(f"Quantidade de outliers superiores: {len(outliers_superiores)}")

    return {
        'q1': q1,
        'q3': q3,
        'iqr': iqr,
        'limite_inferior': limite_inferior,
        'limite_superior': limite_superior,
        'outliers_inferiores': outliers_inferiores,
        'outliers_superiores': outliers_superiores
    }