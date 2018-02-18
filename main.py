def weight():
    global weightLb
    weightLb = int(input("How many pounds do you weigh?"))

    if type(weightLb) != int:
        print("Invalid weight. Please try again.")

def height():
    global heightCm
    heightCm = int(input("How tall are you in cm?"))

    if type(heightCm) != int or heightCm < 0:
        print("Invalid height. Please try again.")

def age():
    global ageInput
    ageInput = int(input("How many years old are you?"))

    if type(ageInput) != int or ageInput < 0:
        print("Invalid age. Please try again.")

def gender():
    global gender
    gender = str(input("Are you male or female?"))

    if gender.lower() == 'male':
        print(bmrMale)
    elif gender.lower() == 'female':
        print(bmrFemale)
    else:
        print("Invalid gender. Please try again.")

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
