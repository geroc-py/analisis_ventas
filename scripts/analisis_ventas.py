import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../datos/ventas.csv") # Carga de dataset

df["total_venta"] = df["id"] * df["sales_amount"] # Cálculo de total de venta por fila

ventas_totales = df["total_venta"].sum() # Cálculo de ventas totales
producto_mas_vendido = df.groupby("id")["sales_amount"].sum().idxmax() # Cálculo del producto más vendido

print("Ventas totales:", ventas_totales) # Impresión de ventas totales
print("Producto mas vendido:", producto_mas_vendido)

df["fecha"] = pd.to_datetime(df["sales_date"]) # Gráfico de ventas mensuales
df["mes"] = df["fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("mes")["total_venta"].sum()

ventas_por_mes.plot(kind="bar", figsize=(12, 5), color="steelblue") # Formato del gráfico
plt.title("Ventas Mensuales 2024")
plt.xlabel("Mes")
plt.ylabel("Total ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../resultados/grafico_ventas.png")
plt.show()

print("La generación ha sido exitosa, el gráfico se ha guardado en '../resultados/grafico_ventas.png'")