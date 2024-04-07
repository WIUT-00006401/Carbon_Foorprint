class Minimize_Emission:
    def __init__(self, over_limit_amount):
        self.over_limit_amount = over_limit_amount
        
    @staticmethod    
    def energy_suggestions(over_limit_amount):
        suggestions = [
            "Consider switching to renewable energy sources if possible.",
            "Improve home insulation to reduce heating and cooling needs.",
            "Invest in energy-efficient appliances."
        ]
        return suggestions
    
    @staticmethod
    def waste_suggestions(over_limit_amount):
        suggestions = [
            "Increase recycling efforts for organic, paper, and plastic waste.",
            "Compost organic waste.",
            "Reduce usage of single-use plastics."
        ]
        return suggestions
    
    @staticmethod
    def travel_suggestions(over_limit_amount):
        suggestions = [
            "Opt for public transportation or carpooling whenever possible.",
            "Consider the necessity of each flight and explore alternatives.",
            "Maintain your vehicle regularly to ensure fuel efficiency."
        ]
        return suggestions