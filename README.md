# HenryPIMovie

Esta es una API para obtener información sobre películas y realizar recomendaciones. La API utiliza el framework FastAPI y está construida sobre un dataset de películas.

Configuración
Asegúrate de tener instaladas todas las dependencias necesarias mencionadas en el archivo requirements.txt.

Ejecución de la API
Asegúrate de estar en el directorio raíz del proyecto.

Ejecuta el siguiente comando para iniciar el servidor de desarrollo de FastAPI:

bash
Copy code
uvicorn main:app --reload
Esto iniciará el servidor de desarrollo de FastAPI y la API estará disponible en http://localhost:8000.

Endpoints
Obtener la cantidad de películas que se estrenaron en un mes específico
URL: /peliculas_mes
Método: GET
Parámetros de consulta:
mes (str): El nombre del mes en español (ejemplo: "enero", "febrero", etc.)
Respuesta exitosa:
Código de estado: 200
Cuerpo de la respuesta:
json
Copy code
{
    "mes": "nombre_mes",
    "cantidad": cantidad_peliculas
}
Ejemplo de uso:
bash
Copy code
GET /peliculas_mes?mes=enero
Obtener la cantidad de películas que se estrenaron en un día de la semana específico
URL: /peliculas_dia
Método: GET
Parámetros de consulta:
dia (str): El nombre del día de la semana en español (ejemplo: "lunes", "martes", etc.)
Respuesta exitosa:
Código de estado: 200
Cuerpo de la respuesta:
json
Copy code
{
    "dia": "nombre_dia",
    "cantidad": cantidad_peliculas
}
Ejemplo de uso:
bash
Copy code
GET /peliculas_dia?dia=lunes
Obtener información sobre una franquicia específica
URL: /franquicia
Método: GET
Parámetros de consulta:
nombre (str): El nombre de la franquicia
Respuesta exitosa:
Código de estado: 200
Cuerpo de la respuesta:
json
Copy code
{
    "franquicia": "nombre_franquicia",
    "cantidad": cantidad_peliculas,
    "ganancia_total": ganancia_total_franquicia,
    "ganancia_promedio": ganancia_promedio_franquicia
}
Ejemplo de uso:
bash
Copy code
GET /franquicia?nombre=Star Wars
Obtener la cantidad de películas producidas en un país específico
URL: /peliculas_pais
Método: GET
Parámetros de consulta:
pais (str): El nombre del país
Respuesta exitosa:
Código de estado: 200
Cuerpo de la respuesta:
json
Copy code
{
    "pais": "nombre_pais",
    "cantidad
