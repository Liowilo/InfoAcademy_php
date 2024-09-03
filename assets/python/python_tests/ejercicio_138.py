# ejercicio_138.py
FUNCTION_NAME = "comprimir"

def run_tests(user_function):
    tests = [
        {"input": ("AABBBCCCC",), "expected": "A2B3C4"},
        {"input": ("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB",), "expected": "W12BW12B3W24B"},
        {"input": ("",), "expected": ""},
        {"input": ("AABBBCCCCAAA",), "expected": "A2B3C4A3"}
    ]
    return [{"input": test["input"], "expected": test["expected"],
             "result": user_function(*test["input"]),
             "passed": user_function(*test["input"]) == test["expected"]}
            for test in tests]