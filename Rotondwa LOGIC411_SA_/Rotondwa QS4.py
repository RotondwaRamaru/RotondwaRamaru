# Python program to convert a list of Fahrenheit measurements to a list of Celsius measurements
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9 

f_list = [32, 70, 100, 212] 
c_list = [] 

for f in f_list: 
    c = fahrenheit_to_celsius(f) 
    c_list.append(c) 
    
print(c_list) 