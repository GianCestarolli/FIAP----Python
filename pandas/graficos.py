import pandas as pd
import matplotlib.pyplot as plb

df = pd.read_csv(r'C:\Users\logonrmlocal\Downloads\manutencao_preditiva.csv')

x = df["UDI"]
y1 = df["Temperatura Ar [K]"]
y2 = df["Temperatura Processo [K]"]

plb.plot(x,y1)
plb.xlabel("Amostras")
plb.ylabel("Temperaturas")
plb.title("Curvas de temperatura")

plb.show()