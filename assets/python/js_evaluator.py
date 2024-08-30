import json
import os
import subprocess
import tempfile
import logging

def check_file_permissions(file_path):
    if os.path.exists(file_path):
        print(f"El archivo {file_path} existe.")
        print(f"Permiso de lectura: {os.access(file_path, os.R_OK)}")
        print(f"Permiso de escritura: {os.access(file_path, os.W_OK)}")
        print(f"Permiso de ejecución: {os.access(file_path, os.X_OK)}")
    else:
        print(f"El archivo {file_path} no existe.")

# Usa esta función antes de intentar leer el archivo
check_file_permissions('C:\\xampp\\htdocs\\InfoAcademy\\assets\\python\\js_tests\\ejercicio_102.js')

# Configurar logging
logging.basicConfig(filename="js_evaluator.log", level=logging.DEBUG)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS_TESTS_DIR = os.path.join(BASE_DIR, "python", "js_tests")


def evaluate_js_code(user_code, exercise_id):
    # Ruta al archivo de pruebas
    test_file_path = os.path.join(JS_TESTS_DIR, f"ejercicio_{exercise_id}.js")
    logging.info(f"Evaluando ejercicio {exercise_id}")
    logging.info(f"Ruta del archivo de prueba: {test_file_path}")
    logging.info(f"El archivo existe: {os.path.exists(test_file_path)}")

    if not os.path.exists(test_file_path):
        logging.error(f"No se encontró el archivo de pruebas: {test_file_path}")
        return False, [
            {
                "error": f"No se encontró el archivo de pruebas para el ejercicio {exercise_id}"
            }
        ]

    test_file_path_normalized = test_file_path.replace("\\", "/")
    with tempfile.NamedTemporaryFile(
        mode="w+", suffix=".js", delete=False
    ) as temp_file:
        temp_file.write(
            f"""
    const ejercicio = require('{test_file_path_normalized}');
let userFunction;
try {{
    userFunction = {user_code};
    if (typeof userFunction !== 'function') {{
        throw new Error('La respuesta no es una función válida');
    }}
}} catch (error) {{
    console.log(JSON.stringify([{{
        error: 'Error de sintaxis o respuesta invalida',
        details: error.message
    }}]));
    process.exit(1);
}}

const resultados = ejercicio.casos.map(caso => {{
    try {{
        const resultado = userFunction(caso.input);
        return {{
            input: caso.input,
            expected: caso.expected,
            result: resultado,
            passed: JSON.stringify(resultado) === JSON.stringify(caso.expected)
        }};
    }} catch (error) {{
        return {{
            input: caso.input,
            expected: caso.expected,
            result: error.message,
            passed: false
        }};
    }}
}});

console.log(JSON.stringify(resultados));
        """
        )
        temp_file_name = temp_file.name

    try:
        # Ejecutar el archivo temporal con Node.js
        result = subprocess.run(
            ["node", temp_file_name], capture_output=True, text=True, timeout=5
        )

        if result.returncode != 0:
            error_output = json.loads(result.stdout)
            return False, error_output

        # Parsear los resultados
        test_results = json.loads(result.stdout)
        all_passed = all(r["passed"] for r in test_results)

        return all_passed, test_results

    except subprocess.TimeoutExpired:
        return False, [{"error": "La ejecución del código tardó demasiado tiempo."}]
    except json.JSONDecodeError:
        return False, [{"error": "Error al procesar los resultados de las pruebas."}]
    except Exception as e:
        return False, [{"error": f"Error inesperado: {str(e)}"}]
    finally:
        # Eliminar el archivo temporal
        os.unlink(temp_file_name)
