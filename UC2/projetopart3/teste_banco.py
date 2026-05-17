import pandas as pd
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="projeto_vacinas"
        )

        df = pd.read_sql(query, conexao)
        return df

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()


query_vacina_ac = """
SELECT
    paciente_endereco_nmMunicipio AS municipio,
    paciente_endereco_uf AS uf,
    vacina_fabricante_nome AS vacina_fabricante,
    COUNT(*) AS total_por_vacina
FROM vacinacao_ac
WHERE paciente_endereco_nmMunicipio IS NOT NULL
  AND paciente_endereco_uf IS NOT NULL
  AND vacina_fabricante_nome IS NOT NULL
GROUP BY
    paciente_endereco_nmMunicipio,
    paciente_endereco_uf,
    vacina_fabricante_nome;
"""

df_vacinas_ac = obter_dados_do_banco(query_vacina_ac)

df_vacinas_ac = df_vacinas_ac.sort_values(
    by=["municipio", "uf", "total_por_vacina"],
    ascending=[True, True, False]
)

df_vacina_mais_usada_ac = df_vacinas_ac.drop_duplicates(
    subset=["municipio", "uf"],
    keep="first"
)

df_vacina_mais_usada_ac["estado"] = "AC"
df_vacina_mais_usada_ac["regiao"] = "Norte"

df_vacina_mais_usada_ac.to_csv(
    "vacina_mais_usada_ac_powerbi.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV da vacina mais usada do Acre gerado com sucesso!")

print(df_vacina_mais_usada_ac.head())
print(df_vacina_mais_usada_ac.shape)