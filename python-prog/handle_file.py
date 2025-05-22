# f = open('data.txt','r')
# #content = f.read()
# for line in f:
#     print(line)

# f.close()

# f = open('data.txt','w')
# f.write("this is my first line!! \n")
# f.write("this is my 2nd line!! \n")
# f.close()

# f = open('data.txt','a')
# f.write("this is my 1st appended line!! \n")
# f.write("this is my 2nd appended line!! \n")
# f.close()

with open('data.txt','r') as f:
    print(f.read())