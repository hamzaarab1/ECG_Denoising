import numpy as np

def calculate_snr(original_signal, noisy_signal):
    # Calculate the power of the clean signal
    signal_power = np.sum(original_signal ** 2)
    # Calculate the noise power (difference between noisy and clean signal)
    noise_power = np.sum((noisy_signal - original_signal) ** 2)
    # Ensure noise power is not zero to avoid division by zero
    if noise_power == 0:
        return float('inf')
    # Calculate SNR in dB
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

