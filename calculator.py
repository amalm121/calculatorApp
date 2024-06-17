def sum_function(num1,num2):
    sum = num1 + num2
    return sum
print("-"*10 +"Calculator"+"-"*10)
print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division \n5.Exit")
option = int(input("Enter an option :"))
if option==1:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    sum = sum_function(num1,num2)
    print(f"Sum of {num1} and {num2} is {sum}")
