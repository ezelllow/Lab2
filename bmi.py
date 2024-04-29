
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
#Add code here to calculate BMI
    bmi = weight/(height*height)
#Add code here to display calculate BMI
    print("Your BMI is: " + str(bmi))
    if bmi<18.5:
        print("You are underweight.")
    elif bmi>=18.5 or bmi<=25:
        print("You are normal weight.")
    else:
        print("You are overweight.")
calculate_bmi(weight=57, height=1.73, underweight=-1, normalweight=0, overweight=1)
