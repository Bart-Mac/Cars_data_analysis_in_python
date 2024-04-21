CORREL = cars_data.corr(numeric_only=True)
sns.heatmap(CORREL, cmap="YlGnBu", annot=True, cbar=True)
plt.show()
pd.to_numeric(cars_data['Engine Size (L)'], errors='coerce')
cars_data.dropna(how='any', inplace=True)
X = cars_data[["Year", "Horsepower", "Torque (lb-ft)", "0-60 MPH Time (seconds)", "Electric", "Hybrid"]]
Y = cars_data["Price (in USD)"]
X =sm.add_constant(X)
model = sm.OLS(Y, X.astype(float)).fit()
print(model.summary())

'''
OLS Regression Results                            
==============================================================================
Dep. Variable:         Price (in USD)   R-squared:                       0.626
Model:                            OLS   Adj. R-squared:                  0.623
Method:                 Least Squares   F-statistic:                     274.8
Date:                Sun, 21 Apr 2024   Prob (F-statistic):          1.39e-206
Time:                        18:24:25   Log-Likelihood:                -14343.
No. Observations:                 994   AIC:                         2.870e+04
Df Residuals:                     987   BIC:                         2.873e+04
Df Model:                           6                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                    2.943e+07   1.42e+07      2.076      0.038    1.61e+06    5.72e+07
Year                    -1.521e+04   7013.338     -2.169      0.030    -2.9e+04   -1452.155
Horsepower               2115.5007    139.888     15.123      0.000    1840.989    2390.012
Torque (lb-ft)            214.9037    169.197      1.270      0.204    -117.123     546.930
0-60 MPH Time (seconds)   8.29e+04   2.62e+04      3.162      0.002    3.14e+04    1.34e+05
Electric                -6.356e+05   9.02e+04     -7.044      0.000   -8.13e+05   -4.59e+05
Hybrid                  -1.199e+04   3.18e+05     -0.038      0.970   -6.35e+05    6.11e+05
==============================================================================
Omnibus:                      761.779   Durbin-Watson:                   1.828
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            16661.240
Skew:                           3.341   Prob(JB):                         0.00
Kurtosis:                      21.911   Cond. No.                     2.18e+06
==============================================================================
1. The Torque (lb-ft) and hybrid variables turned out to be statistically insignificant, so I then removed it from the model
2. 62% of the variability of the explanatory variable was explained by the model


Corrected model
OLS Regression Results                            
==============================================================================
Dep. Variable:         Price (in USD)   R-squared:                       0.625
Model:                            OLS   Adj. R-squared:                  0.623
Method:                 Least Squares   F-statistic:                     412.0
Date:                Sun, 21 Apr 2024   Prob (F-statistic):          7.54e-209
Time:                        18:27:20   Log-Likelihood:                -14343.
No. Observations:                 994   AIC:                         2.870e+04
Df Residuals:                     989   BIC:                         2.872e+04
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                    2.928e+07   1.42e+07      2.066      0.039    1.47e+06    5.71e+07
Year                    -1.513e+04   7011.444     -2.158      0.031   -2.89e+04   -1368.505
Horsepower               2267.5737     72.420     31.312      0.000    2125.460    2409.687
0-60 MPH Time (seconds)  8.242e+04   2.62e+04      3.145      0.002     3.1e+04    1.34e+05
Electric                -6.087e+05   8.77e+04     -6.941      0.000   -7.81e+05   -4.37e+05
==============================================================================
Omnibus:                      767.583   Durbin-Watson:                   1.826
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            16795.671
Skew:                           3.381   Prob(JB):                         0.00
Kurtosis:                      21.969   Cond. No.                     2.11e+06
==============================================================================
1. All variables are statistically significant
2. 62% of the variability of the explanatory variable was explained by the model
'''


