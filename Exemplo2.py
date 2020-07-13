import pandas as pd
import matplotlib.pyplot as plt

url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_residencial.csv"
df_residencial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")
anos = list(df_residencial.columns)
df_residencial = df_residencial.transpose()
cidades = list(df_residencial.columns)

url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_industrial.csv"
df_industrial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")
df_industrial = df_industrial.transpose()

url ="https://github.com/armandokeller/conecta_202001/raw/master/energia_rs/energia_comercial.csv"
df_comercial = pd.read_csv(url,sep=";",encoding="ISO-8859-1",skiprows=6,index_col="Município")
df_comercial = df_comercial.transpose()

cidade = "São Leopoldo"
plt.plot(anos, df_residencial[cidade], label="Residencial")
plt.plot(anos, df_industrial[cidade], label="Industrial")
plt.plot(anos, df_comercial[cidade], label="Comercial")
plt.legend()
plt.ylabel("Energia [MWh]")
plt.xlabel("Ano")
plt.title(f"Consumo de energia em {cidade} - RS")
plt.grid(True)
plt.show()

plt.plot(anos, (df_industrial[cidade]+df_comercial[cidade])/df_residencial[cidade])
plt.title("Relação entre consumo comercial e industrial pelo residêncial")
plt.grid(True)
plt.show()