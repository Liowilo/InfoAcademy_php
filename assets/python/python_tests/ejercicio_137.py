# ejercicio_137.py
FUNCTION_NAME = "mochila"

def run_tests(user_function):
    tests = [
        {"input": ([10, 20, 30], [60, 100, 120], 50), "expected": (220, [1, 2])},
        {"input": ([5, 4, 6, 3], [10, 40, 30, 50], 10), "expected": (90, [1, 3])}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]