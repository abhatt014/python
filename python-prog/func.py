# def print_hello():
#     print("Hello World")

# def add_num(a,b):
#     a = int(a)
#     b = int(b)
#     c = a +b
#     return c

# res = add_num(10,4)
# print(f"result: {res}")

# def print_msg(msg):
# 	print(msg)
	
# print_msg("this is devops class")

# def add_num(num1,num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     result = num1 + num2
#     return result
# res = add_num(10,5)
# print(f"addition : {res}")

# function inside another function
def print_msg_and_add(num1,num2):
    print("hello")
    def add_num(num1,num2):
        result = num1 + num2
        return result
    res = add_num(num1,num2)
    print(res)

if __name__ == "__main__":
    print_msg_and_add(10,5)
  