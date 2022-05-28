class Calorie:
    """
    Represent amount of calories calculated
    with BMR = 10*weight + 6.25height + -5*age
    +5 -10*temperature
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculated(self):
        pass