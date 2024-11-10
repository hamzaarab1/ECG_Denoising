import numpy as np
import matplotlib.pyplot as plt

def fft_analysis(ecg_signal, sampling_rate=500, samples_to_plot=2000):
    """
    Function to perform FFT analysis on the ECG signal.
    
    Parameters:
    - ecg_signal: The raw ECG signal array.
    - sampling_rate: Sampling rate of the ECG signal (default is 500 Hz).
    - samples_to_plot: Number of samples to plot in the FFT (default is 2000).
    """
    # Perform Fast Fourier Transform (FFT)
    N = len(ecg_signal[:samples_to_plot])  # Number of sample points
    T = 1.0 / sampling_rate  # Sampling interval
    fft_signal = np.fft.fft(ecg_signal[:samples_to_plot])  # Compute FFT
    fft_freqs = np.fft.fftfreq(N, T)  # Frequency bins

    # Plot the FFT result (Magnitude of frequencies)
    plt.figure(figsize=(10, 4))
    plt.plot(fft_freqs[:N // 2], np.abs(fft_signal[:N // 2]))  # Only plot positive frequencies
    plt.title('FFT of ECG Signal (Frequency Domain)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.grid()

    # Show the FFT plot
    plt.show()
