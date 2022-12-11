import pandas as pd
import plotly.express as px

# 1. Importando a base de dados
tabela = pd.read_csv("Base de dados.csv")

# 2. Visualizando a base de dados
print(tabela)

# 3. Tratando os dados
print(tabela.info())

# 3.1 Verificando as variáveis de cada coluna
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# 3.2 Excluindo colunas desnecessárias
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("IDCliente", axis=1)
tabela = tabela.dropna(how="all", axis=1)

# 3.3 Analisando as células vazias
tabela = tabela.dropna(how="any", axis=0)
print(tabela)
print(tabela.info())

# 4. Analisando
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))

# 4.1 Analisando Graficamente
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.show()
