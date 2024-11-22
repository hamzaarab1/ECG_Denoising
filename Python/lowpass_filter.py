from scipy.signal import lfilter

def lowpass_filter(noisy_signal):
    # Design a low-pass Butterworth filter
    b = [0.8576, -0.032, 0.8629, -0.0811]  # Numerator
    a = [1, -1.2096, 0.2644, 0.0144]      # Denominator
    # Apply the filter using lfilter
    filtered_signal = lfilter(b, a, noisy_signal)
    return filtered_signal