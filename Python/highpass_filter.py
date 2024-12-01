from scipy.signal import lfilter
def highpass_filter(noisy_signal):
    b = [-0.58034, 1.9441, -1.9441, 0.5034]
    a = [1,-1.1737, 0.2982, 0.0245]  
    filtered_signal = lfilter(b, a, noisy_signal)
    return filtered_signal
