import pandas as pd
import mysql.connector

def obter_dados_do_banco(query):
    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="projeto_vacinas1"
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
    paciente_endereco_nmMunicipio,
    paciente_endereco_uf,
    COUNT(*) AS total_vacinacoes,
    ROUND(AVG(CAST(paciente_idade AS UNSIGNED)), 2) AS media_idade
FROM vacinacao_ac
WHERE paciente_idade IS NOT NULL
  AND paciente_endereco_nmMunicipio IS NOT NULL
  AND paciente_endereco_uf IS NOT NULL
GROUP BY paciente_endereco_nmMunicipio, paciente_endereco_uf;
"""

query_ap = """
SELECT
    paciente_endereco_nmMunicipio,
    paciente_endereco_uf,
    COUNT(*) AS total_vacinacoes,
    ROUND(AVG(CAST(paciente_idade AS UNSIGNED)), 2) AS media_idade
FROM vacinacao_ap
WHERE paciente_idade IS NOT NULL
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

print(df_ac.head())
print(df_ap.head())