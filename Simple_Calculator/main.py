operator = input("Enter an operator")
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if operator == "+":
    print(f"Answer is {(num1 + num2)}")
elif operator == "-":
    print(f"Answer is {num1 - num2}")
elif operator == "*":
    print(f"Answer is {num1 * num2}")
elif operator == "/":
    print(f"Answer is {num1 / num2}")