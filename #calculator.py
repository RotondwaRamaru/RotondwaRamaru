#calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("What do you want to calculate\n" "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

Select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if Select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif Select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
 
elif Select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
 
elif Select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
