# -*- coding: utf-8 -*-
"""C114 Linear Regression Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MCq66XWOjpe12k0HQ9Hrv-iuk_k8BokA
"""

#Uploading the csv
from google.colab import files
data_to_load = files.upload()

"""plotting the TOEFL as X-Coordinate and Chances of admit as Y-Coordinate on the scatter plot."""

import pandas as pd
import plotly.express as px

df = pd.read_csv("main.csv")

TOEFL_Score = df["TOEFL Score"].tolist()
Chances_of_admit = df["Chance of Admit "].tolist()

fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.show()

"""Adding a line using the line equation on the plot."""

m = 1
c = 0
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

"""Changing the values of m and c to find the best fit line

"""

m = 0.018
c = -1.27
y = []
for x in TOEFL_Score:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_Score, y=Chances_of_admit)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_Score), x1= max(TOEFL_Score)
    )
])
fig.show()

"""Now we have the value of slope as 0.018 and intercept as -1.27.
Now we are going to predict the chances of admit based on the TOEFL score
"""

x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")

"""Now we'll use the predefined computer algorithm to find the best fit line and the values of m and c."""

import numpy as np
TOEFL_array = np.array(TOEFL_Score)
Chances_array = np.array(Chances_of_admit)

#Slope and intercept using pre-built function of Numpy
m, c = np.polyfit(TOEFL_array, Chances_array, 1)
y = []
for x in TOEFL_array:
  y_value = m*x + c
  y.append(y_value)

#Plotting the points
fig = px.scatter(x=TOEFL_array, y=Chances_array)
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= min(y), y1= max(y),
      x0= min(TOEFL_array), x1= max(TOEFL_array)
    )
])
fig.show()

"""Now using the values found let's predict the chances of a person to admit."""

x = 250
y = m * x + c
print(f"Chances of admit if the TOEFL score {x} is {y}")