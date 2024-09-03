# ejercicio_132.py
FUNCTION_NAME = "validar_parentesis"

def run_tests(user_function):
    tests = [
        {"input": ("()",), "expected": True},
        {"input": ("()()",), "expected": True},
        {"input": ("(()())",), "expected": True},
        {"input": ("((",), "expected": False},
        {"input": (")(", ), "expected": False}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]