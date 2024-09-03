# ejercicio_125.py
FUNCTION_NAME = "es_palindromo"

def run_tests(user_function):
    tests = [
        {"input": ("Ana",), "expected": True},
        {"input": ("Python",), "expected": False},
        {"input": ("A man a plan a canal Panama",), "expected": True}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]