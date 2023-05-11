from fastapi import FastAPI
import uvicorn
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI()

# Cargar el archivo CSV en un DataFrame de pandas
df = pd.read_csv('dataset_transformed.csv')

df['release_date'] = pd.to_datetime(df['release_date'])
df['revenue'] = df['revenue'].astype(float)

# Desanidar campo anidado production_countries
df['production_countries'] = df['production_countries'].apply(lambda x: eval(x) if (pd.notnull(x) and eval(x)) else [])

# Diccionario para mapear nombres de meses a números
meses = {
    'enero': 1,
    'febrero': 2,
    'marzo': 3,
    'abril': 4,
    'mayo': 5,
    'junio': 6,
    'julio': 7,
    'agosto': 8,
    'septiembre': 9,
    'octubre': 10,
    'noviembre': 11,
    'diciembre': 12
}

# Función para obtener la cantidad de películas que se estrenaron en un mes específico
@app.get('/peliculas_mes')
def peliculas_mes(mes: str):

    # Obtener el número de mes correspondiente
    num_mes = meses.get(mes.lower())
    if num_mes is None:
        return {'error': 'Mes inválido'}
    
    # Filtrar el DataFrame por el mes especificado y contar las filas
    cantidad = df[df['release_date'].dt.month == num_mes].shape[0]

    return {'mes': mes, 'cantidad': cantidad}

# Función para obtener la cantidad de películas que se estrenaron en un día de la semana específico
@app.get('/peliculas_dia')
def peliculas_dia(dia: str):
    
    # Convertir el día a un entero
    dia_num = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'].index(dia.lower())
    
    # Filtrar el DataFrame por el día de la semana especificado y contar las filas
    cantidad = df[df['release_date'].dt.dayofweek == dia_num].shape[0]
    
    return {'dia': dia, 'cantidad': cantidad}

# Función para obtener información sobre una franquicia específica
@app.get('/franquicia')
def franquicia(nombre: str):
    # Filtrar el DataFrame por el nombre de la franquicia
    franquicia_df = df[df['belongs_to_collection'].str.strip() == nombre]
    
    print(franquicia_df)
    print(nombre)
    # Obtener la cantidad de películas de la franquicia
    cantidad = franquicia_df.shape[0]
    
    # Calcular la ganancia total de la franquicia
    ganancia_total = franquicia_df['revenue'].sum()
    
    # Calcular el promedio de ganancia de la franquicia
    ganancia_promedio = franquicia_df['revenue'].mean()

    # Convertir los valores numéricos a cadenas (strings)
    cantidad_str = str(cantidad)
    ganancia_total_str = str(ganancia_total)
    ganancia_promedio_str = str(ganancia_promedio)
    
    return {
        'franquicia': nombre,
        'cantidad': cantidad_str,
        'ganancia_total': ganancia_total_str,
        'ganancia_promedio': ganancia_promedio_str
    }

# Función para obtener la cantidad de películas producidas en un país específico
@app.get('/peliculas_pais')
def peliculas_pais(pais: str):
   
    # Filtrar las películas cuyo primer país de producción coincide con 'pais'
    cantidad = df[df['production_countries'].apply(lambda x: len(x) > 0 and x[0]['name'] == pais)].shape[0]

    return {'pais': pais, 'cantidad': cantidad}

# Función para obtener información sobre una productora específica
@app.get('/productoras')
def productoras(productora: str):
    # Filtrar películas por la productora especificada
    peliculas_productora = df[df['production_companies'] == productora]
    
    # Calcular la ganancia total
    ganancia_total = peliculas_productora['revenue'].sum()
    
    # Obtener la cantidad de películas producidas
    cantidad = peliculas_productora.shape[0]
    
    # Retornar la respuesta
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

# Función para obtener información sobre el retorno de inversión de una película específica
@app.get('/retorno')
def retorno(pelicula: str):
    pelicula_info = df[df['title'] == pelicula]
    if len(pelicula_info) == 0:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    inversion = pelicula_info['budget'].values[0]
    ganancia = pelicula_info['revenue'].values[0]
    retorno = pelicula_info['return'].values[0]
    anio = pelicula_info['release_year'].values[0]
    
    return {
        'pelicula': pelicula,
        'inversion': inversion,
        'ganancia': ganancia,
        'retorno': retorno,
        'anio': anio
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
