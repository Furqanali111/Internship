
def calculate(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        if num2 == 0:
            print("Cannot divide by zero")
        return num1/num2
    else:
        print("Invalid operator")


def main():
    num1=float(input("Enter First number: "))
    operator=input("Enter the operator (+, -, *, /) you want to perform on the two numbers: ")
    num2=float(input("Enter Second number: "))

    print(f"{num1} {operator} {num2} = ",calculate(num1,num2,operator))

if __name__=="__main__":
    main()