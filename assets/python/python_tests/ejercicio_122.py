# ejercicio_122.py
FUNCTION_NAME = "maximo_de_tres"

def run_tests(user_function):
    tests = [
        {"input": (1, 2, 3), "expected": 3},
        {"input": (5, 5, 5), "expected": 5},
        {"input": (-1, -5, 0), "expected": 0}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]