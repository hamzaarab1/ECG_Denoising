import numpy as np
#x_k is the orignal signal
#x_hat_k is the denoised signal
def calculate_prd(x_k, x_hat_k):
    squared_diff = np.sum((x_k - x_hat_k) ** 2) #orignal signal - denoised signa squared
    original_power = np.sum(x_k ** 2)
    # Ensure original power is not zero to avoid division by zero
    if original_power == 0:
        return float('inf')
    # Calculate PRD 
    prd = 0.01*np.sqrt(squared_diff / original_power)
    
    return prd
