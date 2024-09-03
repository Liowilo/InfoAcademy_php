# ejercicio_128.py
FUNCTION_NAME = "ordenar_lista"

def run_tests(user_function):
    tests = [
        {"input": ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],), "expected": [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]},
        {"input": ([9, 8, 7, 6, 5, 4, 3, 2, 1],), "expected": [1, 2, 3, 4, 5, 6, 7, 8, 9]},
        {"input": ([],), "expected": []}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]