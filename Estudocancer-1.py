# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 18:18:23 2026

@author: User
"""

#%% Instalando os pacotes

## Executar na linha de comando do console (sem o #)

 # pip install pandas
 # pip install numpy
 # pip install factor_analyzer
 # pip install sympy
 # pip install scipy
 # pip install matplotlib
 # pip install seaborn
 # pip install plotly
 # pip install pingouin
 # pip install pyshp
 # pip install re

#%% Importando os pacotes necessários

import pandas as pd
import numpy as np
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import plotly.graph_objects as go
import shapefile as shp
import warnings
import re
warnings.filterwarnings("ignore")


#%% Importando o banco de dados

cancerriograndesul = pd.DataFrame()
cancerriograndesul= pd.read_csv("base_nao_identificada_4535.csv", sep=";", encoding= 'latin1')
cancerriograndesul= cancerriograndesul.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

 

canceracre = pd.DataFrame()
canceracre= pd.read_csv("base_nao_identificada_5436.csv", sep=";", encoding= 'latin1')
canceracre= canceracre.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância'],axis=1)
                     
cancerangrarj = pd.DataFrame()
cancerangrarj= pd.read_csv("base_nao_identificada_5437.csv", sep=";", encoding= 'latin1')
cancerangrarj= cancerangrarj.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancerpara = pd.DataFrame()
cancerpara= pd.read_csv("base_nao_identificada_5438.csv", sep=";", encoding= 'latin1')
cancerpara= cancerpara.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancerminasgerais = pd.DataFrame()
cancerminasgerais= pd.read_csv("base_nao_identificada_5439.csv", sep=";", encoding= 'latin1')
cancerminasgerais= cancerminasgerais.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento','TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)
                     
cancercampinassp = pd.DataFrame()
cancercampinassp= pd.read_csv("base_nao_identificada_5440.csv", sep=";", encoding= 'latin1')
cancercampinassp= cancercampinassp.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)   
                     
cancermatogrosso = pd.DataFrame()
cancermatogrosso= pd.read_csv("base_nao_identificada_5441.csv", sep=";", encoding= 'latin1')
cancermatogrosso= cancermatogrosso.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancerbarretossp = pd.DataFrame()
cancerbarretossp= pd.read_csv("base_nao_identificada_5444.csv", sep=";", encoding= 'latin1')
cancerbarretossp= cancerbarretossp.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancerparaiba = pd.DataFrame()
cancerparaiba= pd.read_csv("base_nao_identificada_5445.csv", sep=";", encoding= 'latin1')
cancerparaiba= cancerparaiba.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

canceramazonas = pd.DataFrame()
canceramazonas= pd.read_csv("base_nao_identificada_5446.csv", sep=";", encoding= 'latin1')
canceramazonas= canceramazonas.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancertocantins = pd.DataFrame()
cancertocantins= pd.read_csv("base_nao_identificada_5448.csv", sep=";", encoding= 'latin1')
cancertocantins= cancertocantins.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)

cancerpocosdecaldasmg = pd.DataFrame()
cancerpocosdecaldasmg= pd.read_csv("base_nao_identificada_5449.csv", sep=";", encoding= 'latin1')
cancerpocosdecaldasmg= cancerpocosdecaldasmg.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)
                     
cancerpernambuco = pd.DataFrame()
cancerpernambuco= pd.read_csv("base_nao_identificada_5450.csv", sep=";", encoding= 'latin1')
cancerpernambuco= cancerpernambuco.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)
                     
cancerroraima = pd.DataFrame()
cancerroraima= pd.read_csv("base_nao_identificada_5451.csv", sep=";", encoding= 'latin1')
cancerroraima= cancerroraima.drop(['Código do Paciente', 'Data de Nascimento', 'Código Profissão', 'Naturalidade', 'Código da Topografia', 'Código da Morfologia', 'Código da Doenca', 'Código da Doenca Infantil', 'Código da Doenca Adulto Jovem', 'Extensão', 'Lateralidade', 'Estadiamento', 'TNM', 'Status Vital', 'Metástase à distância', 'Unnamed: 37'],axis=1)                 
                     
#%% concatenar bases
framessp= [cancerbarretossp, cancercampinassp]
cancersp=pd.concat(framessp)

framesmg= [cancerminasgerais, cancerpocosdecaldasmg]
cancermg= pd.concat(framesmg)

frames= [canceracre, canceramazonas, cancerangrarj, cancersp, cancermatogrosso, cancermg, cancerpara, cancerparaiba, cancerpernambuco, cancerriograndesul, cancerroraima, cancertocantins]
cancerbrasil= pd.concat(frames)
cancerbrasil= cancerbrasil.dropna(subset=['Idade'])
cancerbrasil['Idade']=cancerbrasil['Idade'].astype('int')

#%% Informações gerais sobre o DataFrame

print(cancerbrasil.info())
cancerbrasil.head(n=5)

#%% Renomear observações para objetos de estudo


cancerbrasil= cancerbrasil.rename(columns= {'Nome do RCBP':'rcbp',
                                            'Sexo':'sexo',
                                            'Idade':'idade',
                                            'Raca/Cor':'raca/cor',
                                            'Nacionalidade':'pais',
                                            'Naturalidade Estado': 'estado',
                                            'Naturalidade':'naturalidade',
                                            'Grau de Instrução':'instrucao', 
                                            'Estado Civil':'estadocivil',
                                            'Nome Profissão':'profissao',
                                            'Estado Endereço':'estadoendereco',
                                            'Cidade Endereço':'cidadeendereco',
                                            'Descrição da Topografia':'topografia',
                                            'Descrição da Morfologia':'morfologia',
                                            'Descrição da Doenca':'doenca',
                                            'Descrição da Doenca Infantil':'doencainfantil',
                                            'Descrição da Doenca Adulto Jovem':'doencaadultojovem',
                                            'Indicador de Caso Raro':'indicadordecasoraro',
                                            'Meio de Diagnostico':'meiodiagnostico',
                                            'Tipo do Obito':'tipodeobito',
                                            'Data do Óbito':'datadoobito',
                                            'Data de Último Contato':'ultimocontato',
                                            'Data de Diagnostico':'datadiagnostico',
                                                                                    })
                        
cancerbrasil.info()

#%% Substituindo palavras na coluna 'topografia'

replacements={
        'PELE DO LABIO, SOE':'PELE, SOE',
        'LESAO SOBREPOSTA DO LABIO':'BOCA, SOE'
        }
cancerbrasil['topografia']=cancerbrasil['topografia'].replace(replacements)

print("Valores na coluna 'topografia' após a sbstituição:")
print(cancerbrasil['topografia'])

#%% Salvando arquivo unificado



#cancerbrasilunificado= cancerbrasil.to_csv("cancerbrasilunificado.csv", sep=";", encoding= 'latin1')

#%% Selecionando casos de interesse

#cancerinfantil= cancerbrasil.dropna(['doencainfantil']).copy()

cancer_pele_nao_melanoma= cancerbrasil[cancerbrasil['topografia'].str.contains('Pele', case=False, na=False)]
cancer_pele_nao_melanoma= cancer_pele_nao_melanoma[~cancer_pele_nao_melanoma['doenca'].str.contains('melanoma', case=False, na=False)]
print("Rows where Name contains 'Pele':")
display(cancer_pele_nao_melanoma)

cancer_colo_do_utero= cancerbrasil[cancerbrasil['topografia'].str.contains('Colo do Utero', case=False, na=False)]
print("Rows where Name contains 'Colo do utero':")
display(cancer_colo_do_utero)

cancer_estomago= cancerbrasil[cancerbrasil['topografia'].str.contains('Estomago', case=False, na=False)]
print("Rows where Name contains 'Estomago':")
display(cancer_estomago)

cancer_prostata= cancerbrasil[cancerbrasil['topografia'].str.contains('Prostata', case=False, na=False)]
print("Rows where Name contains 'Prostata':")
display(cancer_prostata)

cancer_tireoide= cancerbrasil[cancerbrasil['topografia'].str.contains('Tireoide', case=False, na=False)]
print("Rows where Name contains 'Tireoide':")
display(cancer_tireoide)

cancer_mama= cancerbrasil[cancerbrasil['topografia'].str.contains('Mam', case=False, na=False)]
print("Rows where Name contains 'Mam':")
display(cancer_mama)


search_words= ['TRAQUEIA', 'BRONQUIO', 'PULMAO']
regex_pattern= '|'.join(map(re.escape,search_words))
cancer_pulmao= cancerbrasil[cancerbrasil['topografia'].str.contains(regex_pattern, case= False, na=False)]
print(f"Rows where Name contains {search_words}:")
display(cancer_pulmao)

search_words= ['BOCA', 'LINGUA', 'LABIO', 'PALATO', 'CAVIDADE ORAL']
regex_pattern= '|'.join(map(re.escape,search_words))
cancer_boca= cancerbrasil[cancerbrasil['topografia'].str.contains(regex_pattern, case= False, na=False)]
print(f"Rows where Name contains {search_words}:")
display(cancer_boca)

search_words= ['COLON', 'RETO']
regex_pattern= '|'.join(map(re.escape,search_words))
cancer_colon_reto= cancerbrasil[cancerbrasil['topografia'].str.contains(regex_pattern, case= False, na=False)]
print(f"Rows where Name contains {search_words}:")
display(cancer_colon_reto)

#%% Tabelas descritivas

cancer_pele_nao_melanoma['topografia'].value_counts()

tab_idade=pd.crosstab(cancer_pele_nao_melanoma['idade'], cancer_pele_nao_melanoma['topografia'])
tab_sexo=pd.crosstab(cancer_pele_nao_melanoma['sexo'], cancer_pele_nao_melanoma['topografia']).T
tab_instrucao=pd.crosstab(cancer_pele_nao_melanoma['instrucao'], cancer_pele_nao_melanoma['topografia'])
tab_estado_civil=pd.crosstab(cancer_pele_nao_melanoma['estadocivil'], cancer_pele_nao_melanoma['topografia'])

cancer_pulmao['topografia'].value_counts()

tab_idade1=pd.crosstab(cancer_pulmao['idade'], cancer_pulmao['topografia'])
tab_sexo1=pd.crosstab(cancer_pulmao['sexo'], cancer_pulmao['topografia']).T
tab_instrucao1=pd.crosstab(cancer_pulmao['instrucao'], cancer_pulmao['topografia'])
tab_estado_civil1=pd.crosstab(cancer_pulmao['estadocivil'], cancer_pulmao['topografia'])

cancerbrasil['doencainfantil'].value_counts()

tab_idade2=pd.crosstab(cancerbrasil['idade'], cancerbrasil['doencainfantil'])
tab_sexo2=pd.crosstab(cancerbrasil['sexo'], cancerbrasil['doencainfantil']).T

cancerbrasil['doencaadultojovem'].value_counts()

tab_idade3=pd.crosstab(cancerbrasil['idade'], cancerbrasil['doencaadultojovem'])
tab_sexo3=pd.crosstab(cancerbrasil['sexo'], cancerbrasil['doencaadultojovem']).T


#%% 

"""
EXTENSÃO DO ESTUDO — Machine Learning (Não Supervisionado e Supervisionado)
Objetivo: investigar a relação entre o TIPO DE CÂNCER (variável-alvo) e
          SEXO, IDADE, PROFISSÃO e REGIÃO (variáveis explicativas).

"""

#%% Instalando os pacotes adicionais

#pip install scikit-learn
#pip install scipy
#pip install prince        # Análise de Correspondência Múltipla (MCA)

#%% Importando os pacotes adicionais

from scipy.stats import chi2_contingency, f_oneway
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.cluster import KMeans
from sklearn.metrics import (silhouette_score, accuracy_score,
                              classification_report, confusion_matrix)
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import CategoricalNB
from scipy.cluster.hierarchy import dendrogram, linkage
import prince


#%% 1. PREPARAÇÃO DA BASE PARA MACHINE LEARNING
# =========================================================================

df_ml = cancerbrasil.copy()

# 1.1 Selecionando as colunas de interesse ------------------------------
# Alvo (target): tipo de câncer -> usamos 'topografia' (local do tumor),
# que é mais estável/consistente do que 'doenca' para virar variável-alvo.
colunas_interesse = ['topografia', 'sexo', 'idade', 'profissao',
                      'estadoendereco']
df_ml = df_ml[colunas_interesse]
df_ml= df_ml.dropna(subset=['profissao'])
print(df_ml.info())


# 1.2 Tratando a idade ----------------------------------------------------

df_ml['idade'] = pd.to_numeric(df_ml['idade'], errors='coerce')
df_ml = df_ml.dropna(subset=['idade'])
df_ml = df_ml[(df_ml['idade'] >= 0) & (df_ml['idade'] <= 110)]
df_ml=df_ml.dropna(subset=['estadoendereco'])

# 1.3 Criando a variável REGIÃO a partir do estado -----------------------
regioes = {
    'ACRE': 'Norte', 'AMAPÁ': 'Norte', 'AMAZONAS': 'Norte', 'PARÁ': 'Norte',
    'RONDONIA': 'Norte', 'RORAIMA': 'Norte', 'TOCANTINS': 'Norte',
    'ALAGOAS': 'Nordeste', 'BAHIA': 'Nordeste', 'CEARÁ': 'Nordeste', 'MARANHÃO': 'Nordeste',
    'PARAÍBA': 'Nordeste', 'PERNAMBUCO': 'Nordeste', 'PIAUÍ': 'Nordeste', 'RIO GRANDE DO NORTE': 'Nordeste',
    'SERGIPE': 'Nordeste',
    'DISTRITO FEDERAL': 'Centro-Oeste', 'GOIÁS': 'Centro-Oeste', 'MATO GROSSO ': 'Centro-Oeste',
    'ESPÍRITO SANTO': 'Sudeste', 'MINAS GERAIS': 'Sudeste', 'RIO DE JANEIRO': 'Sudeste', 'SÃO PAULO': 'Sudeste',
    'PARANA': 'Sul', 'RIO GRANDE DO SUL': 'Sul', 'SANTA CATARINA': 'Sul'
}
df_ml['regiao'] = df_ml['estadoendereco'].map(regioes)
df_ml = df_ml.dropna(subset=['regiao'])

# 1.4 Reduzindo o número de categorias do alvo ---------------------------
# Modelos de classificação e testes de associação ficam pouco confiáveis
# com centenas de categorias raras. Mantemos as N topografias mais
# frequentes e agrupamos o restante em "OUTROS".
N_CLASSES = 15
top_topografias = df_ml['topografia'].value_counts().nlargest(N_CLASSES).index
df_ml['topografia_agrupada'] = df_ml['topografia'].where(
    df_ml['topografia'].isin(top_topografias), 'OUTROS'
)

# 1.5 Reduzindo o número de categorias de profissão -----------------------
N_PROFISSOES = 20
top_profissoes = df_ml['profissao'].value_counts().nlargest(N_PROFISSOES).index
df_ml['profissao_agrupada'] = df_ml['profissao'].where(
    df_ml['profissao'].isin(top_profissoes), 'OUTRAS'
)

print(df_ml[['topografia_agrupada', 'sexo', 'idade',
             'profissao_agrupada', 'regiao']].info())

#%% Salvando o arquivo agrupado
#cancerbrasilunificado= cancerbrasil.to_csv("cancerbrasilunificado.csv", sep=";", encoding= 'latin1')

cancerbrasil_ml= df_ml.to_csv("cancerbrasil_ml.csv", sep=";", encoding= 'latin1')



#%% 2. ANÁLISE NÃO SUPERVISIONADA
# =========================================================================

#%% 2.1 Testes de associação (correlação entre variáveis categóricas) ----
# Para variáveis categóricas, a "correlação" é medida pelo V de Cramér,
# baseado no teste Qui-quadrado de independência.

def cramers_v(cat1, cat2):
    tabela = pd.crosstab(cat1, cat2)
    chi2 = chi2_contingency(tabela)[0]
    n = tabela.sum().sum()
    k = min(tabela.shape) - 1
    return np.sqrt(chi2 / (n * k))

associacoes = {
    'sexo': cramers_v(df_ml['topografia_agrupada'], df_ml['sexo']),
    'profissao': cramers_v(df_ml['topografia_agrupada'],
                            df_ml['profissao_agrupada']),
    'regiao': cramers_v(df_ml['topografia_agrupada'], df_ml['regiao']),
}
print("V de Cramér (associação com o tipo de câncer):")
for var, valor in associacoes.items():
    print(f"  {var}: {valor:.3f}")

# A idade é numérica: usamos ANOVA (idade varia entre os grupos de câncer?)
grupos_idade = [g['idade'].values for _, g in df_ml.groupby('topografia_agrupada')]
f_stat, p_valor = f_oneway(*grupos_idade)
print(f"\nANOVA idade x tipo de câncer: F={f_stat:.2f}, p={p_valor:.4f}")

# Boxplot idade por tipo de câncer
plt.figure(figsize=(14, 6))
ordem = df_ml.groupby('topografia_agrupada')['idade'].median().sort_values().index
sns.boxplot(data=df_ml, x='topografia_agrupada', y='idade', order=ordem)
plt.xticks(rotation=75, ha='right')
plt.title('Distribuição de idade por tipo de câncer')
plt.tight_layout()
plt.show()

#%% 2.2 Análise de Correspondência Múltipla (MCA) -------------------------
# MCA é o equivalente do PCA para dados categóricos: reduz dimensionalidade
# e permite visualizar quais categorias tendem a ocorrer juntas.

df_mca = df_ml[['topografia_agrupada', 'sexo', 'profissao_agrupada',
                 'regiao']].astype(str)

mca = prince.MCA(n_components=2, random_state=42)
mca = mca.fit(df_mca)
coords = mca.column_coordinates(df_mca)

plt.figure(figsize=(10, 8))
plt.scatter(coords[0], coords[1], alpha=0.3)
for nome, (x, y) in coords.iterrows():
    if 'topografia_agrupada_' in nome:
        plt.annotate(nome.replace('topografia_agrupada_', ''), (x, y),
                     fontsize=8, color='crimson'),
                         
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='blue', lw=0.5)
plt.title('MCA — categorias de câncer, sexo, profissão e região')
plt.xlabel('Dimensão 1')
plt.ylabel('Dimensão 2')
plt.tight_layout()
plt.show()

print(f"Inércia explicada pelas 2 dimensões: "
      f"{mca.percentage_of_variance_.sum():.1f}%")

#%% 2.3 Clusterização (K-Means) sobre as coordenadas da MCA ---------------
# Agrupamos os PACIENTES (não as categorias) para identificar perfis
# demográficos com padrões semelhantes de tipo de câncer.

coords_individuos = mca.row_coordinates(df_mca)

inercias = []
silhuetas = []
faixa_k = range(2, 9)
for k in faixa_k:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(coords_individuos)
    inercias.append(km.inertia_)
    silhuetas.append(silhouette_score(coords_individuos, labels))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(list(faixa_k), inercias, marker='o')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Inércia')
plt.title('Método do cotovelo')

plt.subplot(1, 2, 2)
plt.plot(list(faixa_k), silhuetas, marker='o', color='darkorange')
plt.xlabel('Número de clusters (k)')
plt.ylabel('Coeficiente de silhueta')
plt.title('Qualidade dos clusters')
plt.tight_layout()
plt.show()

# Escolher k pelo melhor coeficiente de silhueta
melhor_k = list(faixa_k)[np.argmax(silhuetas)]
kmeans_final = KMeans(n_clusters=melhor_k, random_state=42, n_init=10)
df_ml['cluster'] = kmeans_final.fit_predict(coords_individuos)
print(f"\nMelhor número de clusters: {melhor_k}")

# Perfil de cada cluster: tipo de câncer predominante, sexo, idade média
perfil_clusters = df_ml.groupby('cluster').agg(
    idade_media=('idade', 'mean'),
    sexo_predominante=('sexo', lambda x: x.mode()[0]),
    regiao_predominante=('regiao', lambda x: x.mode()[0]),
    topografia_predominante=('topografia_agrupada', lambda x: x.mode()[0]),
    n_pacientes=('idade', 'count')
)
print("\nPerfil dos clusters encontrados:")
print(perfil_clusters)

#%% 2.4 Dendrograma (agrupamento hierárquico) — amostra ------------------
# Em bases grandes, o dendrograma completo é inviável computacionalmente;
# usamos uma amostra para fins ilustrativos/didáticos.
amostra = df_ml.sample(n=min(300, len(df_ml)), random_state=42).index
coords_amostra = coords_individuos.loc[amostra]

Z = linkage(coords_amostra, method='ward')
plt.figure(figsize=(14, 6))
dendrogram(Z, no_labels=True)
plt.title('Dendrograma (amostra de 300 pacientes) — agrupamento hierárquico')
plt.xlabel('Pacientes')
plt.ylabel('Distância')
plt.tight_layout()
plt.show()


#%% 3. ANÁLISE SUPERVISIONADA
# =========================================================================

#%% 3.1 Preparando features (X) e alvo (y) --------------------------------

X = df_ml[['sexo', 'idade', 'profissao_agrupada', 'regiao']].copy()
y = df_ml['topografia_agrupada'].copy()

# Codificando variáveis categóricas (Label Encoding para modelos de árvore)
encoders = {}
for coluna in ['sexo', 'profissao_agrupada', 'regiao']:
    le = LabelEncoder()
    X[coluna] = le.fit_transform(X[coluna])
    encoders[coluna] = le

le_target = LabelEncoder()
y_encoded = le_target.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)

print(f"Treino: {X_train.shape[0]} pacientes | Teste: {X_test.shape[0]} pacientes")
print(f"Número de classes (tipos de câncer): {len(le_target.classes_)}")

#%% 3.2 Modelo 1 — Árvore de Decisão --------------------------------------

arvore = DecisionTreeClassifier(max_depth=6, random_state=42,
                                 class_weight='balanced')
arvore.fit(X_train, y_train)
y_pred_arvore = arvore.predict(X_test)

print("\n=== Árvore de Decisão ===")
print(f"Acurácia: {accuracy_score(y_test, y_pred_arvore):.3f}")
print(classification_report(y_test, y_pred_arvore,
                             target_names=le_target.classes_,
                             zero_division=0))

plt.figure(figsize=(30, 10))
plot_tree(arvore, feature_names=X.columns, max_depth=3,
          class_names=le_target.classes_, filled=True, fontsize=8)
plt.title('Árvore de Decisão (3 primeiros níveis)')
plt.show()

#%% 3.3 Modelo 2 — Random Forest ------------------------------------------

floresta = RandomForestClassifier(n_estimators=300, max_depth=10,
                                   random_state=42, class_weight='balanced',
                                   n_jobs=-1)
floresta.fit(X_train, y_train)
y_pred_floresta = floresta.predict(X_test)

print("\n=== Random Forest ===")
print(f"Acurácia: {accuracy_score(y_test, y_pred_floresta):.3f}")
print(classification_report(y_test, y_pred_floresta,
                             target_names=le_target.classes_,
                             zero_division=0))

# Validação cruzada (mais robusta que um único split treino/teste)
scores_cv = cross_val_score(floresta, X, y_encoded, cv=5, scoring='accuracy')
print(f"Acurácia média (validação cruzada, 5 folds): "
      f"{scores_cv.mean():.3f} +/- {scores_cv.std():.3f}")

#%% 3.4 Modelo 3 — Naive Bayes Categórico (baseline simples) --------------

nb = CategoricalNB()
# Naive Bayes categórico exige apenas colunas discretas -> removendo idade
# ou discretizando-a em faixas etárias
#%% Categoriar a variavel idade
# Criar uma nova categoria coluna 'faixa_etaria' 
bins = [0, 12, 17, 30, 59, df_ml['idade'].max() + 1]
labels = False

X_nb = X.copy()
X_nb['faixa_etaria'] = pd.cut(X_nb['idade'], bins=bins, labels=labels, right=False)

X_nb_train, X_nb_test, y_nb_train, y_nb_test = train_test_split(
    X_nb, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
)
nb.fit(X_nb_train, y_nb_train)
y_pred_nb = nb.predict(X_nb_test)
print("\n=== Naive Bayes Categórico (baseline) ===")
print(f"Acurácia: {accuracy_score(y_nb_test, y_pred_nb):.3f}")

#%% 3.5 Comparando os modelos ----------------------------------------------

comparacao = pd.DataFrame({
    'Modelo': ['Árvore de Decisão', 'Random Forest', 'Naive Bayes'],
    'Acurácia (teste)': [
        accuracy_score(y_test, y_pred_arvore),
        accuracy_score(y_test, y_pred_floresta),
        accuracy_score(y_nb_test, y_pred_nb),
    ]
})
print("\nComparação final dos modelos:")
print(comparacao)

plt.figure(figsize=(8, 5))
sns.barplot(data=comparacao, x='Modelo', y='Acurácia (teste)')
plt.ylim(0, 1)
plt.title('Comparação de acurácia entre os modelos supervisionados')
plt.tight_layout()
plt.show()

#%% 3.6 Importância das variáveis (Random Forest) --------------------------

importancias = pd.Series(floresta.feature_importances_, index=X.columns)
importancias = importancias.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=importancias.values, y=importancias.index, orient='h')
plt.title('Importância das variáveis para prever o tipo de câncer')
plt.xlabel('Importância relativa')
plt.tight_layout()
plt.show()

print("\nImportância das variáveis:")
print(importancias)

#%% 3.7 Matriz de confusão (Random Forest) ---------------------------------

matriz = confusion_matrix(y_test, y_pred_floresta)
plt.figure(figsize=(12, 10))
sns.heatmap(matriz, annot=False, cmap='Blues',
            xticklabels=le_target.classes_, yticklabels=le_target.classes_)
plt.xlabel('Predito')
plt.ylabel('Real')
plt.xticks(rotation=75, ha='right')
plt.title('Matriz de confusão — Random Forest')
plt.tight_layout()
plt.show()



