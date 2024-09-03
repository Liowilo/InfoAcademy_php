# ejercicio_131.py
FUNCTION_NAME = "a_romano"

def run_tests(user_function):
    tests = [
        {"input": (4,), "expected": "IV"},
        {"input": (9,), "expected": "IX"},
        {"input": (37,), "expected": "XXXVII"},
        {"input": (944,), "expected": "CMXLIV"}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]