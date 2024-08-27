import json
import logging
import tempfile
import subprocess
import os

logger = logging.getLogger(__name__)

def evaluate_js_code(user_code, correct_answer):
    logger.info("Iniciando evaluación de código JavaScript")
    logger.debug(f"Código del usuario: {user_code}")
    logger.debug(f"Respuesta correcta: {correct_answer}")

    try:
        function_code, test_cases = parse_js_answer(correct_answer)
    except Exception as e:
        logger.error(f"Error al parsear la respuesta correcta: {str(e)}")
        return False, [{"error": f"Error en la configuración del ejercicio: {str(e)}"}]

    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.js', delete=False) as temp_file:
            temp_file.write(user_code + '\n\n')
            temp_file.write('const testCases = ' + json.dumps(test_cases) + ';\n')
            temp_file.write('''
                const results = [];
                try {
                    testCases.forEach((testCase, index) => {
                        try {
                            const result = eval(testCase.input);
                            results.push({
                                testCase: index,
                                input: testCase.input,
                                expected: JSON.stringify(testCase.expected),
                                result: JSON.stringify(result),
                                passed: JSON.stringify(result) === JSON.stringify(testCase.expected)
                            });
                        } catch (error) {
                            results.push({
                                testCase: index,
                                input: testCase.input,
                                expected: JSON.stringify(testCase.expected),
                                result: JSON.stringify(String(error)),
                                passed: false
                            });
                        }
                    });
                } catch (error) {
                    results.push({
                        error: JSON.stringify(String(error))
                    });
                }
                console.log(JSON.stringify(results));
            ''')
            temp_file_name = temp_file.name

        logger.debug(f"Archivo temporal creado: {temp_file_name}")

        result = subprocess.run(['node', temp_file_name], capture_output=True, text=True, timeout=5)
        logger.debug(f"Resultado de subprocess: returncode={result.returncode}, stdout={result.stdout}, stderr={result.stderr}")
        
        if result.returncode != 0:
            logger.warning(f"Error en la ejecución del código: {result.stderr}")
            return False, [{"error": "Error de sintaxis en el código", "details": result.stderr}]
        
        test_results = json.loads(result.stdout)
        all_passed = all(result.get('passed', False) for result in test_results if 'passed' in result)
        logger.info(f"Evaluación completada. Todos los tests pasados: {all_passed}")
        return all_passed, test_results
    
    except subprocess.TimeoutExpired:
        logger.error("Tiempo de ejecución excedido")
        return False, [{"error": "El código tardó demasiado en ejecutarse. Verifica si hay bucles infinitos."}]
    except json.JSONDecodeError as e:
        logger.error(f"Error al decodificar JSON de los resultados: {str(e)}")
        return False, [{"error": f"Error al procesar los resultados: {str(e)}"}]
    except Exception as e:
        logger.error(f"Error inesperado: {str(e)}", exc_info=True)
        return False, [{"error": f"Error inesperado: {str(e)}"}]
    finally:
        if 'temp_file_name' in locals():
            os.unlink(temp_file_name)
            logger.debug(f"Archivo temporal eliminado: {temp_file_name}")

def parse_js_answer(answer):
    logger.debug(f"Parseando respuesta: {answer}")
    parts = answer.split('//TESTS//')
    if len(parts) != 2:
        raise ValueError(f"La respuesta no tiene el formato correcto (código + //TESTS// + casos de prueba). Partes encontradas: {len(parts)}")

    function_code = parts[0].strip()
    test_cases_str = parts[1].strip()
    
    logger.debug(f"Código de la función: {function_code}")
    logger.debug(f"Casos de prueba (sin procesar): {test_cases_str}")

    try:
        # Intenta parsear directamente
        test_cases = json.loads(test_cases_str)
    except json.JSONDecodeError as e:
        logger.warning(f"Error al decodificar JSON directamente: {str(e)}")
        
        # Intenta limpiar el string y parsear nuevamente
        clean_test_cases_str = test_cases_str.replace('\n', '').replace('\r', '').replace(' ', '')
        try:
            test_cases = json.loads(clean_test_cases_str)
        except json.JSONDecodeError as e:
            logger.error(f"Error al decodificar JSON de los casos de prueba después de limpiar: {str(e)}")
            logger.debug(f"Contenido problemático (limpio): {clean_test_cases_str}")
            raise ValueError(f"Los casos de prueba no son JSON válido. Error: {str(e)}. Contenido limpio: {clean_test_cases_str[:100]}...")

    if not isinstance(test_cases, list):
        raise ValueError(f"Los casos de prueba deben ser una lista. Tipo actual: {type(test_cases)}")

    return function_code, test_cases