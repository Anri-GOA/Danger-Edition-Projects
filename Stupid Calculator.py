#Stupid Calculator

a =float(input("Write First Symbol: "))
b =float(input("Write Second Symbol: "))

operation = input("What To Do? (+, -, / , *): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "/":
    result = a / b
elif operation == "*":
    result = a * b

print(f"result is: {result}")
