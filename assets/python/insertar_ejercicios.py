import mysql.connector
from mysql.connector import Error

questions = [
    {
        "question": "¿Cuál es la etiqueta HTML para crear un enlace?",
        "answer": "<a>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear una lista no ordenada?",
        "answer": "<ul>",
        "difficulty": 1
    },
    {
        "question": "¿Cuál es la etiqueta para crear un encabezado de nivel 1?",
        "answer": "<h1>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear una tabla?",
        "answer": "<table>",
        "difficulty": 2
    },
    {
        "question": "¿Cuál es la etiqueta para crear un párrafo?",
        "answer": "<p>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un botón?",
        "answer": "<button>",
        "difficulty": 2
    },
    {
        "question": "¿Cuál es la etiqueta para crear un input de texto?",
        "answer": "<input>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear una imagen?",
        "answer": "<img>",
        "difficulty": 1
    },
    {
        "question": "¿Cuál es la etiqueta para crear una lista ordenada?",
        "answer": "<ol>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 2?",
        "answer": "<h2>",
        "difficulty": 1
    },
    {
        "question": "¿Cuál es la etiqueta para crear un enlace a un archivo CSS?",
        "answer": "<link>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 3?",
        "answer": "<h3>",
        "difficulty": 1
    },
    {
        "question": "¿Cuál es la etiqueta para crear un enlace a un archivo JavaScript?",
        "answer": "<script>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 4?",
        "answer": "<h4>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 5?",
        "answer": "<h5>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 6?",
        "answer": "<h6>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un párrafo de texto grande?",
        "answer": "<big>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un párrafo de texto pequeño?",
        "answer": "<small>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un salto de línea?",
        "answer": "<br>",
        "difficulty": 1
    },
    {
        "question": "¿Qué etiqueta se usa para crear un espacio en blanco?",
        "answer": "<nbsp>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un div?",
        "answer": "<div>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un span?",
        "answer": "<span>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un formulario?",
        "answer": "<form>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo checkbox?",
        "answer": "<input type='checkbox'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo radio?",
        "answer": "<input type='radio'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo submit?",
        "answer": "<input type='submit'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo text?",
        "answer": "<input type='text'>",
        "difficulty": 2
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo password?",
        "answer": "<input type='password'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo file?",
        "answer": "<input type='file'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo hidden?",
        "answer": "<input type='hidden'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo image?",
        "answer": "<input type='image'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo reset?",
        "answer": "<input type='reset'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo button?",
        "answer": "<input type='button'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo color?",
        "answer": "<input type='color'>",
        "difficulty": 3
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo date?",
        "answer": "<input type='date'>",
        "difficulty": 3
    },
    {
        "question": "Escribe el código HTML para crear una lista desordenada con los nombres `Pepe`, `Juan` y `Ana`.",
        "answer": "<ul><li>Pepe</li><li>Juan</li><li>Ana</li></ul>",
        "difficulty": 3
    }
]

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="login_infoacademy"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def ensure_language_exists(cursor, language_name='HTML'):
    query = "SELECT id FROM lenguajes WHERE nombre = %s"
    cursor.execute(query, (language_name,))
    result = cursor.fetchone()
    
    if result:
        return result[0]
    else:
        insert_query = "INSERT INTO lenguajes (nombre) VALUES (%s)"
        cursor.execute(insert_query, (language_name,))
        return cursor.lastrowid

def insert_exercises():
    connection = get_db_connection()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        
        # Asegurarse de que el lenguaje HTML existe y obtener su ID
        html_id = ensure_language_exists(cursor)
        
        for question in questions:
            query = """
            INSERT INTO ejercicios (lenguaje_id, descripcion, pregunta, respuesta, dificultad)
            VALUES (%s, %s, %s, %s, %s)
            """
            values = (html_id, "Ejercicio de HTML", question['question'], question['answer'], question['difficulty'])
            
            cursor.execute(query, values)
        
        connection.commit()
        print(f"Se insertaron {len(questions)} ejercicios en la base de datos.")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_exercises()