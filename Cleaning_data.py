import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st
cars_data['Horsepower'] = cars_data['Horsepower'].str.replace(',', '.').str.replace('+','')
cars_data['Horsepower'] = pd.to_numeric(cars_data['Horsepower'])
