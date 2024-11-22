import wfdb
import matplotlib.pyplot as plt
import numpy as np
from noise_generator import generate_60hz_noise  # Importing the noise generator
from lowpass_filter import lowpass_filter

# Load the ECG record
record_name = 'mit-bih-arrhythmia-database-1.0.0/101'  #set the path for a specific record in here file 100
record = wfdb.rdrecord(record_name, sampfrom=0, channels=[0])  # rerecord is to read the spcificed ECG recor
# Extract the signal data
original_signal = record.p_signal[:, 0]  


# Generate noise and add it to the signal
sampling_rate = 360   # Sampling rate in Hz
frequency = 60      # Power line interference frequency in Hz
amplitude = 0.0985     # Noise amplitude can be adjusted from 0.05mV to 0.3mV
harmonics = None #optinal if needed depoding on type of noise genrated example = [(0.05, 2)]
noise = generate_60hz_noise(len(original_signal), sampling_rate, frequency, amplitude, harmonics)
noisy_signal = np.array(original_signal) + np.array(noise)

#Lowpass filter
denoised_signal_lp = lowpass_filter(noisy_signal)

#Plots
# how many samples to plot in seconds?
seconds= 5
sample_to_plot = seconds * 360 #sampling rate is 360 was provided on the MIT-BIH Arrhythmia


# Plot the raw signal
plt.figure(figsize=(12, 6))
plt.plot(original_signal[:sample_to_plot])  # Plotting the first 3 second with each second 360 sample
plt.title(f"ECG Signal from Record 100 (First {seconds} seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()

# Plot the noisy signal
plt.figure(figsize=(12, 6))
plt.plot(noisy_signal[:sample_to_plot])  # Plotting the first 3 seconds (360 samples per second)
plt.title(f"Noisy ECG Signal from Record 100 (First {seconds} seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()


#plotting
plt.figure(figsize=(12, 6))
plt.plot(denoised_signal_lp[:sample_to_plot])  # Plotting the first 3 second with each second 360 sample
plt.title("Low-Pass Filtered ECG Signal")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()
