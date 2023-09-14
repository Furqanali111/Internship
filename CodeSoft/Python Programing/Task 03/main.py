import random
import string

def passwordgen(length):
    data=string.ascii_letters+string.digits
    password=''.join(random.choices(data,k=length))
    return password

if __name__=="__main__":
    try:
        length=int(input("Enter the desired length of the password: "))
        print("Your generated  password is :",passwordgen(length))
    except ValueError:
        print("Enter a integer")
        try:
            length = int(input("Enter the desired length of the password:  "))
            print("your generated  password is :",passwordgen(length))
        except ValueError:
            print("Try Again")
