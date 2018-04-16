def getWeight():

    while True:
        try:
            weightLb = input("How many pounds do you weigh?:")
            return int(weightLb)
        except ValueError:
            print("Please only enter positive numbers.")


def getHeight():

    while True:
        try:
            heightCm = input("How tall are you in cm?")
            return int(heightCm)
        except ValueError:
            print("Please only enter positive numbers.")


def getAge():

    while True:
        try:
            ageInput = input("How many years old are you?")
            return int(ageInput)
        except ValueError:
            print("Please only enter positive numbers.")


def getGender():

    genderInput = input("Are you male or female?")

    if genderInput.lower() == 'male':
        return 'male'
    elif genderInput.lower() == 'female':
        return 'female'


def poundsToMass(weight):
    mass = weight / 2.20462
    return int(mass)


def Mifflin(mass, cm, age, gender):
    """
    Mifflin-St Jeor Formula
    """
    bmrMale = (10 * mass + 6.25 * cm - 5 * age) + 5
    bmrFemale = (10 * mass + 6.25 * cm - 5 * age) - 151

    if gender == 'male':
        return bmrMale
    else:
        return bmrFemale


print("Welcome to my BMR calculator.")

print(f"Your BMR is: {Mifflin(poundsToMass(getWeight()), getHeight(), getAge(), getGender())}")
