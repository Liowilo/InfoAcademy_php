import mysql.connector
from mysql.connector import Error
from datetime import date, timedelta

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

def store_exercise_result(user_id, exercise_id, user_answer, is_correct, time_taken, language_id, difficulty):
    try:
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        
        query = """
        INSERT INTO resultados (usuario_id, ejercicio_id, respuesta_usuario, es_correcto, tiempo_resolucion, fecha_realizacion, lenguaje_id, dificultad)
        VALUES (%s, %s, %s, %s, %s, NOW(), %s, %s)
        """
        
        cursor.execute(query, (user_id, exercise_id, user_answer, is_correct, time_taken, language_id, difficulty))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
    except Error as e:
        print(f"Error storing exercise result: {e}")
        return False

def get_user_performance(user_id, language_id=1):
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
            AVG(dificultad) as dificultad_promedio
        FROM resultados
        WHERE usuario_id = %s AND lenguaje_id = %s
        """
        
        cursor.execute(query, (user_id, language_id))
        result = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        # Convertir explícitamente los valores a float o int según sea necesario
        if result:
            result['ejercicios_completados'] = int(result['ejercicios_completados']) if result['ejercicios_completados'] is not None else 0
            result['tasa_aciertos'] = float(result['tasa_aciertos']) if result['tasa_aciertos'] is not None else 0
            result['tiempo_promedio'] = float(result['tiempo_promedio']) if result['tiempo_promedio'] is not None else 0
            result['dificultad_promedio'] = float(result['dificultad_promedio']) if result['dificultad_promedio'] is not None else 0
        
        return result
    except Error as e:
        print(f"Error getting user performance: {e}")
        return None
    
def update_user_streak(user_id):
    try:
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor(dictionary=True)
        
        # Obtener la última actualización de racha del usuario
        query = "SELECT dias_consecutivos, ultima_actualizacion FROM racha_usuario WHERE usuario_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()
        
        today = date.today()
        
        if result:
            last_update = result['ultima_actualizacion']
            current_streak = result['dias_consecutivos']
            
            if today - last_update == timedelta(days=1):
                # El usuario ha mantenido su racha
                new_streak = current_streak + 1
            elif today == last_update:
                # El usuario ya ha actualizado hoy, no hacemos nada
                return True
            else:
                # La racha se ha roto
                new_streak = 1
        else:
            # Primera racha del usuario
            new_streak = 1
        
        # Actualizar o insertar la nueva racha
        query = """
        INSERT INTO racha_usuario (usuario_id, dias_consecutivos, ultima_actualizacion)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        dias_consecutivos = VALUES(dias_consecutivos),
        ultima_actualizacion = VALUES(ultima_actualizacion)
        """
        cursor.execute(query, (user_id, new_streak, today))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
    except Error as e:
        print(f"Error updating user streak: {e}")
        return False
    
def update_daily_tracking(user_id, language_id, exercises_completed, total_time):
    try:
        conn = get_db_connection()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        
        today = date.today()
        
        query = """
        INSERT INTO seguimiento_diario (usuario_id, fecha, ejercicios_completados, tiempo_total, lenguaje_id)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        ejercicios_completados = ejercicios_completados + VALUES(ejercicios_completados),
        tiempo_total = tiempo_total + VALUES(tiempo_total)
        """
        
        cursor.execute(query, (user_id, today, exercises_completed, total_time, language_id))
        conn.commit()
        
        cursor.close()
        conn.close()
        
        return True
    except Error as e:
        print(f"Error updating daily tracking: {e}")
        return False