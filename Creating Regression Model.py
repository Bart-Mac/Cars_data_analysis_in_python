corr = cars_data.corr(numeric_only=True)
print(corr)
cars_data.dropna(inplace=True)
x=  cars_data[['Year', 'Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)']]
y= cars_data['Price (in USD)']
model =sm.OLS(y, x.astype(float)).fit()
print(model.summary())
