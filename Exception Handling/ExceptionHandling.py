

try:
    print("Exception Handling Exaomple")
    num1,num2 = input("Enter num1 & num2: ").split()
    num3 = int(num1)/int(num2)
    
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print("the Result is ", num3)
