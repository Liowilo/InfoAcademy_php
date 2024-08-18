import mysql.connector
from mysql.connector import Error

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

def store_exercise_result(user_id, exercise_id, user_answer, is_correct, time_taken):
    try:
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        
        query = """
        INSERT INTO resultados (usuario_id, ejercicio_id, respuesta_usuario, es_correcto, tiempo_resolucion, fecha_realizacion)
        VALUES (%s, %s, %s, %s, %s, NOW())
        """
        
        cursor.execute(query, (user_id, exercise_id, user_answer, is_correct, time_taken))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
    except Error as e:
        print(f"Error storing exercise result: {e}")
        return False

def get_user_performance(user_id, language_id):
    try:
        conn = get_db_connection()
        if conn is None:
            return None
        
        cursor = conn.cursor(dictionary=True)
        
        query = """
        SELECT 
            COUNT(*) as ejercicios_completados,
            AVG(CASE WHEN es_correcto THEN 1 ELSE 0 END) as tasa_aciertos,
            AVG(tiempo_resolucion) as tiempo_promedio,
            AVG(e.dificultad) as dificultad_promedio
        FROM resultados r
        JOIN ejercicios e ON r.ejercicio_id = e.id
        WHERE r.usuario_id = %s AND e.lenguaje_id = %s
        """
        
        cursor.execute(query, (user_id, language_id))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        return result
    except Error as e:
        print(f"Error getting user performance: {e}")
        return None