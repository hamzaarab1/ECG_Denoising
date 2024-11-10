import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def apply_bandstop_filter(ecg_signal, sampling_rate, notch_freq, quality_factor, samples_to_plot=None):
    # Design a bandstop filter using notch filter to remove power line interference
    b, a = signal.iirnotch(notch_freq, quality_factor, sampling_rate)
    
    # Apply the filter to the signal
    filtered_signal = signal.filtfilt(b, a, ecg_signal)
    
    # If samples_to_plot is specified, limit the plot to those samples
    if samples_to_plot is not None:
        filtered_signal = filtered_signal[:samples_to_plot]

    # Plot the filtered signal
    plt.figure(figsize=(10, 4))
    plt.plot(filtered_signal, label='Filtered ECG Signal', color='orange')
    plt.title('Bandstop Filtered ECG Signal')
    plt.xlabel('Time (samples)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

    return filtered_signal
