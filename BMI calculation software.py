#BMI Calculator 
import colorama
from colorama import init, Fore, Back, Style

init()  # Initialize colorama for colored text output

print(Back.GREEN + "Welcome to Anri Tsetskhladze's BMI calculation software.")
print(Back.CYAN)

try:
    weight = float(input("What's your weight in kilograms?: "))
    height = float(input("And what's your height in centimeters?: "))

    if height <= 0:
        raise ValueError("ERROR ")

except ValueError as e:
    print(Back.RED + f"Error: Invalid input: {e}")
    exit()

bmi = float("{0:.2f}".format(weight / ((height / 100) ** 2)))  # Calculate BMI using correct formula

print(Back.RED + f"Your current BMI is {bmi}")

if bmi <= 18.5:
    print(Back.RED + "Underweight or you are on a cut")
elif bmi <= 25:
    print(Back.GREEN + "Normal weight")
elif bmi <= 30:
    print(Back.YELLOW + "Overweight")
elif bmi <= 35:
    print(Back.ORANGE + "stage1 obese")
elif bmi <= 40:
    print(Back.RED + "stage 2 obese)")
else:
    print(Back.RED + "stage 3 obese)")

print("")
print(Style.RESET_ALL)

input("Press Enter to exit...")
