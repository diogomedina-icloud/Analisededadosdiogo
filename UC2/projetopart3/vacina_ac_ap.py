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


query_ac = """
SELECT
    paciente_endereco_nmMunicipio AS municipio,
    paciente_endereco_uf AS uf,
    COUNT(*) AS total_vacinacoes,
    ROUND(AVG(paciente_idade), 2) AS media_idade
FROM vacinacao_ac
WHERE paciente_idade IS NOT NULL
  AND paciente_idade >= 0
  AND paciente_idade <= 120
  AND paciente_endereco_nmMunicipio IS NOT NULL
  AND paciente_endereco_uf IS NOT NULL
GROUP BY paciente_endereco_nmMunicipio, paciente_endereco_uf;
"""

query_ap = """
SELECT
    paciente_endereco_nmMunicipio AS municipio,
    paciente_endereco_uf AS uf,
    COUNT(*) AS total_vacinacoes,
    ROUND(AVG(paciente_idade), 2) AS media_idade
FROM vacinacao_ap
WHERE paciente_idade IS NOT NULL
  AND paciente_idade >= 0
  AND paciente_idade <= 120
  AND paciente_endereco_nmMunicipio IS NOT NULL
  AND paciente_endereco_uf IS NOT NULL
GROUP BY paciente_endereco_nmMunicipio, paciente_endereco_uf;
"""

df_ac = obter_dados_do_banco(query_ac)
df_ap = obter_dados_do_banco(query_ap)

df_ac["estado"] = "AC"
df_ac["regiao"] = "Norte"

df_ap["estado"] = "AP"
df_ap["regiao"] = "Norte"

df_ac.to_csv("vacinas_ac_powerbi.csv", index=False, encoding="utf-8-sig")
df_ap.to_csv("vacinas_ap_powerbi.csv", index=False, encoding="utf-8-sig")

print("CSV do Acre gerado com sucesso!")
print("CSV do Amapá gerado com sucesso!")

print("\nAcre:")
print(df_ac.head())
print(df_ac["media_idade"].describe())

print("\nAmapá:")
print(df_ap.head())
print(df_ap["media_idade"].describe())