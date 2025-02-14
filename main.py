# main.py

from calculator import calculate

def sum2(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def main():
    print("Введите математическое выражение для вычисления (например, 2 + 2, 3 * 5, 10 / 2 )")
    print("Для выхода введите 'q'.")

    while True:
        expression = input("Введите выражение: ")

        if expression.lower() == 'q':
            print("выход из программы.")
            break

        result = calculate(expression)
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()