from emission_factors import EMISSION_FACTORS

class Travel:
    def __init__(self, by_plane, by_train, by_car):
        self.by_plane = by_plane
        self.by_train = by_train
        self.by_car = by_car
        
    def plane(self):
        return (round((self.by_plane * EMISSION_FACTORS["Travel_Plane"]), 2))
    
    def train(self):
        return (round((self.by_train * EMISSION_FACTORS["Travel_Train"]), 2))
    
    def car(self):
        return (round((self.by_car * EMISSION_FACTORS["Travel_Car"]), 2))    
        
    def calculate_emission(self):
        return (self.plane() + self.train() + self.car())