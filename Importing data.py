import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st
cars_data = pd.read_csv('C:/Users/barte/Desktop/CAR DETAILS FROM CAR DEKHO.csv') #importing data
print(cars_data.info()) # checking a type of data imported
print(cars_data.corr(numeric_only=True)) # checking basic correlation beetween numeric type of data
