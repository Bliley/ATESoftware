from lmfit import Model
import numpy as np

# Define the nonlinear model function
def nonlinear_model(x, a, b, c):
    return a + b * np.log(abs(1 + c * x))

def modelFit(x, y): 
    coefs = []

    # Create a model object using the nonlinear model function
    model = Model(nonlinear_model)

    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    # Perform the fit
    result = model.fit(y, x=x, a=0.001, b=0.01, c=1.0, method='slsqp')

    # Extract fitted parameters
    coefs.append(result.params['a'].value)
    coefs.append(result.params['b'].value)
    coefs.append(result.params['c'].value)

    # Calculate predicted values
    predicted_values = nonlinear_model(x, result.params['a'].value, result.params['b'].value, result.params['c'].value)

    # Rescale predicted values to match the range of y
    min_y, max_y = np.min(y), np.max(y)
    min_pred, max_pred = np.min(predicted_values), np.max(predicted_values)
    scaled_predicted_values = (predicted_values - min_pred) / (max_pred - min_pred) * (max_y - min_y) + min_y
    
    # Calculate RMSE
    residuals = y - scaled_predicted_values
    rmse = np.sqrt(np.mean(residuals**2))
    coefs.append(rmse)

    # Calculate value at 365 days and rescale it
    value_at_365_days = nonlinear_model(365, result.params['a'].value, result.params['b'].value, result.params['c'].value)
    scaled_value_at_365_days = (value_at_365_days - min_pred) / (max_pred - min_pred) * (max_y - min_y) + min_y
    coefs.append(scaled_value_at_365_days)

    return coefs
