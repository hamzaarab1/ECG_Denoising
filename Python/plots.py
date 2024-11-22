import wfdb
import matplotlib.pyplot as plt
import numpy as np
from noise_generator import generate_60hz_noise  # Importing the noise generator
from lowpass_filter import lowpass_filter
from highpass_filter import highpass_filter  # Importing the high-pass filter function

# Load the ECG record
record_name = 'mit-bih-arrhythmia-database-1.0.0/101'  # Set the path for a specific record here
record = wfdb.rdrecord(record_name, sampfrom=0, channels=[0])  # Read the specified ECG record

# Extract the signal data
original_signal = record.p_signal[:, 0]

# Generate noise and add it to the signal
sampling_rate = 360   # Sampling rate in Hz
frequency = 60        # Power line interference frequency in Hz
amplitude = 0.0985    # Noise amplitude can be adjusted from 0.05mV to 0.3mV
harmonics = None      # Optional; if needed, define harmonics (e.g., [(0.05, 2)])
noise = generate_60hz_noise(len(original_signal), sampling_rate, frequency, amplitude, harmonics)
noisy_signal = np.array(original_signal) + np.array(noise)

# Apply filters
denoised_signal_lp = lowpass_filter(noisy_signal)  # Low-pass filter
cutoff_frequency_hp = 1.0  # Example: 1 Hz cutoff frequency for high-pass filter
denoised_signal_hp = highpass_filter(noisy_signal, cutoff_frequency_hp, sampling_rate)  # High-pass filter

# Combine low-pass and high-pass filters
denoised_signal_combined = highpass_filter(denoised_signal_lp, cutoff_frequency_hp, sampling_rate)

# Number of samples to plot (in seconds)
seconds = 5
sample_to_plot = seconds * sampling_rate  # Sampling rate is 360 Hz

# Combine all five plots into a single figure
plt.figure(figsize=(15, 20))

# Plot the raw signal
plt.subplot(5, 1, 1)
plt.plot(original_signal[:sample_to_plot], label="Original Signal")
plt.title(f"ECG Signal from Record 100 (First {seconds} seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.legend()

# Plot the noisy signal
plt.subplot(5, 1, 2)
plt.plot(noisy_signal[:sample_to_plot], label="Noisy Signal", color='orange')
plt.title(f"Noisy ECG Signal from Record 100 (First {seconds} seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.legend()

# Plot the low-pass filtered signal
plt.subplot(5, 1, 3)
plt.plot(denoised_signal_lp[:sample_to_plot], label="Low-Pass Filtered Signal", color='green')
plt.title("Low-Pass Filtered ECG Signal")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.legend()

# Plot the high-pass filtered signal
plt.subplot(5, 1, 4)
plt.plot(denoised_signal_hp[:sample_to_plot], label="High-Pass Filtered Signal", color='purple')
plt.title("High-Pass Filtered ECG Signal")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.legend()

# Plot the combined denoised signal
plt.subplot(5, 1, 5)
plt.plot(denoised_signal_combined[:sample_to_plot], label="Combined Low-Pass & High-Pass Filtered Signal", color='blue')
plt.title("Denoised ECG Signal (Combined Filters)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.legend()

# Adjust layout and show the combined plot
plt.tight_layout()
plt.show()
