CREATE DATABASE projeto_vacinas;
USE projeto_vacinas;


CREATE TABLE vacinacao_ac (
    document_id VARCHAR(150),
    paciente_id VARCHAR(150),
    paciente_idade VARCHAR(50),
    paciente_datanascimento VARCHAR(50),
    paciente_enumsexobiologico VARCHAR(50),
    paciente_racacor_codigo VARCHAR(50),
    paciente_racacor_valor VARCHAR(100),
    paciente_endereco_coibgemunicipio VARCHAR(50),
    paciente_endereco_copais VARCHAR(50),
    paciente_endereco_nmmunicipio VARCHAR(100),
    paciente_endereco_nmpais VARCHAR(100),
    paciente_endereco_uf VARCHAR(50),
    paciente_endereco_cep VARCHAR(50),
    paciente_nacionalidade_enumnacionalidade VARCHAR(100),
    estabelecimento_valor VARCHAR(50),
    estabelecimento_razaosocial VARCHAR(255),
    estalecimento_nofantasia VARCHAR(255),
    estabelecimento_municipio_codigo VARCHAR(50),
    estabelecimento_municipio_nome VARCHAR(100),
    estabelecimento_uf VARCHAR(10),
    vacina_grupoatendimento_codigo VARCHAR(50),
    vacina_grupoatendimento_nome VARCHAR(255),
    vacina_categoria_codigo VARCHAR(50),
    vacina_categoria_nome VARCHAR(255),
    vacina_lote VARCHAR(100),
    vacina_fabricante_nome VARCHAR(150),
    vacina_fabricante_referencia VARCHAR(150),
    vacina_dataaplicacao VARCHAR(50),
    vacina_descricao_dose VARCHAR(100),
    vacina_codigo VARCHAR(50),
    vacina_nome VARCHAR(255),
    sistema_origem VARCHAR(100),
    is_duplicado VARCHAR(10)
);
TRUNCATE TABLE vacinacao_ac;

CREATE TABLE vacinacao_ap (
    document_id VARCHAR(150),
    paciente_id VARCHAR(150),
    paciente_idade VARCHAR(50),
    paciente_datanascimento VARCHAR(50),
    paciente_enumsexobiologico VARCHAR(50),
    paciente_racacor_codigo VARCHAR(50),
    paciente_racacor_valor VARCHAR(100),
    paciente_endereco_coibgemunicipio VARCHAR(50),
    paciente_endereco_copais VARCHAR(50),
    paciente_endereco_nmmunicipio VARCHAR(100),
    paciente_endereco_nmpais VARCHAR(100),
    paciente_endereco_uf VARCHAR(50),
    paciente_endereco_cep VARCHAR(50),
    paciente_nacionalidade_enumnacionalidade VARCHAR(100),
    estabelecimento_valor VARCHAR(50),
    estabelecimento_razaosocial VARCHAR(255),
    estalecimento_nofantasia VARCHAR(255),
    estabelecimento_municipio_codigo VARCHAR(50),
    estabelecimento_municipio_nome VARCHAR(100),
    estabelecimento_uf VARCHAR(10),
    vacina_grupoatendimento_codigo VARCHAR(50),
    vacina_grupoatendimento_nome VARCHAR(255),
    vacina_categoria_codigo VARCHAR(50),
    vacina_categoria_nome VARCHAR(255),
    vacina_lote VARCHAR(100),
    vacina_fabricante_nome VARCHAR(150),
    vacina_fabricante_referencia VARCHAR(150),
    vacina_dataaplicacao VARCHAR(50),
    vacina_descricao_dose VARCHAR(100),
    vacina_codigo VARCHAR(50),
    vacina_nome VARCHAR(255),
    sistema_origem VARCHAR(100),
    is_duplicado VARCHAR(10)
);

 -- 1 Distribuição de vacinação por sexo entre Acre e Amapá

SELECT 
    'AC' AS estado,
    paciente_enumsexobiologico AS sexo,
    COUNT(*) AS quantidade
FROM vacinacao_ac
GROUP BY paciente_enumsexobiologico

UNION ALL

SELECT 
    'AP' AS estado,
    paciente_enumsexobiologico AS sexo,
    COUNT(*) AS quantidade
FROM vacinacao_ap
GROUP BY paciente_enumsexobiologico

ORDER BY estado, quantidade DESC;

-- 2 Fabricantes de vacinas mais utilizadas entre Acre e Amapá

SELECT 
    'AC' AS estado,
    vacina_fabricante_nome AS fabricante,
    COUNT(*) AS quantidade
FROM vacinacao_ac
GROUP BY vacina_fabricante_nome

UNION ALL

SELECT 
    'AP' AS estado,
    vacina_fabricante_nome AS fabricante,
    COUNT(*) AS quantidade
FROM vacinacao_ap
GROUP BY vacina_fabricante_nome

ORDER BY estado, quantidade DESC;

-- 3 Comparação AC x AP comparação de total de registos de vacinas

SELECT 'AC' AS estado, COUNT(*) AS total_registros
FROM vacinacao_ac
UNION ALL
SELECT 'AP' AS estado, COUNT(*) AS total_registros
FROM vacinacao_ap;

-- 4 Comparação AC x AP média de idade de aplicação

SELECT 'AC' AS estado, ROUND(AVG(CAST(paciente_idade AS UNSIGNED)), 2) AS media_idade
FROM vacinacao_ac
UNION ALL
SELECT 'AP' AS estado, ROUND(AVG(CAST(paciente_idade AS UNSIGNED)), 2) AS media_idade
FROM vacinacao_ap;

-- 5 Comparação AC x AP de sexo com porcentagem

SELECT 
    estado,
    paciente_enumsexobiologico AS sexo,
    COUNT(*) AS quantidade,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY estado), 
        2
    ) AS porcentagem
FROM (
    SELECT 'AC' AS estado, paciente_enumsexobiologico
    FROM vacinacao_ac
    UNION ALL
    SELECT 'AP' AS estado, paciente_enumsexobiologico
    FROM vacinacao_ap
) AS dados
GROUP BY estado, paciente_enumsexobiologico
ORDER BY estado, quantidade DESC;



SELECT DISTINCT paciente_idade
FROM vacinacao_ap
WHERE paciente_idade IS NOT NULL
ORDER BY CAST(paciente_idade AS UNSIGNED) ASC
LIMIT 20;
