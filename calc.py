operator = input("Enter operator: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match operator:
    case "+":
        print(f"{num1} + {num2} = ",num1 + num2)
    case "-":
        print(f"{num1} - {num2} = ",num1 - num2)
    case "*":
        print(f"{num1} * {num2} = ",num1 * num2)
    case "/":
        print(f"{num1} / {num2} = ",num1 / num2)