def weight():
    global weightLb

    while True:
        try:
            weightLb = int(input("How many pounds do you weigh?:"))
        except ValueError:
            print("Please only enter positive numbers.")
            continue
        else:
            break

def height():
    global heightCm

    while True:
        try:
            heightCm = int(input("How tall are you in cm?"))
        except ValueError:
            print("Please only enter positive numbers.")
            continue
        else:
            break

def age():
    global ageInput

    while True:
        try:
            ageInput = int(input("How many years old are you?"))
        except ValueError:
            print("Please only enter positive numbers.")
            continue
        else:
            break

def gender():
    global gender

    while True:
        gender = input("Are you male or female?")
        gender = gender.lower()
        if gender == 'male':
            print("Your bmr is",int(bmrMale))
            break
        elif gender == 'female':
            print("Your bmr is",int(bmrFemale))
            break
        else:
            print("Invalid gender. Please try again.")
            continue
            

def poundsToNewtons(weightLb):
    poundsMass = 4.4482216152605 * weightLb
    return poundsMass

def poundsToKilo(weightLb):
    poundsKilo = weightLb / 2.20462
    return poundsKilo

def Mifflin(poundsMass,heightCm,ageInput):
    global bmrMale,bmrFemale
    bmrMale = (10 * poundsKilo + 6.25 * heightCm - 5 * ageInput) + 5
    bmrFemale = (10 * poundsKilo + 6.25 * heightCm - 5 * ageInput) - 151
    
weight()
poundsMass = poundsToNewtons(weightLb)
poundsKilo = poundsToKilo(weightLb)
height()
age()
Mifflin(poundsMass,heightCm,ageInput)
gender()
