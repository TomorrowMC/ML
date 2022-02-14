import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet


# Loading the data from the repo:
df = pd.read_csv("https://raw.githubusercontent.com/facebook/prophet/master/examples/example_wp_log_peyton_manning.csv")

# Fitting the model
model = Prophet()
model.fit(df) #fit the  model.

# Predict
future = model.make_future_dataframe(periods=730) # predicting for ~ 2 years
forecast = model.predict(future) # Predict future

# Plot results
fig1 = model.plot(forecast) # Plot the fit to past data and future forcast.
fig2 = model.plot_components(forecast) # Plot breakdown of components.
plt.show()
forecast # Displaying various results in table format.