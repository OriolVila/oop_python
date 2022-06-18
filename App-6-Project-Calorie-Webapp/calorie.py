class Calorie:
    """
    Represent amount of calories calculated
    with BMR = 10*weight + 6.25height + -5*age
    +5 -10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = float(temperature)

    def calculated(self):

        result = 10 * self.weight + 6.5 * self.height + 5 * self.age - 10 * self.temperature
        return result
