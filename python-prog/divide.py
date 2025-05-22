try:
    a = 10
    b = 10
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print("Division by zero not allowd")    
finally:
    print("program execution completed")    