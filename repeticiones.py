import pandas as pd
from IPython.display import HTML
# archivo = "C:/Users/Usuario/Desktop/PROPUESTA FINAL.xlsm"
# archivo = "C:/Users/CEMAE4/OneDrive - IKEA/Escritorio/PROPUESTA FINAL.xlsm"
archivo = "./static/archivos/PROPUESTA_FINAL"

df2 = pd.read_excel(archivo, sheet_name="PICKING")
df = df2[["NOMBRE", "MV", "REF", "DESDE"]].dropna()
indices_a_eliminar = df[~df["DESDE"].str.contains("-", regex=False, na=False)].index
df = df.drop(indices_a_eliminar, axis=0)

df["REF"] = df["REF"].astype(int)
df["REPETICIONES"] = df.groupby("REF")["REF"].transform("count")
df_filtrado2 = df[df["REPETICIONES"] > 10]
df_filtrado = df_filtrado2.drop_duplicates(subset="REF")

resultado = df_filtrado[["NOMBRE", "REF", "REPETICIONES"]]
resultado_ordenado = resultado.sort_values(by="REPETICIONES", ascending=False)

repeticiones_html = HTML(resultado_ordenado.to_html(classes="table table-dark table-striped table-bordered table-sm text-center",
                                           index=False, justify="center", columns=["NOMBRE", "REF", "REPETICIONES"]))

