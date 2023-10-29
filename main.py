from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()


@app.get("/userdata/{User_id}")
def userdata(User_id:str):
    '''
    Devuelve la cantidad de dinero gastado por el usuario ingresado, el porcentaje de 
    recomendaciones que dejo y cuantos juegos comprados tiene en su libreria.
    '''
   #
   #filtered_df = df_userdata.query(f"user_id == '{User_id}'")
   #response= {"Usuario_ingresado":str(filtered_df.iloc[0,0]),
   #        "Dinero_Gastado":int(filtered_df.iloc[0,2]),
   #        "Porcentaje de recomendaciones hechas positivas":float(filtered_df.iloc[0,3]),
   #        "Cantidad de Juegos en libreria":int(filtered_df.iloc[0,1])}
    return 'response'