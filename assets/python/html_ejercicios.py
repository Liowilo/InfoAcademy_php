from flask import Flask, jsonify, request
from flask_cors import CORS
import random
from database import store_exercise_result, get_user_performance

app = Flask(__name__)
CORS(app)

questions = [
    {
        "question": "¿Cuál es la etiqueta HTML para crear un enlace?",
        "answer": "<a>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear una lista no ordenada?",
        "answer": "<ul>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear un encabezado de nivel 1?",
        "answer": "<h1>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear una tabla?",
        "answer": "<table>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear un párrafo?",
        "answer": "<p>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un botón?",
        "answer": "<button>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear un input de texto?",
        "answer": "<input>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear una imagen?",
        "answer": "<img>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear una lista ordenada?",
        "answer": "<ol>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 2?",
        "answer": "<h2>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear un enlace a un archivo CSS?",
        "answer": "<link>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 3?",
        "answer": "<h3>"
    },
    {
        "question": "¿Cuál es la etiqueta para crear un enlace a un archivo JavaScript?",
        "answer": "<script>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 4?",
        "answer": "<h4>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 5?",
        "answer": "<h5>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un encabezado de nivel 6?",
        "answer": "<h6>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un párrafo de texto grande?",
        "answer": "<big>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un párrafo de texto pequeño?",
        "answer": "<small>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un salto de línea?",
        "answer": "<br>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un espacio en blanco?",
        "answer": "<nbsp>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un div?",
        "answer": "<div>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un span?",
        "answer": "<span>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un formulario?",
        "answer": "<form>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo checkbox?",
        "answer": "<input type='checkbox'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo radio?",
        "answer": "<input type='radio'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo submit?",
        "answer": "<input type='submit'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo text?",
        "answer": "<input type='text'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo password?",
        "answer": "<input type='password'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo file?",
        "answer": "<input type='file'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo hidden?",
        "answer": "<input type='hidden'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo image?",
        "answer": "<input type='image'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo reset?",
        "answer": "<input type='reset'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo button?",
        "answer": "<input type='button'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo color?",
        "answer": "<input type='color'>"
    },
    {
        "question": "¿Qué etiqueta se usa para crear un input de tipo date?",
        "answer": "<input type='date'>"
    },
    {
        "question": "Escribe el código HTML para crear una lista desordenada con los nombres `Pepe`, `Juan` y `Ana`.",
        "answer": "<ul><li>Pepe</li><li>Juan</li><li>Ana</li></ul>"
    }
    # Añade más preguntas aquí
]

@app.route('/get_question', methods=['GET'])
def get_question():
    question = random.choice(questions)
    return jsonify({"question": question["question"]})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data['answer']
    question = data['question']
    user_id = data.get('user_id', 1)  # Asume un ID de usuario por defecto si no se proporciona
    time_taken = data.get('time_taken', 0)  # Tiempo en segundos
    
    for q in questions:
        if q['question'] == question:
            correct_answer = q['answer']
            break
    
    is_correct = user_answer.lower().strip() == correct_answer.lower()
    
    # Almacena el resultado en la base de datos
    store_exercise_result(user_id, question, user_answer, is_correct, time_taken)
    
    return jsonify({
        "is_correct": is_correct,
        "correct_answer": correct_answer
    })

@app.route('/get_performance', methods=['GET'])
def get_performance():
    user_id = request.args.get('user_id', 1)  # Asume un ID de usuario por defecto si no se proporciona
    performance_data = get_user_performance(user_id)
    
    if performance_data is None:
        return jsonify({"error": "No se pudo obtener el rendimiento del usuario"}), 500
    
    return jsonify(performance_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)