# 1.	Rewrite the following print statement using an f-string: 
item = "laptop"
price = 1200
# print("The " + item + " costs $" + str(price) + ".")

msg = f"the {item} costs ${price} ."
print(msg)
