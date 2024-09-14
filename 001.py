import pandas as pd
import numpy as np


df = pd.read_excel("INPUT DATA.xlsx")

# print(df.columns)

df['Sum'] = df[['Ni', 'Co', 'Al2O3', 'CaO', 'Cr2O3', 'Fe2O3', 'K2O',
                 'MgO', 'MnO', 'Na2O', 'P*', 'S*', 'SiO2', 'TiO2', 'LOI']].sum(axis=1)

df["diff"] = np.round(100-df["Sum"])

df

df["macro"]=df[["Fe2O3","Al2O3","SiO2","LOI"]].sum(axis=1)
df["%LOI"]=df["LOI"]/df["macro"]
df["%SiO2"]=df["SiO2"]/df["macro"]
df["%Fe2O3"]=df["Fe2O3"]/df["macro"]
df["%Al2O3"]=df["Al2O3"]/df["macro"]

df["LOI"]+=np.round((df["diff"]*df['%LOI']),2)
df["SiO2"]+=np.round((df["diff"]*df["%SiO2"]),2)
df["Fe2O3"]+=np.round((df["diff"]*df["%Fe2O3"]),2)
df["Al2O3"]+=np.round((df["diff"]*df["%Al2O3"]),2)
df['Sum'] = df[['Ni', 'Co', 'Al2O3', 'CaO', 'Cr2O3', 'Fe2O3', 'K2O',
                 'MgO', 'MnO', 'Na2O', 'P*', 'S*', 'SiO2', 'TiO2', 'LOI']].sum(axis=1)
# df=df[['SAMPLE','Ni', 'Co', 'Al2O3', 'CaO', 'Cr2O3', 'Fe2O3', 'K2O',
#                  'MgO', 'MnO', 'Na2O', 'P*', 'S*', 'SiO2', 'TiO2', 'LOI']]
df["Sum"]
# df.to_excel("output.xlsx")


