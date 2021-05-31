a = 1  
b = 0  
print (b)  
for i in range(0,10):  
    c = b  
    b = a  
    a = c + b  
    print(a)
