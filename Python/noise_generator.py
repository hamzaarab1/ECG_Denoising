# noise_generator.py
import numpy as np

def generate_60hz_noise(signal_length, sampling_rate=360):
    # Generate time values based on the signal length and sampling rate
    t = np.arange(signal_length) / sampling_rate
    # Create 60 Hz sinusoidal noise
    noise = 0.1 * np.sin(2 * np.pi * 60 * t)
    # 2*pi to convert frequency in Hz to Rad. 60 is the powline interference, and t is the time array
    #Result 6Hz sine wave * 0.1(scales the amplitude of the noise to 0.1)
    return noise
