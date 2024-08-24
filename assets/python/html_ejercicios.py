from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_db_connection, store_exercise_result, get_user_performance, update_user_streak, update_daily_tracking
from ml_utils import generate_recommendation
import tensorflow as tf
import numpy as np

app = Flask(__name__)
CORS(app)

# Cargar el modelo entrenado
# model = tf.keras.models.load_model('path_to_your_saved_model')

def get_random_question(difficulty=None):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT id, pregunta, respuesta, dificultad, lenguaje_id FROM ejercicios WHERE lenguaje_id = 1"
        params = []
        
        if difficulty:
            query += " AND dificultad = %s"
            params.append(difficulty)
        
        query += " ORDER BY RAND() LIMIT 1"
        
        cursor.execute(query, params)
        
        question = cursor.fetchone()
        
        return question
    
    except Error as e:
        print(f"Error: {e}")
        return None
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_question', methods=['GET'])
def get_question():
    difficulty = request.args.get('difficulty', type=int)
    question = get_random_question(difficulty)
    if question:
        return jsonify({
            "id": question['id'],
            "question": question['pregunta'],
            "difficulty": question['dificultad'],
            "language_id": question['lenguaje_id']
        })
    else:
        return jsonify({"error": "No se pudo obtener una pregunta"}), 500

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data['answer'].lower().strip()
    question_id = data['question_id']
    user_id = data.get('user_id', 1)
    time_taken = data.get('time_taken', 0)
    
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        
        query = "SELECT respuesta, dificultad, lenguaje_id FROM ejercicios WHERE id = %s"
        cursor.execute(query, (question_id,))
        
        result = cursor.fetchone()
        
        if result:
            correct_answer = result['respuesta'].lower().strip()
            difficulty = result['dificultad']
            language_id = result['lenguaje_id']
            is_correct = user_answer == correct_answer
            
            store_exercise_result(user_id, question_id, user_answer, is_correct, time_taken, language_id, difficulty)
            update_user_streak(user_id)
            update_daily_tracking(user_id, language_id, 1, time_taken)
            
            return jsonify({
                "is_correct": is_correct,
                "correct_answer": result['respuesta'],  # Devuelve la respuesta original sin modificar
                "difficulty": difficulty
            })
        else:
            return jsonify({"error": "Pregunta no encontrada"}), 404
    
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Error al procesar la respuesta"}), 500
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get_performance', methods=['GET'])
def get_performance():
    user_id = request.args.get('user_id', 1, type=int)
    language_id = request.args.get('language_id', 1, type=int)  # Asumimos que HTML tiene id 1
    performance_data = get_user_performance(user_id, language_id)
    
    if performance_data is None:
        return jsonify({"error": "No se pudo obtener el rendimiento del usuario"}), 500
    
    return jsonify(performance_data)

@app.route('/get_recommendation', methods=['GET'])
def get_recommendation():
    user_id = request.args.get('user_id', type=int)
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    recommendation = generate_recommendation(user_id)
    return jsonify({"recommendation": recommendation})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)