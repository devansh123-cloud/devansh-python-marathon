

print("--- PyCalculator Intermediate ---")
while True:
    operation = input("Choose operation (+, -, *, /) or type 'exit' to quit : ").strip()
    
    if operation == "exit":
        print("Thanks for using PyCalculator")
        break
        
    
    if operation not in ["+", "-", "/", "*"]:
        print("Invalid operation. Try again.")
        
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid number \n")
        continue
    
    if operation == "+":
        result = num1 + num2
    
    elif operation == "-":
        result = num1 - num2
    
    elif operation == "/":
        result = num1 / num2
        
        if num2 == 0:
            print("❌ Cannot divide by zero.\n")
    
    elif operation == "*":
        result = num1 * num2
    
    print(f"Result {result} ✅\n")
        