corr = cars_data.corr(numeric_only=True)
print(corr)
cars_data.dropna(inplace=True)
x=  cars_data[['Year', 'Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)']]
y= cars_data['Price (in USD)']
x =sm.add_constant(x)
model =sm.OLS(y, x.astype(float)).fit()
print(model.summary())
OLS Regression Results
'''
 OLS Regression Results                            
==============================================================================
Dep. Variable:         Price (in USD)   R-squared:                       0.609
Model:                            OLS   Adj. R-squared:                  0.607
Method:                 Least Squares   F-statistic:                     293.0
Date:                Wed, 17 Apr 2024   Prob (F-statistic):          4.87e-189
Time:                        08:53:12   Log-Likelihood:                -13647.
No. Observations:                 948   AIC:                         2.731e+04
Df Residuals:                     942   BIC:                         2.733e+04
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                    4.183e+07    1.4e+07      2.978      0.003    1.43e+07    6.94e+07
Year                    -2.155e+04   6947.882     -3.102      0.002   -3.52e+04   -7917.520
Engine Size (L)         -5.017e+04    1.3e+04     -3.874      0.000   -7.56e+04   -2.48e+04
Horsepower               2640.5774    173.760     15.197      0.000    2299.576    2981.579
Torque (lb-ft)            294.6420    206.491      1.427      0.154    -110.593     699.877
0-60 MPH Time (seconds)  1.635e+05   2.83e+04      5.786      0.000    1.08e+05    2.19e+05
==============================================================================
Omnibus:                      836.716   Durbin-Watson:                   1.739
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            32459.291
Skew:                           3.887   Prob(JB):                         0.00
Kurtosis:                      30.592   Cond. No.                     2.16e+06
==============================================================================
1. The Torque (lb-ft) variable turned out to be statistically insignificant, so I then removed it from the model
2. 60% of the variability of the explanatory variable was explained by the model
'''
