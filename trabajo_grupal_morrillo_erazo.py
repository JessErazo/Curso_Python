############################################## CURSO PYTHON ############################################

#Integrantes: Fernando Morillo y Jéssica Erazo
#Trabjado en grupo
#Indocador: Acceso a energía eléctrica 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_countries = pd.read_excel("datos\API_EG.ELC.ACCS.ZS_DS2_es_excel_v2_1652.xls",sheet_name="Metadata - Countries") ##Base 1
df_acceso_elec= pd.read_excel("datos/API_EG.ELC.ACCS.ZS_DS2_es_excel_v2_1652.xls",sheet_name="Data", skiprows=3) ##Base 2

##Primera pregunta: ¿Cuál es el valor promedio del indicador seleccionado entre los países de América Latina en el año 2020?
amer_lati= df_countries[df_countries["Region"]=="América Latina y el Caribe (excluido altos ingresos)"]
df_AL_electr = amer_lati.merge(df_acceso_elec,on=["Country Name","Country Code"], how="left") ##Union de base 1 y 2 

##Calcular el valor promedio en el año 2020 sobre el acceso a electricidad en America Latina
prom_amer_lati_2020=df_AL_electr["2020"].mean() 
print(prom_amer_lati_2020)
print(f"El valor promedio de acceso a electricidad de los países de América Latina en 2020 es de {prom_amer_lati_2020} %.")

##Segunda preunta: ¿Cómo ha evolucionado este indicador a lo largo del tiempo en América Latina?
df_amelati_elec = df_AL_electr.drop(["Country Name", "Country Code", "Region", "Income_Group", "Indicator Name", "Indicator Code"], axis=1)
resum_AL= df_amelati_elec.describe()
average_amerlati = resum_AL.iloc[1].to_numpy(copy=True)
df_serie_amerlati=pd.DataFrame()
an_os = list(range(1960, 2023, 1)) 
df_serie_amerlati["Year"]=an_os
df_serie_amerlati["Media AL"]=average_amerlati
df_serie_amerlati=df_serie_amerlati.dropna()
Graf_AL = sns.lineplot(data = df_serie_amerlati, x="Year", y="Media AL")
plt.title("La evolución del índice de acceso a electricidad de Amércia Latina durante 1990 a 2021")
plt.show()
##El índice de acceso a lectricidad presenta una tendencia creciente a lo largo del tiempo, sin embargo, antes del año 2000 podemos observar pertubaciones y picos donde el índice cae.

##Tercera pregunta: ¿Cómo es el mapa de correlación entre los últimos 5 años de datos disponibles para los países de América Latina?
df_amerlati_5_years=df_amelati_elec [["2017","2018","2019","2020","2021"]]
matriz_correlacion=df_amerlati_5_years.corr()
mapa_correlacion= sns.heatmap(matriz_correlacion, annot=True, cmap="YlGnBu", vmax=1, vmin=-1)
plt.title("Mapa de correlacion")
plt.show()
##Se puede observar que en los últimos 5 años se ha experimentado una fuerte correlacion para los paises latinos.
