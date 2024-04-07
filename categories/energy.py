from emission_factors import EMISSION_FACTORS

class Energy:
    def __init__(self, electricity_bill, gas_bill, fuel_bill):
        self.electricity_bill = electricity_bill
        self.gas_bill = gas_bill
        self.fuel_bill = fuel_bill
        
    def electricity(self):
        return (round(((self.electricity_bill * EMISSION_FACTORS["Energy_Electricity"]) * 12), 2))
    
    def gas(self):
        return (round(((self.gas_bill * EMISSION_FACTORS["Energy_Gas"]) * 12), 2))
    
    def fuel(self):
        return (round(((self.fuel_bill * EMISSION_FACTORS["Energy_Fuel"]) * 12), 2))        
        
    def calculate_emission(self):
        return (self.electricity() + self.gas() + self.fuel())