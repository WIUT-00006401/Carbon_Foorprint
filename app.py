import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

from energy import Energy
from waste import Waste
from travel import Travel
from minimize_emission import Minimize_Emission

from average_limit import AVERAGE_LIMIT




# Main page parameters
st.set_page_config(page_title="Carbon Calculator")
st.title("Carbon Footprint Calculator")

st.markdown("***")
st.markdown("This project is created as a part of the assignment from Computer Programming module in GISMA University of Applied Sciences. The primary functionality of this tool revolves around enabling users to input data concerning their energy consumption, waste generation, and travel habits. Upon processing this data, the tool calculates the overall carbon footprint and generates detailed reports. These reports highlight areas where emissions exceed recommended limits and offer suggestions for reducing their carbon footprint. From a technical standpoint, the project utilizes a combination of Python for backend calculations and Streamlit for creating an interactive web interface.")
st.markdown("Student ID: GH1028483")
st.markdown("***")



# Input parameters

# Electricity
st.subheader("⚡️ Energy consumption (monthly bill in euros)")

col1, col2, col3 = st.columns(3)

with col1:
    electricity = st.number_input("💡 Electricity consumption", 0, key="electricity_input")
    # electricity = round(electricity, 2)

with col2:
    gas = st.number_input("🔥 Natural Gas", 0, key="gas_input")
    # gas = round(gas, 2)

with col3:
    fuel = st.number_input("⛽️ Fuel", 0, key="fuel_input")
    # fuel = round(fuel, 2)

st.markdown("***")

# Waste
st.subheader("🗑 Monthly Waste generated (kg) and recycled (%)")

# --organic waste
col4, col5 = st.columns(2)
with col4:
    organic_waste = st.number_input("🍎 Organic", 0, key="organic_waste_input")
with col5:
    organic_recycled = st.slider("♻️ Recycled", 0, 100, key="organic_recycled_input")

# --paper waste
col6, col7 = st.columns(2)
with col6:
    paper_waste = st.number_input("📰 Paper", 0, key="paper_waste_input")
with col7:
    paper_recycled = st.slider("♻️ Recycled", 0, 100, key="paper_recycled_input")

# --plastic waste
col8, col9 = st.columns(2)
with col8:
    plastic_waste = st.number_input("🍶 Plastic", 0, key="plastic_waste_input")
with col9:
    plastic_recycled = st.slider("♻️ Recycled", 0, 100, key="plastic_recycled_input")


st.markdown("***")

# Travel
st.subheader("🗺 Business travel per year (in km)")

col10, col11, col12 = st.columns(3)

with col10:
    travel_plane = st.number_input("✈️By Plane", 0, key="travel_plane")
with col11:
    travel_train = st.number_input("🚝 By Train", 0, key="travel_train")
with col12:
    travel_car = st.number_input("🚘 By Car", 0, key="travel_car")
    

st.markdown("***")


# Generating factors by categories
energy = Energy(electricity, gas, fuel)
waste = Waste(organic_waste, organic_recycled, paper_waste, paper_recycled, plastic_waste, plastic_recycled)
travel = Travel(travel_plane, travel_train, travel_car)

# Total results of each categories for plotting a pie chart and a table
pl_electricity = energy.electricity()
pl_gas = energy.gas()
pl_fuel = energy.fuel()

pl_organic = waste.organic()
pl_paper = waste.paper()
pl_plastic = waste.plastic()

pl_plane = travel.plane()
pl_train = travel.train()
pl_car = travel.car()

# Calculating emission factors
energy_emission = energy.calculate_emission()
waste_emission = waste.calculate_emission()
travel_emission = travel.calculate_emission()
# Sum up the results
total_emission = energy_emission + waste_emission + travel_emission


def results_pie_chart():
    # st.title("Nested Pie Chart Result with Matplotlib")
    fig, ax = plt.subplots()
    ax.set_title("Customizing pie chart")

    size = 0.25
    vals = np.array([[pl_electricity, pl_gas, pl_fuel], [pl_organic, pl_paper, pl_plastic], [pl_plane, pl_train, pl_car]])
    
    total = vals.sum()

    # Colors of pie chart
    cmap = plt.colormaps["tab20c"]
    outer_colors = cmap(np.array([1, 5, 9]))
    inner_colors = cmap(np.array([1, 2, 3, 5, 6, 7, 9, 10, 11]))

    # # Labels for the outer and inner rings
    labels_outer = ['Energy', 'Waste', 'Travel']
    labels_inner = ['Electricity', 'Gas', 'Fuel', 'Organic', 'Paper', 'Plastic', 'Plane', 'Train', 'Car']
    # labels_inner = ['💡', '🔥', '⛽️', '🍎', '📰', '🍶', '✈️', '🚝', '🚘']

    percentages_inner = [f"{label} ({val/total*100:.1f}%)" for label, val in zip(labels_inner, vals.flatten())]

    # Plotting the inner ring with colors
    ax.pie(vals.sum(axis=1), 
        radius=0.8, 
        colors=outer_colors, 
        labels=labels_outer,
        wedgeprops=dict(width=size, edgecolor='w'), 
        autopct='%1.1f%%', 
        pctdistance=0.85, 
        startangle=140)

    # Plotting the inner ring with colors
    ax.pie(vals.flatten(), 
        radius=0.8-size, 
        colors=inner_colors, 
        #labels=labels_inner,
        wedgeprops=dict(width=size, edgecolor='w'), 
        #autopct='%1.0f%%', 
        pctdistance=0.75, 
        startangle=140)
    
    inner_patches = [mpatches.Patch(color=inner_colors[i], label=label) for i, label in enumerate(percentages_inner)]

    # Adding the legend to the plot
    plt.legend(handles=inner_patches, bbox_to_anchor=(1.05, 1), loc='upper left', title="Categories")

    # Adjusting layout to make room for the legend
    plt.tight_layout()

    # Equal aspect ratio ensuring that pie is drawn as a circle.
    ax.set(aspect="equal")
    st.pyplot(fig)
    

    
def results_table():

    column_labels = ['', 'Emission Factors', 'CO2 in kg', 'Average limit in kg', 'Difference']
    myData = [
        ['💡', '🔥', '⛽️', '🍎', '📰', '🍶', '✈️', '🚝', '🚘'],
        ['Electricity', 'Gas', 'Fuel', 'Organic', 'Paper', 'Plastic', 'Plane', 'Train', 'Car'],
        [pl_electricity, pl_gas, pl_fuel, pl_organic, pl_paper, pl_plastic, pl_plane, pl_train, pl_car],
        [AVERAGE_LIMIT["Energy_Electricity"], AVERAGE_LIMIT["Energy_Gas"], AVERAGE_LIMIT["Energy_Fuel"], 
         AVERAGE_LIMIT["Waste_Organic"], AVERAGE_LIMIT["Waste_Paper"], AVERAGE_LIMIT["Waste_Plastic"],
         AVERAGE_LIMIT["Travel_Plane"], AVERAGE_LIMIT["Travel_Train"], AVERAGE_LIMIT["Travel_Car"]]
    ]
    
    myData.append([round((myData[2][i] - myData[3][i]), 2) for i in range(len(myData[0]))])
    
    data_transposed = list(map(list, zip(*myData)))  # Transpose operation

    # Creating a DataFrame
    df = pd.DataFrame(data_transposed, columns=column_labels)
    
    html = """
    <style>
        .dataframe {width: 100%; border-collapse: collapse;}
        .dataframe th, .dataframe td {text-align: left; border: 1px solid black;}
        .dataframe th {background-color: #f0f0f0;}
        .negative {background-color: #ffcccc;}
    </style>
    <table class="dataframe"><thead><tr>
    """

    # Adding headers to the HTML string
    for col in df.columns:
        html += f'<th>{col}</th>'
    html += '</tr></thead><tbody>'

    # Add the data rows to the HTML string
    for index, row in df.iterrows():
        # Applying a 'negative' class to rows where the last column value is less than 0
        row_class = "negative" if row['Difference'] > 0.0 else ''
        html += f'<tr class="{row_class}">'
        for value in row:
            html += f"<td>{value}</td>"
        html += "</tr>"

    html += "</tbody></table>"
    
    st.markdown(html, unsafe_allow_html=True)



suggestion_functions = {
    'energy': Minimize_Emission.energy_suggestions,
    'waste': Minimize_Emission.waste_suggestions,
    'travel': Minimize_Emission.travel_suggestions
}

average_energy_limit = AVERAGE_LIMIT['Energy_Electricity'] + AVERAGE_LIMIT['Energy_Gas'] + AVERAGE_LIMIT['Energy_Fuel']
average_waste_limit = AVERAGE_LIMIT['Waste_Organic'] + AVERAGE_LIMIT['Waste_Paper'] + AVERAGE_LIMIT['Waste_Plastic']
average_travel_limit = AVERAGE_LIMIT['Travel_Plane'] + AVERAGE_LIMIT['Travel_Train'] + AVERAGE_LIMIT['Travel_Car']

category_contributions = {
    'energy': energy_emission - average_energy_limit,
    'waste': waste_emission - average_waste_limit,
    'travel': travel_emission - average_travel_limit
}

def evaluate_and_suggest(category_contributions):
    for category, over_limit_amount in category_contributions.items():
        if over_limit_amount > 0:
            st.info(f"Suggestions to reduce {category} emissions")
            suggestions = suggestion_functions[category](over_limit_amount)
            for suggestion in suggestions:
                st.markdown(f"- {suggestion}")
        else
            st.info("There is no exceeding amount of emission among factors for suggestion evaluations")


# Present the results
if st.button("Calculate CO2 Emissions"):
    
    st.header("Results")
    
    col3, col4 = st.columns([2, 3])
    
    with col3:
        st.subheader("By Categories")
        
        st.info(f"⚡️ Energy: {energy_emission} kg")
        st.info(f"🗑 Waste: {waste_emission} kg")
        st.info(f"🗺 Business Travel: {travel_emission} kg")
        
    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"🌎 Total Carbon footprint is: {round((total_emission), 2)} kg CO2 per year")
        # st.warning("Pass")
        if total_emission <= 9430.36:
            st.info("🌳 Carbon emission is within the limit")
            total_difference = 9430.36 - total_emission
            st.info(f"Untill the average: {round(total_difference, 2)} kg")
        else:
            st.info("🔴 Average limit is exceeded")
            total_difference = total_emission - 9430.36
            st.info(f"Exceeding amount is: {round(total_difference, 2)} kg")
            
    try:
        results_pie_chart()
    except Exception as e:
        st.error(f"Failed to generate the pie chart due to incorrect user input")  
        st.write("At least one user input should be generated for representing pie chart ")  
        
    # results_pie_chart()
    results_table()
    
    st.markdown("***")
    
    evaluate_and_suggest(category_contributions)
