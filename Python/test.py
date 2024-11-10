import wfdb
import matplotlib.pyplot as plt
from noise_generator import generate_60hz_noise  # Importing the noise generator


# Load the ECG record
record_name = 'mit-bih-arrhythmia-database-1.0.0/101'  #set the path for a specific record in here file 100
record = wfdb.rdrecord(record_name, sampfrom=0, channels=[0])  # rerecord is to read the spcificed ECG recor

# Extract the signal data
signal = record.p_signal[:, 0]  # Ensure we're using the correct channel

# how many sample to plot? 
secods= 4
sample_to_plot = secods * 360 #sampling rate is 360 was provided on the MIT-BIH Arrhythmia 

# Plot the raw signal
plt.figure(figsize=(12, 6))
plt.plot(signal[:sample_to_plot])  # Plotting the first 3 second with each second 360 sample 
plt.title("ECG Signal from Record 100 (First 3 seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()

# Generate 60 Hz noise and add it to the signal
noise = generate_60hz_noise(len(signal), sampling_rate=360)
noisy_signal = signal + noise

# Plot the noisy signal
plt.figure(figsize=(12, 6))
plt.plot(noisy_signal[:sample_to_plot])  # Plotting the first 3 seconds (360 samples per second)
plt.title("Noisy ECG Signal from Record 100 (First 3 seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()
