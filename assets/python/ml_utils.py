import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from database import get_db_connection

def preprocess_data(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener datos de seguimiento diario
    query = """
    SELECT lenguaje_id, AVG(ejercicios_completados) as promedio_ejercicios, 
           AVG(tiempo_total) as promedio_tiempo
    FROM seguimiento_diario
    WHERE usuario_id = %s
    GROUP BY lenguaje_id
    """
    cursor.execute(query, (user_id,))
    seguimiento = pd.DataFrame(cursor.fetchall())
    print("Datos de seguimiento:")
    print(seguimiento)

    # Obtener datos de racha
    query = "SELECT dias_consecutivos FROM racha_usuario WHERE usuario_id = %s"
    cursor.execute(query, (user_id,))
    racha_result = cursor.fetchone()
    racha = racha_result['dias_consecutivos'] if racha_result else 0
    print(f"Racha: {racha}")

    # Obtener tasa de aciertos por lenguaje
    query = """
    SELECT e.lenguaje_id, AVG(r.es_correcto) as tasa_aciertos
    FROM resultados r
    JOIN ejercicios e ON r.ejercicio_id = e.id
    WHERE r.usuario_id = %s
    GROUP BY e.lenguaje_id
    """
    cursor.execute(query, (user_id,))
    aciertos = pd.DataFrame(cursor.fetchall())
    print("Datos de aciertos:")
    print(aciertos)

    cursor.close()
    conn.close()

    # Combinar todos los datos
    if seguimiento.empty and aciertos.empty:
        print(f"No hay datos suficientes para el usuario {user_id}")
        return None, None

    data = pd.merge(seguimiento, aciertos, on='lenguaje_id', how='outer').fillna(0)
    data['racha'] = racha

    # Ajustar los lenguaje_id para que comiencen desde 0
    data['lenguaje_id'] = data['lenguaje_id'] - 1

    # Asegurarse de que tenemos datos para los 4 lenguajes
    for lenguaje_id in range(4):  # 0=HTML, 1=CSS, 2=JavaScript, 3=Python
        if lenguaje_id not in data['lenguaje_id'].values:
            new_row = pd.DataFrame({'lenguaje_id': [lenguaje_id], 
                                    'promedio_ejercicios': [0], 
                                    'promedio_tiempo': [0], 
                                    'tasa_aciertos': [0], 
                                    'racha': [racha]})
            data = pd.concat([data, new_row], ignore_index=True)

    print("Datos finales antes de la normalización:")
    print(data)

    # Normalizar los datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.drop('lenguaje_id', axis=1))

    print("Datos normalizados:")
    print(scaled_data)

    return scaled_data, data['lenguaje_id'].values

def create_model(input_shape):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_shape,)),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(4, activation='softmax')  # 4 salidas para HTML, CSS, JavaScript, Python
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model():
    # Obtener datos de todos los usuarios
    all_user_data = []
    all_user_labels = []
    
    for user_id in get_all_user_ids():
        data, labels = preprocess_data(user_id)
        if data is not None and labels is not None:
            all_user_data.extend(data)
            all_user_labels.extend(labels)
    
    if not all_user_data:
        print("No hay suficientes datos para entrenar el modelo.")
        return None

    X = np.array(all_user_data)
    y = np.array(all_user_labels)
    
    print(f"Rango de etiquetas: {np.min(y)} a {np.max(y)}")
    print(f"Etiquetas únicas: {np.unique(y)}")
    
    if len(np.unique(y)) < 2:
        print("No hay suficiente variedad en los datos para entrenar el modelo.")
        return None

    model = create_model(X.shape[1])
    history = model.fit(X, y, epochs=50, batch_size=32, validation_split=0.2, verbose=1)
    
    # Evaluar el modelo
    loss, accuracy = model.evaluate(X, y, verbose=0)
    print(f"Precisión del modelo en los datos de entrenamiento: {accuracy*100:.2f}%")
    
    model.save('recommendation_model.h5')
    return model, history

def generate_recommendation(user_id):
    model = load_model('recommendation_model.h5')
    data, _ = preprocess_data(user_id)
    if data is None:
        return "No hay suficientes datos para hacer una recomendación"
    
    # Asegúrate de que data sea 2D, incluso para un solo usuario
    if len(data.shape) == 1:
        data = data.reshape(1, -1)
    
    prediction = model.predict(data)
    print("Predicción del modelo:")
    print(prediction)
    languages = ['HTML', 'CSS', 'JavaScript', 'Python']
    recommended_language = languages[np.argmax(prediction[0])]
    return recommended_language

def get_all_user_ids():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    user_ids = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return user_ids