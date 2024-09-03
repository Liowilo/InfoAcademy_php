# ejercicio_120.py
FUNCTION_NAME = "invertir_lista"

def run_tests(user_function):
    tests = [
        {"input": ([1, 2, 3],), "expected": [3, 2, 1]},
        {"input": (["a", "b", "c"],), "expected": ["c", "b", "a"]},
        {"input": ([],), "expected": []}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]
