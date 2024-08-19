from ml_utils import generate_recommendation, preprocess_data

def test_model():
    user_id = 4  # El único usuario con datos
    
    print(f"\nProcesando usuario {user_id}")
    data, labels = preprocess_data(user_id)
    if data is not None and labels is not None:
        print("Datos procesados:")
        print(data)
        print("Etiquetas:")
        print(labels)
        recommendation = generate_recommendation(user_id)
        print(f"Para el usuario {user_id}, la recomendación es: {recommendation}")
    else:
        print(f"No se pudo generar una recomendación para el usuario {user_id}")

if __name__ == "__main__":
    test_model()