import numpy as np

def mean_squared_error(y_pred, y_true):
    y_pred = np.asarray(y_pred, float)
    y_true = np.asarray(y_true, float)

    return np.mean((y_pred -y_true)**2)

    
    
    """
    Returns: float MSE
    """
    # Write code here
    pass
