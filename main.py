def getWeight():
    """
    Returns an integer representing the user's weight in pounds
    """
    while True:
        try:
            weightLb = input("How many pounds do you weigh?:")
            return int(weightLb)
        except ValueError:
            print("Please only enter positive numbers.")


def getHeight():
    """
    Returns an integer representing the user's height in centimeters
    """
    while True:
        try:
            heightCm = input("How tall are you in cm?")
            return int(heightCm)
        except ValueError:
            print("Please only enter positive numbers.")


def getAge():
    """
    Returns an integer representing the user's age in years
    """
    while True:
        try:
            ageInput = input("How many years old are you?")
            return int(ageInput)
        except ValueError:
            print("Please only enter positive numbers.")


def getGender():
    """
    Returns a string representing the user's gender
    """
    genderInput = input("Are you male or female?")

    if genderInput.lower() == 'male':
        return 'male'
    elif genderInput.lower() == 'female':
        return 'female'


def poundsToMass(weight):
    """
    Returns an integer representing the user's mass
    """
    mass = weight / 2.20462
    return int(mass)


def Mifflin(mass, cm, age, gender):
    """
    Mifflin-St Jeor Formula
    """
    bmrMale = (10 * mass + 6.25 * cm - 5 * age) + 5
    bmrFemale = (10 * mass + 6.25 * cm - 5 * age) - 151

    if gender == 'male':
        return int(bmrMale)
    else:
        return int(bmrFemale)


print("Welcome to my BMR calculator.")
print(f"Your BMR is {Mifflin(poundsToMass(getWeight()), getHeight(), getAge(), getGender())} calories per day.")
