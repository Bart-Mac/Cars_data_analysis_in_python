import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st
cars_data['Horsepower'] = cars_data['Horsepower'].str.replace(',', '.').str.replace('+','')
cars_data['Horsepower'] = pd.to_numeric(cars_data['Horsepower'])
print(cars_data.info())
cars_data['Price (in USD)']= cars_data['Price (in USD)'].str.replace(',', '')
cars_data['Price (in USD)'] = pd.to_numeric(cars_data['Price (in USD)'])
print(cars_data.info())
print(cars_data['Torque (lb-ft)'].unique())
cars_data['Torque (lb-ft)'] = cars_data['Torque (lb-ft)'].str.replace(',', '.').str.replace('-', '').str.replace('+', '')
cars_data['Torque (lb-ft)'] = pd.to_numeric(cars_data['Torque (lb-ft)'])
print(cars_data.info())
print(cars_data['0-60 MPH Time (seconds)'].unique())
cars_data['0-60 MPH Time (seconds)'] = cars_data['0-60 MPH Time (seconds)'].str.replace('<', '')
cars_data['0-60 MPH Time (seconds)'] = pd.to_numeric(cars_data['0-60 MPH Time (seconds)'])
print(cars_data.info())
print(cars_data['Engine Size (L)'].unique())
cars_data['Engine Size (L)'] = pd.to_numeric(cars_data['Engine Size (L)'], errors='coerce')
print(cars_data.info())
