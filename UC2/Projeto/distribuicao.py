import pandas as pd

def analisar_assimetria_curtose(dados):

    dados_serie = pd.Series(dados)

    assimetria = dados_serie.skew()

    media = dados_serie.mean()
    mediana = dados_serie.median()

    print("\n===== ASSIMETRIA =====")
    print(f"Assimetria das Idades: {assimetria:.4f}")
    print(f"Média: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")

    if assimetria >= -0.5 and assimetria <= 0.5:
        analise_assimetria = "Simétrica ou quase simétrica. Média e mediana são próximas."
    elif assimetria > 0.5:
        analise_assimetria = "Positiva. A cauda se estende para a direita, indicando presença de idades maiores."
    else:
        analise_assimetria = "Negativa. A cauda se estende para a esquerda, indicando presença de idades menores."

    print(f"\nConclusão da Assimetria: {analise_assimetria}")

    print("\n===== CURTOSE =====")

    curtose_excesso = dados_serie.kurtosis()
    curtose_real = curtose_excesso + 3

    print(f"Curtose em Excesso (Pandas): {curtose_excesso:.4f}")
    print(f"Curtose Real (Referência 3.0): {curtose_real:.4f}")

    if curtose_real >= 2.5 and curtose_real <= 3.5:
        analise_curtose = "Mesocúrtica. Distribuição próxima da normal."
    elif curtose_real < 2.5:
        analise_curtose = "Platicúrtica. Dados mais dispersos em relação à média, com curva mais achatada."
    else:
        analise_curtose = "Leptocúrtica. Dados mais concentrados no centro e com caudas mais pesadas."

    print(f"\nConclusão da Curtose: {analise_curtose}")

    return {
        'assimetria': assimetria,
        'curtose_excesso': curtose_excesso,
        'curtose_real': curtose_real,
        'analise_assimetria': analise_assimetria,
        'analise_curtose': analise_curtose
    }