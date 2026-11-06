# importar librerias 
import pandas as pd
import numpy as np

print("analisis de datos vehiculos valeria yaretzi NC = 1341 ")

vehiculos = {
    "Modelo": ["Sedan X", "SUV Compact", "Hatchback Z", "Pickup Heavy", "Electric Eco", "Coupe Sport"],
    "Tipo_Motor": ["Gasolina", "Electrico", "Gasolina", "Diesel", "Electrico", "Gasolina"], # 'Electrico' se repite
    "Autonomia_Km": [600, 800, 550, 700, 450, 500],
    "Precio_USD": [22000, 35000, 18000, 45000, 32000, 41000]
}

df = pd.DataFrame(vehiculos)
print(df)

print("-+-+-Agrupar por tipo de motor -++-+--")
agrupado = df.groupby('Tipo_Motor')
print(agrupado)

print("-+-+-por agregacion -++-+--")
# precio promedio por cada tipo de motor
print(agrupado['Precio_USD'].mean())

# precio maximo por cada tipo de motor
print(agrupado['Precio_USD'].max())