import importlib.util
import os
import logging
import traceback
import sys

logging.basicConfig(filename="python_evaluator.log", level=logging.DEBUG)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PYTHON_TESTS_DIR = os.path.join(BASE_DIR, "python", "python_tests")

def check_file_permissions(file_path):
    if os.path.exists(file_path):
        logger.info(f"El archivo {file_path} existe.")
        logger.info(f"Permiso de lectura: {os.access(file_path, os.R_OK)}")
        logger.info(f"Permiso de escritura: {os.access(file_path, os.W_OK)}")
        logger.info(f"Permiso de ejecución: {os.access(file_path, os.X_OK)}")
    else:
        logger.error(f"El archivo {file_path} no existe.")

def evaluate_python_code(user_code, exercise_id):
    test_file_path = os.path.join(PYTHON_TESTS_DIR, f"ejercicio_{exercise_id}.py")
    logger.info(f"Evaluando ejercicio {exercise_id}")
    logger.info(f"Ruta del archivo de prueba: {test_file_path}")
    
    check_file_permissions(test_file_path)

    if not os.path.exists(test_file_path):
        logger.error(f"No se encontró el archivo de pruebas: {test_file_path}")
        return False, [{"error": f"No se encontró el archivo de pruebas para el ejercicio {exercise_id}"}]

    try:
        spec = importlib.util.spec_from_file_location(f"ejercicio_{exercise_id}", test_file_path)
        test_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_module)

        # Ejecutar el código del usuario
        local_vars = {}
        try:
            exec(user_code, local_vars)
        except Exception as e:
            logger.error(f"Error al ejecutar el código del usuario: {str(e)}")
            return False, [{"error": f"Error de sintaxis o respuesta inválida: {str(e)}"}]

        if not hasattr(test_module, 'FUNCTION_NAME'):
            logger.error("No se especificó FUNCTION_NAME en el archivo de pruebas")
            return False, [{"error": "Error en la configuración de las pruebas: FUNCTION_NAME no especificado"}]

        if test_module.FUNCTION_NAME not in local_vars:
            logger.error(f"No se encontró la función '{test_module.FUNCTION_NAME}'")
            return False, [{"error": f"No se encontró la función '{test_module.FUNCTION_NAME}'. Asegúrate de nombrar tu función correctamente."}]

        user_function = local_vars[test_module.FUNCTION_NAME]

        # Ejecutar las pruebas
        test_results = test_module.run_tests(user_function)
        
        # Verificar el formato de los resultados
        if not isinstance(test_results, list):
            logger.error("El resultado de las pruebas no es una lista")
            return False, [{"error": "Error en el formato de los resultados de las pruebas"}]

        for result in test_results:
            if not all(key in result for key in ["input", "expected", "result", "passed"]):
                logger.error("Formato incorrecto en los resultados de las pruebas")
                return False, [{"error": "Error en el formato de los resultados de las pruebas"}]

        all_passed = all(result["passed"] for result in test_results)

        logger.info(f"Evaluación completada. Todas las pruebas pasaron: {all_passed}")
        return all_passed, test_results

    except Exception as e:
        logger.exception(f"Error inesperado al evaluar el código: {str(e)}")
        return False, [{"error": f"Error inesperado al evaluar el código: {str(e)}", "traceback": traceback.format_exc()}]