Task = input("What do you want + or - : or / or * or % or ** or //. Type what you want: ")
if(Task == "+"): 
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1+number2)
elif(Task == "-"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1-number2)
elif(Task == "/"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1/number2)  
elif(Task == "*"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1*number2) 
elif(Task == "%"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1%number2)
elif(Task == "**"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1**number2) 
elif(Task == "//"):
    number1 = int(input("Input first number: "))
    number2 = int(input("Input second number: "))
    print(number1//number2)  
else:
    print("Wrong symbol")