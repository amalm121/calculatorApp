def sum_function(num1,num2):
    sum = num1 + num2
    return sum
def diff_function(num1,num2):
    diff = num1 - num2
    return diff
def mul_function(num1,num2):
    mul = num1 * num2
    return mul
def div_function(num1,num2):
    div = num1/num2
    return div
def percent_function(part,whole):
    div = div_function(part,whole)
    percent = mul_function(div,100)
    return percent
def calculator_function():
    print("-"*10 +"Calculator"+"-"*10)
    print("1. Addition\n2. Substraction\n3. Multiplication\n4. Division\n5.Percentage")
    option = int(input("Enter an option :"))
    if option==1:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        sum = sum_function(num1,num2)
        print(f"Sum of {num1} and {num2} is {sum}")
    if option==2:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        diff = diff_function(num1,num2)
        print(f"Difference of {num1} and {num2} is {diff}")
    if option==3:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        mul = mul_function(num1,num2)
        print(f"Difference of {num1} and {num2} is {mul}")
    if option==4:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        div = div_function(num1,num2)
        print(f"Difference of {num1} and {num2} is {div}")
    if option==5:
        part = float(input("Enter the part : "))
        whole = float(input("Enter the whole : "))
        percent = percent_function(part,whole)
        print("Percentage :",percent)


calculator_function()

