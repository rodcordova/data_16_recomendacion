# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Descripción

Este proyecto es una API basada en FastAPI que proporciona información y recomendaciones relacionadas con juegos de Steam. La API ofrece diversas funciones que permiten a los usuarios obtener datos sobre usuarios, reseñas, géneros, desarrolladores y análisis de sentimientos de juegos.

## Requisitos

- Python 3.7 o superior
- Bibliotecas necesarias: fastapi, pandas, joblib (puedes instalarlas utilizando `pip install -r requirements.txt`)

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las bibliotecas requeridas utilizando `pip install -r requirements.txt`.
3. Asegúrate de tener los archivos de datos en la carpeta `data_api` (user_data.csv, count_reviews.csv, genre.csv, userforgenre.csv, developer.csv, sentiment_analysis.csv).
4. Ejecuta la API utilizando `uvicorn main:app --reload` desde la línea de comandos.

## Uso

### Funciones de la API

1. **/userdata/{User_id}**: Devuelve información sobre un usuario específico, incluyendo el dinero gastado, el porcentaje de recomendaciones positivas y la cantidad de juegos en su librería.

   Ejemplo de solicitud:

GET /userdata/{User_id}