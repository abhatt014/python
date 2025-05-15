# print values from 0 to 100
# data = ""
# for i in range(101): #0...100
# 	if i == 0:
# 		print("below are the values from 1 to 100 \n")
# 	elif i == 100:
# 		data = data + str(i) 
	
# 	else:
# 		data = data + str(i) + ","


# print(data)

# fruits = ["apple", "banana"]
# for fruit in fruits:
#     print(fruit)


# print("hello user ",userdata['name'],"\n")
# print(f"your age is {userdata['age']+1}")
# print("you obtained  ",userdata['grade']," grade \n")   


# for key,value in userdata.items():
# 	print(key,value)

		
userdata = {"name":"alice","age":20,"grade":"C"}

# # Accessing keys and values

# for key in userdata:
#     value = userdata[key]
#     print(f"Key: {key}, Value: {value}") 
  


# Accessing only values

# for value in userdata.values():
#     print(f"Value: {value}") 

# # Accessing key-value pairs (items) - Most Pythonic way

for k, v in userdata.items():
    print(f"Key: {k} | Value: {v}") 




	


