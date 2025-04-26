import random
import string
import traceback

def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_int():
    return random.randint(-1000, 1000)

def random_float():
    return random.uniform(-1000, 1000)

# Example functions to fuzz (replace with your actual KubeSec functions if you want)
def func1(x):
    return x.upper()

def func2(x):
    return int(x)

def func3(x, y):
    return x / y

def func4(x):
    return [i for i in x]

def func5(x):
    return {k: v for k, v in enumerate(x)}

functions_to_fuzz = [
    (func1, [random_string]),
    (func2, [random_string]),
    (func3, [random_float, random_float]),
    (func4, [random_string]),
    (func5, [random_string])
]

def main():
    with open("bugs_found.txt", "w") as f:
        for i in range(100):  # 100 fuzzing attempts
            for func, generators in functions_to_fuzz:
                try:
                    inputs = [g() for g in generators]
                    result = func(*inputs)
                except Exception as e:
                    f.write(f"Error in {func.__name__} with inputs {inputs}\n")
                    f.write(traceback.format_exc())
                    f.write("\n---\n")

if __name__ == "__main__":
    main()
