# visualization.py

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import streamlit as st

class PieChartVisualizer:
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

    def results_pie_chart(self):
        fig, ax = plt.subplots()
        ax.set_title("Pie chart Analysis")

        size = 0.25
        vals = np.array([[self.electricity, self.gas, self.fuel], [self.organic, self.paper, self.plastic], [self.plane, self.train, self.car]])
        
        total = vals.sum()

        cmap = plt.colormaps["tab20c"]
        outer_colors = cmap(np.array([1, 5, 9]))
        inner_colors = cmap(np.array([1, 2, 3, 5, 6, 7, 9, 10, 11]))

        labels_outer = ['Energy', 'Waste', 'Travel']
        labels_inner = ['Electricity', 'Gas', 'Fuel', 'Organic', 'Paper', 'Plastic', 'Plane', 'Train', 'Car']

        percentages_inner = [f"{label} ({val/total*100:.1f}%)" for label, val in zip(labels_inner, vals.flatten())]

        ax.pie(vals.sum(axis=1), radius=0.8, colors=outer_colors, labels=labels_outer, wedgeprops=dict(width=size, edgecolor='w'), autopct='%1.1f%%', pctdistance=0.85, startangle=140)

        ax.pie(vals.flatten(), radius=0.8-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'), pctdistance=0.75, startangle=140)
        
        inner_patches = [mpatches.Patch(color=inner_colors[i], label=label) for i, label in enumerate(percentages_inner)]

        plt.legend(handles=inner_patches, bbox_to_anchor=(1.05, 1), loc='upper left', title="Subcategories")
        plt.tight_layout()
        ax.set(aspect="equal")
        st.pyplot(fig)
