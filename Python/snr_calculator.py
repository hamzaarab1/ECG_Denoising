import numpy as np
#x_k is the orignal signal
#y_k is the noisy signal 
#x_hat_k is the denoised signal
def calculate_snr(x_k, y_k,x_hat_k):
    signal_power = np.sum((x_hat_k-x_k) ** 2)
    noise_power = np.sum((y_k - x_k) ** 2)
    if noise_power == 0:
        return float('inf')
    # Calculate SNR in dB
    snr = 10 * np.log10(signal_power/noise_power)
    return snr
#if the signal is not denoised we user the formula
# x(k)^2/ (y(k)-x(k))^2

# if the signal is denoised 
# y(k) or the noisy signa 
# x(x) is the raw signa 
# x^(x) is the filtered signal 
# (y(k)-x(k))^2/(x^(k)-x(k))^2
