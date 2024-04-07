# table_visualization.py

import pandas as pd
import streamlit as st
from average_limit import AVERAGE_LIMIT
# from app import pl_electricity, pl_gas, pl_fuel, pl_organic, pl_paper, pl_plastic, pl_plane, pl_train, pl_car

class TableVisualizer:
    def __init__(self, electricity, gas, fuel, organic, paper, plastic, plane, train, car):
        self.electricity = electricity
        self.gas = gas
        self.fuel = fuel
        self.organic = organic
        self.paper = paper
        self.plastic = plastic
        self.plane = plane
        self.train = train
        self.car = car

    def results_table(self):        
        column_labels = ['', 'Emission Factors', 'CO2 in kg', 'Average limit in kg', 'Difference in kg']
        myData = [
            ['💡', '🔥', '⛽️', '🍎', '📰', '🍶', '✈️', '🚝', '🚘'],
            ['Electricity', 'Gas', 'Fuel', 'Organic', 'Paper', 'Plastic', 'Plane', 'Train', 'Car'],
            [self.electricity, self.gas, self.fuel, self.organic, self.paper, self.plastic, self.plane, self.train, self.car],
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
            row_class = "negative" if row['Difference in kg'] > 0.0 else ''
            html += f'<tr class="{row_class}">'
            for value in row:
                html += f"<td>{value}</td>"
            html += "</tr>"

        html += "</tbody></table>"
        
        st.markdown(html, unsafe_allow_html=True)

