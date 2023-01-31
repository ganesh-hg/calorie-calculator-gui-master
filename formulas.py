def male_bmr(weight, height, age):
    # Calculate male bmr
    return (6.24 * weight) + (12.7 * height) - (6.755 * age) + 66.47


def female_bmr(weight, height, age):
    # Calculate female BMR
    return (4.35 * weight) + (4.7 * height) - (4.7 * age) + 665.1


def male_calories(heartrate, weight, age, duration):
    # Calculate male calories burned based on heart rate and duration
    return (
        (-55.0969 + (0.6309 * heartrate) + (0.1988 * (weight / 2.205)) + (0.2017 * age))
        / 4.184
    ) * duration


def female_calories(heartrate, weight, age, duration):
    # Calculate female calories burned based on heart rate and duration
    return (
        (-20.4022 + (0.4472 * heartrate) - (0.1263 * (weight / 2.205)) + (0.074 * age))
        / 4.184
    ) * duration
