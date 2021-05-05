import numpy as np
import pandas as pd
import xlrd
import openpyxl

# zad1
xlsl = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel('imiona.xlsx', header=0)
print(df)

# zad2
print(df[df["Liczba"] < 1000])
grupa = df.groupby(['Imie'])
print(grupa.get_group('PIOTR'))
print(df.agg({'Liczba':['sum']}))
rok1 = df[((df.Rok > 2004) & (df.Rok < 2011))]
print(rok1.agg({'Liczba':['sum']}))
