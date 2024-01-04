def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462

def pounds_to_kilograms(pounds):
    return pounds / 2.20462

def main():
    print("Unit Converter")
    print("_____________________________________________________________________________")
    print("1. Temperature Converter (Celsius to Fahrenheit and vice versa)")
    print("2. Length Converter (Meters to Feet and vice versa)")
    print("3. Weight Converter (Kilograms to Pounds and vice versa)")
    print("-------------------------------------------------------------------------")
    choice = input("Enter the number corresponding to your choice (1/2/3): ")

    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if choice == 1:
        try:
            celsius = float(input("Enter the temperature in Celsius: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.") # here the .2f is to get a precise float value upto two numbers after point

    elif choice == 2:
        try:
            meters = float(input("Enter the length in meters: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        feet = meters_to_feet(meters)
        print(f"{meters} meters is equal to {feet:.2f} feet.")   

    elif choice == 3:
        try:
            kilograms = float(input("Enter the weight in kilograms: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} kilograms is equal to {pounds:.2f} pounds.")

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
