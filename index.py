import pandas as pd
import plotly_express as px

df = pd.read_excel('Relatorio_05-2024.xlsx')

df.head()

df.tail()#visualizar  valores da dataframe

print(df.Produto.value_counts())

print(df.describe().round(2))

grafico = px.histogram(df, 'Tipo', 'Lucro', text_auto=True)
print(grafico)

