
print("Welcome to PythonCalc 🧮")
n1 = int(input("Enter first number:"))
operator = input("Enter operator(+, -, *, /):")
n2 = int(input("Enter second number:"))

if operator == "+":
    print(f"Result:", n1+n2)

elif operator == "-":
    print(f"Result:" , n1-n2)

elif operator == "*":
    print(f"Result:" , n1*n2)

elif operator == "/":
    print(f"Result:" , n1/n2)

else:
    print("Invalid Operator")