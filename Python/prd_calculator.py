import numpy as np
def calculate_prd(original_signal, noisy_signal):
   
    # Calculate the numerator: squared differences between clean and noisy signals
    squared_diff = np.sum((original_signal - noisy_signal) ** 2)
    # Calculate the denominator: power of the original signal
    original_power = np.sum(original_signal ** 2)
    # Ensure original power is not zero to avoid division by zero
    if original_power == 0:
        return float('inf')
    # Calculate PRD as a percentage
    prd = 100 * np.sqrt(squared_diff / original_power)
    return prd
