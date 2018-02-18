def poundsToNewtons(weightLb):
    poundsMass = 4.4482216152605 * weightLb
    return poundsMass
def poundsToKilo(weightLb):
    poundsKilo = weightLb / 2.20462
    return poundsKilo

weightLb = int(input("How many pounds do you weigh?"))
heightCm = int(input("How tall are you in cm?"))
ageInput = int(input("How many years old are you?"))
poundsMass = poundsToNewtons(weightLb)
poundsKilo = poundsToKilo(weightLb)

def Mifflin(poundsMass,heightCm,ageInput):
    global bmrMale,bmrFemale
    bmrMale = (10 * poundsKilo + 6.25 * heightCm - 5 * ageInput) + 5
    bmrFemale = (10 * poundsKilo + 6.25 * heightCm - 5 * ageInput) - 151

Mifflin(poundsMass,heightCm,ageInput)

print(bmrFemale)
    
    
