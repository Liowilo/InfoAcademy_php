from flask import Blueprint, jsonify, request, current_app
from flask_cors import CORS
from js_evaluator import evaluate_js_code
from database import (
    get_db_connection,
    store_exercise_result,
    get_user_performance,
    update_user_streak,
    update_daily_tracking,
)
from ml_utils import generate_recommendation
import mysql.connector
import traceback
import sys
import json
import logging

js_bp = Blueprint('javascript', __name__)

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@js_bp.route("/")
def home():
    return "Servidor Flask para ejercicios de JavaScript funcionando correctamente."

@js_bp.route("/test")
def test():
    return jsonify({"message": "Conexión exitosa al servidor Flask"})

def get_random_js_question(difficulty=None):
    connection = get_db_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT id, pregunta, respuesta, dificultad, lenguaje_id FROM ejercicios WHERE lenguaje_id = 3"  # 3 para JavaScript
        params = []

        if difficulty:
            query += " AND dificultad = %s"
            params.append(difficulty)

        query += " ORDER BY RAND() LIMIT 1"

        cursor.execute(query, params)

        question = cursor.fetchone()

        return question

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@js_bp.route("/get_js_question", methods=["GET"])
def get_js_question():
    difficulty = request.args.get("difficulty", type=int)
    question = get_random_js_question(difficulty)
    if question:
        return jsonify(
            {
                "id": question["id"],
                "question": question["pregunta"],
                "difficulty": question["dificultad"],
                "language_id": question["lenguaje_id"],
            }
        )
    else:
        return jsonify({"error": "No se pudo obtener una pregunta de JavaScript"}), 500

@js_bp.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {str(e)}")
    logger.error(traceback.format_exc())
    return (
        jsonify(
            {
                "error": "Ha ocurrido un error inesperado en el servidor",
                "details": str(e),
                "traceback": traceback.format_exc(),
            }
        ),
        500,
    )

@js_bp.route("/check_js_answer", methods=["POST"])
def check_js_answer():
    logger.info("Iniciando check_js_answer")
    try:
        data = request.get_json(force=True)
        logger.debug(f"Datos recibidos: {data}")
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON de la solicitud: {str(e)}")
        return jsonify({"error": "Solicitud inválida", "details": str(e)}), 400

    user_answer = data.get("answer")
    question_id = data.get("question_id")
    user_id = data.get("user_id", 1)
    time_taken = data.get("time_taken", 0)

    if not all([user_answer, question_id]):
        logger.warning("Faltan datos requeridos en la solicitud")
        return jsonify({"error": "Faltan datos requeridos"}), 400

    logger.info(f"Procesando respuesta para pregunta ID: {question_id}, usuario ID: {user_id}")

    connection = get_db_connection()
    if connection is None:
        logger.error("No se pudo conectar a la base de datos")
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    try:
        cursor = connection.cursor(dictionary=True)

        query = "SELECT id, respuesta, dificultad, lenguaje_id FROM ejercicios WHERE id = %s"
        cursor.execute(query, (question_id,))

        result = cursor.fetchone()
        logger.debug(f"Resultado de la consulta: {result}")

        if result:
            correct_answer = result["respuesta"]
            difficulty = result["dificultad"]
            language_id = result["lenguaje_id"]

            logger.info(f"Evaluando respuesta del usuario para el ejercicio ID: {result['id']}")
            logger.debug(f"Contenido del ejercicio: {correct_answer}")

            try:
                is_correct, test_results = evaluate_js_code(user_answer, question_id)
                
                if isinstance(test_results, list) and len(test_results) == 1 and "error" in test_results[0]:
                    logger.warning(f"Error en la evaluación: {test_results[0]['error']}")
                    return jsonify({
                        "is_correct": False,
                        "error": "Error en la evaluación del código",
                        "details": test_results[0]['error'],
                        "test_results": test_results
                    })

                logger.debug(f"Resultado de la evaluación: is_correct={is_correct}, test_results={test_results}")

                logger.info("Almacenando resultado del ejercicio")
                store_exercise_result(
                    user_id,
                    question_id,
                    user_answer,
                    is_correct,
                    time_taken,
                    language_id,
                    difficulty,
                )
                update_user_streak(user_id)
                update_daily_tracking(user_id, language_id, 1, time_taken)

                response_data = {"is_correct": is_correct, "test_results": test_results}
                logger.debug(f"Respuesta a enviar: {response_data}")
                return jsonify(response_data)

            except Exception as e:
                logger.error(f"Error al evaluar el código: {str(e)}")
                error_details = {
                    "error": "Error en la evaluación del código",
                    "details": str(e),
                    "exercise_id": result["id"],
                    "exercise_content": correct_answer,
                }
                if "Los casos de prueba no son JSON válido" in str(e):
                    test_cases_part = correct_answer.split("//TESTS//")[-1].strip()
                    error_details["test_cases"] = test_cases_part
                return jsonify(error_details), 500

        else:
            logger.warning(f"Pregunta no encontrada: {question_id}")
            return jsonify({"error": "Pregunta no encontrada"}), 404

    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}")
        logger.error(traceback.format_exc())
        return (
            jsonify(
                {
                    "error": "Error al procesar la respuesta",
                    "details": str(e),
                    "traceback": traceback.format_exc(),
                }
            ),
            500,
        )

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
        logger.info("Finalizando check_js_answer")

@js_bp.route("/get_js_performance", methods=["GET"])
def get_js_performance():
    user_id = request.args.get("user_id", 1, type=int)
    language_id = 3  # 3 para JavaScript
    performance_data = get_user_performance(user_id, language_id)

    if performance_data is None:
        return (
            jsonify(
                {"error": "No se pudo obtener el rendimiento del usuario en JavaScript"}
            ),
            500,
        )

    return jsonify(performance_data)

@js_bp.route("/get_recommendation", methods=["GET"])
def get_recommendation():
    user_id = request.args.get("user_id", type=int)
    if not user_id:
        return jsonify({"error": "Se requiere el ID del usuario"}), 400

    recommendation = generate_recommendation(user_id)
    return jsonify({"recommendation": recommendation})