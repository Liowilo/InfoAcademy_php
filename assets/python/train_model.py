from ml_utils import train_model

if __name__ == '__main__':
    print("Iniciando entrenamiento del modelo...")
    trained_model = train_model()
    if trained_model:
        print("Entrenamiento completado. Modelo guardado como 'recommendation_model.h5'")
    else:
        print("No se pudo entrenar el modelo debido a la falta de datos suficientes.")