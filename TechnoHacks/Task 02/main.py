# Temperature converter

def converter(scale):
    if scale=='cl':
        val = float(input("Enter Fahrenheit value: "))
        C = (val - 32) * 5 / 9
        print("Celsius value = ", C)
    elif scale=='fe':
        val = float(input("Enter Celsius value: "))
        F = (val * (9 / 5)) + 32
        print("Fahrenheit value = ", F)

if __name__=="__main__":
    print("Welcome to temperature converter")
    scale=input("Please Chose the scale you want to convert to Fahrenheit(fe) Celsius(cl): ")
    if scale=="fe" or scale=="cl":
        result=converter(scale)
    else:
        print("Invalid Scale")
