# Caleb Neale, can4ku


def st_jeor(mass, height, age, sex):
    if sex == "male":
        sex_constant = 5
    else:
        sex_constant = -161
    daily_cal = ((10.0*mass)+(6.25*height)-(5.0*age)+sex_constant)
    return daily_cal
