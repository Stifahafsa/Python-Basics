for i in range (100):
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    operation = input("Choose Operations : + , - , * , / or ** :  ")

    if operation == '+' :
        res = num1 + num2
    elif operation == '-':
        res = num1 - num2
    elif operation == '*':
        res = num1 * num2
    elif operation == '**':
        res = num1 ** num2
    elif operation == '/':
        if num2 == 0 :
            print("Error, dividing by 0 is not possible")
        else:
            res = num1 / num2 
    
    else:
        print("Invalid Operations, please choose one from the list (+, -, *, /,**)")
    

    print(f"the result is {res}")