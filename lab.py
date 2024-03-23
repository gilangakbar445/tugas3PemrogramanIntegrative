class BMI:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False
    
person1 = BMI(100, 1.80)
person2 = BMI(77, 1.74)
print("Are person 1 and person 2 equal?", person1 == person2)