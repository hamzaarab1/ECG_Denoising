from scipy.signal import butter, filtfilt

def highpass_filter(signal, cutoff_frequency, sampling_rate, order=5):
    """
    Applies a high-pass Butterworth filter to the input signal.

    Parameters:
        signal (array-like): The input signal to be filtered.
        cutoff_frequency (float): The cutoff frequency for the high-pass filter in Hz.
        sampling_rate (float): The sampling rate of the signal in Hz.
        order (int, optional): The order of the filter. Higher order means a steeper filter. Default is 5.

    Returns:
        filtered_signal (array-like): The filtered signal after applying the high-pass filter.
    """
    # Calculate the Nyquist frequency (half of the sampling rate)
    nyquist = 0.5 * sampling_rate

    # Normalize the cutoff frequency with respect to the Nyquist frequency
    # This is necessary because the butter function works with normalized frequencies
    normal_cutoff = cutoff_frequency / nyquist

    # Design a Butterworth high-pass filter
    # b and a are the numerator and denominator coefficients of the filter, respectively
    b, a = butter(order, normal_cutoff, btype='high', analog=False)

    # Apply the filter to the signal using zero-phase filtering
    # filtfilt applies the filter forward and backward to eliminate phase distortion
    filtered_signal = filtfilt(b, a, signal)

    # Return the filtered signal
    return filtered_signal
