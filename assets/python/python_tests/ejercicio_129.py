# ejercicio_129.py
FUNCTION_NAME = "eliminar_duplicados"

def run_tests(user_function):
    tests = [
        {"input": ([1, 2, 2, 3, 4, 3, 5],), "expected": [1, 2, 3, 4, 5]},
        {"input": (["a", "b", "a", "c", "c"],), "expected": ["a", "b", "c"]},
        {"input": ([],), "expected": []}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]  