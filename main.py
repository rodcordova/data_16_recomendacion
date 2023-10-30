from fastapi import FastAPI
import pandas as pd
#import joblib

app = FastAPI()

df1 = pd.read_csv(r"consulta1.csv")

@app.get("/developer/{desarrollador}")
def developer(desarrollador:str):
    '''
    te da cantidad de items y % de contenido free segun la empresa desarrolladora
    '''
   
   # Filtro por el publisher # Agrupado
    filtrado=df1[df1['publisher']==desarrollador].groupby('release_year')['price'].agg([('Cantidad free',lambda x:(x==0.00).sum()),('Totoal elementos', 'count')]).reset_index()

    filtrado['porcentaje_free']= filtrado.apply(lambda x:round(x['Cantidad free']/x['Totoal elementos'],2)*100 if x['Totoal elementos']!= 0 else 0,axis=1)

    
    # Se crea el diccionario de respuesta
    respuesta = {
        'desarrollador': desarrollador,
        'Anio': filtrado['release_year']
        }

    return respuesta

#release_year	Cantidad free	Totoal elementos	porcentaje_free