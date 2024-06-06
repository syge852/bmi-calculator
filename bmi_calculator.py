# bmi_calculator.py

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    print("BMI Calculator")
    
    # Get user input
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Display result
    print(f"Your BMI is: {bmi:.2f}")

    # Determine BMI category
    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obesity")

if __name__ == "__main__":
    main()
