import pandas as pd
import numpy as np

#%%
dados = pd.read_csv('Base_Dados/Placement_Data_Full_Class.csv')
#%%
df = pd.DataFrame(dados)
#Verifando as primeiras colunas do dataset
df.head()
#%%
#Exibindo um resumo conciso do Dataframe
df.info()
#Verificando que temos dados ausentes na coluna de 'salary'
#%%
#Verificando a dimensão do dateset
df.shape
#%%
# Verificando a contagem de valores nulos por coluna
print("\n--- Contagem de Valores Nulos (Antes) ---")
print(df.isnull().sum())

#Temos 67 valores nulos na coluna coluna 'salary'
#%%
#pegando o valor da moda no salario, para preencher os valores ausentes
moda_salario = df['salary'].mode()[0]
moda_salario
#%%
#Preenchendo os valores ausentes no salario
df['salary'].fillna(moda_salario, inplace=True)
df['salary']
#%%
# Verificando a contagem de valores nulos por coluna
print("\n--- Contagem de Valores Nulos (Depois) ---")
print(df.isnull().sum())

