#try-except block
try:
   f = open('dat.txt', 'r')
   print(f.read)    
except FileNotFoundError as e:
    print(f"An error occured: File not found") 
