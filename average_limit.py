from emission_factors import EMISSION_FACTORS


AVERAGE_LIMIT = {
    
    "Energy_Electricity": round((500 * EMISSION_FACTORS['Energy_Electricity'] * 12), 2),
    "Energy_Gas": round((100 * EMISSION_FACTORS['Energy_Gas'] * 12), 2),
    "Energy_Fuel": round((100 * EMISSION_FACTORS['Energy_Fuel'] * 12), 2),
    "Waste_Organic": round((150 * EMISSION_FACTORS['Waste_Organic'] * 12), 2),
    "Waste_Paper": round((150 * EMISSION_FACTORS['Waste_Paper'] * 12), 2),
    "Waste_Plastic": round((150 * EMISSION_FACTORS['Waste_Plastic'] * 12), 2),
    "Travel_Plane": round((4000 * EMISSION_FACTORS['Travel_Plane']), 2),
    "Travel_Train": round((6000 * EMISSION_FACTORS['Travel_Train']), 2),
    "Travel_Car": round((8000 * EMISSION_FACTORS['Travel_Car']), 2)
    
}