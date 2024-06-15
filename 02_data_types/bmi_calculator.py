height = input("Enter your height: ")
weight = input("Enter your weight: ")

bmi = float(weight) / float(height) ** 2
print("Your BMI: " + str(int(bmi)))
