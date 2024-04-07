from emission_factors import EMISSION_FACTORS

class Waste:
    def __init__(self, organic_waste, organic_recycled, 
                 paper_waste, paper_recycled, 
                 plastic_waste, plastic_recycled):
        self.organic_waste = organic_waste
        self.paper_waste = paper_waste
        self.plastic_waste = plastic_waste
        
        self.organic_recycled = organic_recycled
        self.paper_recycled = paper_recycled
        self.plastic_recycled = plastic_recycled
        
    def organic(self):
        return (round(((self.organic_waste * (1 - (self.organic_recycled / 100)) * EMISSION_FACTORS["Waste_Organic"]) * 12), 2))
    
    def paper(self):
        return (round(((self.paper_waste * (1 - (self.paper_recycled / 100)) * EMISSION_FACTORS["Waste_Paper"]) * 12), 2))
    
    def plastic(self):
        return (round(((self.plastic_waste * (1 - (self.plastic_recycled / 100)) * EMISSION_FACTORS["Waste_Plastic"]) * 12), 2))
    
    def calculate_emission(self):
        return (self.organic() + self.paper() + self.plastic())