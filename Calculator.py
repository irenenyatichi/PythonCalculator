def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def division(x, y):
    return x / y


def multiplication(x, y):
    return x * y


def modulus(x, y):
    return x % y


def exp(x, y):
    return x // y


print("select operation")
print("1.addition")
print("2.subtraction")
print("3.division")
print("4.multiplication")
print("5.modulus")
print("6.whole number division")

while True:
    choice = input("Enter choice(1/2/3/4/5/6): ")
    break
if choice in ('1', '2', '3', '4', '5', '6'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

if choice == '1':
    print(num1, "+", num2, "=", addition(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtraction(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", division(num1, num2))
elif choice == '5':
    print(num1, "%", num2, "=", modulus(num1, num2))
elif choice == '6':
    print(num1, "//", num2, "=", exp(num1, num2))

else:
    print("Invalid Input")
