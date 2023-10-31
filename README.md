# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

# Recomendador de Juegos para Steam

## Descripción del Proyecto

Este proyecto tiene como objetivo crear un sistema de recomendación de videojuegos para los usuarios de Steam, una plataforma multinacional de videojuegos. El proyecto abarca desde la recopilación y transformación de datos hasta la creación de una API para proporcionar recomendaciones a los usuarios.

## Rol y Tareas

Como Data Scientist en Steam, tu rol es crear un sistema de recomendación de videojuegos. El proyecto incluye las siguientes tareas:


### Desarrollo de API

Se propone la creación de una API utilizando el framework FastAPI que proporcionará las siguientes consultas:

- `developer(desarrollador)`: Proporciona la cantidad de juegos y el porcentaje de contenido gratuito por año según la empresa desarrolladora.
- `userdata(User_id)`: Devuelve información sobre el dinero gastado por el usuario, el porcentaje de recomendación en base a las reviews y la cantidad de juegos.
- `UserForGenre(genero)`: Encuentra al usuario con más horas jugadas para el género dado y proporciona una lista de las horas jugadas por año de lanzamiento.
- `best_developer_year(año)`: Ofrece el top 3 de desarrolladores con juegos más recomendados por usuarios para el año dado.
- `developer_reviews_analysis(desarrolladora)`: Presenta el análisis de sentimiento de las reseñas de usuarios para un desarrollador específico.

### Deployment

El proyecto se desplegará en un servicio como Render

### Análisis Exploratorio de Datos (EDA)

Se realizará un análisis exploratorio de los datos para comprender las relaciones entre las variables, identificar outliers y patrones interesantes. Se pueden generar nubes de palabras para visualizar las palabras más frecuentes en los títulos de juegos.

### Modelo de Aprendizaje Automático

Se desarrollará un modelo de recomendación basado en ítem-ítem o usuario-ítem. El modelo permitirá recibir un juego o un usuario como entrada y proporcionará una lista de juegos recomendados.

## Instrucciones de Uso

Para utilizar la API y obtener recomendaciones de juegos, siga las instrucciones a continuación:

1. Acceda a la API en la siguiente dirección: [https://data16-recomendaciones.onrender.com/docs]



2. Recibirá las respuestas en formato JSON con los resultados de las consultas.

## Requerimientos

Este proyecto utiliza las siguientes tecnologías:

- Python
- FastAPI
- Bibliotecas de análisis de datos (pandas, nltk, etc.)
- Bibliotecas de aprendizaje automático (scikit-learn)

## Contribución

Si deseas contribuir a este proyecto, siéntete libre de abrir problemas (issues) o enviar solicitudes de extracción (pull requests).

## Créditos

Este proyecto ha sido desarrollado por Rodrigo para Steam.


