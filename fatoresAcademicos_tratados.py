import pandas as pd
import numpy as np

#%%
dados_tratados = pd.read_csv('Base_Dados/Tratado_Placement_Data_Full_Class.csv')

#%%
df2 = pd.DataFrame(dados_tratados)
#Verifando as primeiras colunas do dataset
df2.head()

#%%
#Exibindo um resumo conciso do Dataframe
df2.info()

#%%
df2['salario'].describe()

#%%
df2.describe()