import pandas as pd
import os
# Ricardo Lopez NC 0085
# URL del dataset público
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
# Descargar y cargar el CSV
datos = pd.read_csv(url)
print(datos)
# Guardar una copia local
datos.to_csv("datasets/iris.csv", index=False)
# explorar datos
print("primeras 5 filas")
print(datos.head())
print()
print("\\nCANTIDAD DE FILAS Y COLUMNAS")
print(datos.shape)
print("\\nNOMBRES DE LAS COLUMNAS")
print(datos.columns.tolist())
print("\\nINFORMACION DEL DATASET")
print(datos.info())
print("\\nINFORMACION DEL DATASET")
print(datos.info())
print("\\nCARACTERISTICAS (X)")
X = datos.drop(columns=["species"])
print(X.head())
print("\\nVARIABLE OBJETIVO (y)")
y = datos["species"]
print(y.head())
print("\\nESPECIES REGISTRADAS")
print(y.unique())
