import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_histograma(dados):

    media = np.mean(dados)
    mediana = np.median(dados)
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)

    plt.figure(figsize=(12, 6))

    sns.histplot(dados, kde=True)

    plt.axvline(media, linestyle='-', label=f'Média: {media:.2f}')
    plt.axvline(mediana, linestyle='-', label=f'Mediana: {mediana:.2f}')
    plt.axvline(q1, linestyle='--', label=f'Q1: {q1:.2f}')
    plt.axvline(q3, linestyle='--', label=f'Q3: {q3:.2f}')

    plt.title('Distribuição das Idades dos Pacientes')
    plt.xlabel('Idade')
    plt.ylabel('Quantidade')
    plt.legend()
    plt.grid(True)

    plt.show()


def gerar_painel_boxplot(dados_array_final, medidas, titulo_boxplot='Boxplot das Idades dos Pacientes', caminho_salvar=None):

    if medidas is None:
        print("Erro: Medidas estatísticas não fornecidas ou inválidas.")
        return

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    sns.boxplot(y=dados_array_final, ax=axes[0])
    axes[0].set_title(titulo_boxplot)
    axes[0].set_ylabel('Idade')

    axes[1].axis('off')
    axes[1].set_title('Medidas Estatísticas Calculadas')

    resumo = (
        f"Medidas de Tendência Central:\n"
        f"  Média: {medidas['media']:.2f} anos\n"
        f"  Mediana (Q2): {medidas['mediana']:.2f} anos\n"
        f"  Moda: {medidas['moda']:.2f} anos\n"
        f"\n"
        f"Medidas de Posição/Dispersão:\n"
        f"  Q1: {medidas['q1']:.2f} anos\n"
        f"  Q3: {medidas['q3']:.2f} anos\n"
        f"  IQR: {medidas['iqr']:.2f}\n"
        f"  Desvio Padrão: {medidas['desvio_padrao']:.2f}\n"
    )

    axes[1].text(
        0.1,
        0.95,
        resumo,
        transform=axes[1].transAxes,
        fontsize=12,
        verticalalignment='top',
        bbox=dict(boxstyle="round,pad=0.5", alpha=0.1, color='lightgray')
    )

    plt.tight_layout()

    if caminho_salvar:
        plt.savefig(caminho_salvar)
        print(f"Painel salvo em: {caminho_salvar}")

    plt.show()