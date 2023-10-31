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

    anio=[fila for fila in filtrado['release_year']]
    cantElementos=[fila for fila in filtrado['Totoal elementos']]
    free=[fila for fila in filtrado['porcentaje_free']]
    # Se crea el diccionario de respuesta
    respuesta = {
        'desarrollador': desarrollador,
        'Anio': anio,
        'Cantidad items':cantElementos,
        "Contenido free":free
        }

    return respuesta

#release_year	Cantidad free	Totoal elementos	porcentaje_free

@app.get("/userdata/{User_id}")
def userdata(User_id:str):
    filtrado=df1[df1['user_id']==User_id]

    gastado=filtrado['price'].sum()

    cantidad_items=filtrado.shape[0]

    positivo=[reco for reco in filtrado['recommend'] if reco==True]
    cant_pos=len(positivo)
    porcentaje=cant_pos/cantidad_items

    respuesta = {
        'User_id': User_id,
        'Dinero_gastado': gastado,
        'Cantidad_items':cantidad_items,
        "%recomendacion":porcentaje
        }

    return respuesta

@app.get("/best_developer/{anio}")
def best_developer(anio:str):
    # filtramos por el anio
    filtrado=df1[df1['release_year']==anio]

    # cantidad total por año 
    top_developers = filtrado.groupby('release_year')['user_id'].agg([('cantidad','count')])
    top_developers.reset_index()

    # cantidad total de año positivos
    cantpos = filtrado.groupby(['release_year','developer'])['recommend'].agg([('cantidad_pos',lambda x:(x==True).count())])
    cantpos=cantpos.reset_index()

    # Combinar DataFrames utilizando 'merge'
    resultado = top_developers.merge(cantpos, on='release_year', how='outer')
    
    # divido 2 columnas del dataframe
    resultado['total']=resultado['cantidad_pos']/resultado['cantidad']

    # ordeno y reseteo el indice
    resultado=resultado.sort_values(by='total', ascending=False)
    resultado.reset_index(drop=True)

    respuesta = {[
        'developer1': resultado.iloc[0]['developer'],
        'developer2': resultado.iloc[1]['developer'],
        'developer3': resultado.iloc[2]['developer']]
        }

    return respuesta