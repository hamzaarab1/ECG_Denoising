import numpy as np
#x_k is the orignal signal
#x_hat_k is the denoised signal
def calculate_rmse(x_k, x_hat_k):
    squared_diff = np.sum((x_hat_k - x_k) ** 2) #(denoised signa - orignal signal) squared
    original_power = np.sum(x_k ** 2)

    squared_diff = np.sum((x_k - x_hat_k) ** 2)# Calculate squared difference
    N = len(x_k)
    
    rmse = np.sqrt(squared_diff / N)
    return rmse