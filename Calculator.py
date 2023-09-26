#Python Exercise - Let's Make a Calculator!

#Defining functions for add, subtract, multiply, and divide
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

#Importing time module for UX
import time

#Defining main function, and printing message w/ time delay to simulate boot-up (UX)
def main():
    print("Calculator Starting...")

    time.sleep(3)
#Creating loop for repeated calculations (UX)
    #Loop start
    while True:
        #Prompts user for operator input
        print("Select Operation:")
        print("1. Add 2. Sub 3. Mul 4. Div")
        #Operation choice by user
        choice = input("Enter choice (1/2/3/4): ")
        #Using try and except blocks to catch errors
        try:
            #Get user input for both numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if choice == '1':
                result = add(num1, num2)
                print("Result:", result)
            elif choice == '2':
                result = sub(num1, num2)
                print("Result:", result)
            elif choice == '3':
                result = mul(num1, num2)
                print("Result:", result)
            elif choice == '4':
                if num2 == 0:
                    print("Error: Divided by zero")
                else:
                    result = div(num1, num2)
                    print("Result:", result)
            else: print("Invalid input. Please enter a valid choice (1/2/3/4).")
        except ValueError:
            print('Invalid input. Please enter numeric values for num1 and num2.')
        another_calculation = input("Do you want to perform another calculation? (yes/no)")
        #Accounts for both 'yes' and 'y' as acceptable inputs for running program again, but breaks loop otherwise
        if another_calculation.lower() not in ('yes', 'y'):
            print("\nTerminating Session...\n")
            time.sleep(3)
            break
        #Loop end
if __name__ == "__main__":
    main()