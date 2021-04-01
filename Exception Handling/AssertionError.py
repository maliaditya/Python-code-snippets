num1 = 2
num2 = 4
try:
    assert num1 == num2
except AssertionError as e:
    print("Assertion Error")