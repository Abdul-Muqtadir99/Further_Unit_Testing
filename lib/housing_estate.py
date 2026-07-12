
class HousingEstate:
    def __init__(self):
        self.houses = []

    def get_house_numbers(self):
        # Numbers_in_housing_estate = []
        # for house in self.houses:
        #     Numbers_in_housing_estate.append(house.number)
        # return Numbers_in_housing_estate

# Below is list comprehension of the for loop above.
        return [house.number for house in self.houses]