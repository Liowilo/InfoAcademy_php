# ejercicio_133.py
FUNCTION_NAME = "cifrado_cesar"

def run_tests(user_function):
    tests = [
        {"input": ("HELLO", 3), "expected": "KHOOR"},
        {"input": ("abc", 1), "expected": "bcd"},
        {"input": ("XYZ", 3), "expected": "ABC"}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]