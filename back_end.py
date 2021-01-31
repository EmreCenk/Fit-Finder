

#Variables
get_height = 0.0
get_weight = 0.0
body_mass_index = 0.0


#Start:
    print("Welcome to my BMI calculator!")
    print("If you can tell me your weight and height")
    print("I can tell you your Body Mass Index")
    print("Let's Go!\n")

def main():
    bmi_intro()    
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = float(input("Please enter your height in inches. "))
    get_weight = float(input("Please enter your weight in pounds. "))
    body_mass_index = (get_weight * 703) / (get_height ** 2)
    if body_mass_index < 18.5:
        return("A person with a BMI of " + str(body_mass_index ) + " is underwieght ")
    elif body_mass_index < 24.9:
        return("A person with a BMI of " + str(body_mass_index ) + " is normal weight ")
    else:
        return("A person with a BMI of " + str(body_mass_index ) + " is overweight ")

