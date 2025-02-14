# test.py

from main import sum2, subtract, multiply, divide

def test_sum2():
    assert sum2(15, 8) == 23
    assert sum2(0, 0) == 0
    assert sum2(-1, 1) == 0

def test_subtract():
    assert subtract(15, 8) == 7
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(3, 5) == 15
    assert multiply(0, 10) == 0
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(10, 2) == 5
    assert divide(0, 1) == 0
    assert divide(-10, 2) == -5

    # Проверка деления на ноль
    try:
        divide(10, 0)
        assert False, "Ошибка: Функция должна была вызвать исключение при делении на ноль"
    except ValueError:
        pass

if __name__ == "__main__":
    import pytest
    pytest.main()