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
    paciente_idade,
    paciente_enumSexoBiologico,
    paciente_racaCor_valor,
    paciente_endereco_nmMunicipio,
    paciente_endereco_uf,
    vacina_dataAplicacao,
    vacina_categoria_nome,
    vacina_grupoAtendimento_nome,
    vacina_fabricante_nome,
    sistema_origem
FROM vacinacao_ac;
"""

query_ap = """
SELECT
    paciente_idade,
    paciente_enumSexoBiologico,
    paciente_racaCor_valor,
    paciente_endereco_nmMunicipio,
    paciente_endereco_uf,
    vacina_dataAplicacao,
    vacina_categoria_nome,
    vacina_grupoAtendimento_nome,
    vacina_fabricante_nome,
    sistema_origem
FROM vacinacao_ap;
"""

df_ac = obter_dados_do_banco(query_ac)
df_ap = obter_dados_do_banco(query_ap)

df_ac.to_csv("vacinas_ac_powerbi.csv", index=False, encoding="utf-8-sig")
df_ap.to_csv("vacinas_ap_powerbi.csv", index=False, encoding="utf-8-sig")

print("CSV do Acre gerado com sucesso!")
print("CSV do Amapá gerado com sucesso!")

print(df_ac.head())
print(df_ap.head())