import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as st
import seaborn as sns
cars_data = pd.read_csv('/Sport car price.csv') #importing data
print(cars_data.info()) # checking data type
