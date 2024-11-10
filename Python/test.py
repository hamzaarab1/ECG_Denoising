import wfdb
import matplotlib.pyplot as plt

# Load the ECG record
record_name = 'mit-bih-arrhythmia-database-1.0.0/101'  #set the path for a specific record in here file 100
record = wfdb.rdrecord(record_name, sampfrom=0, channels=[0])  # rerecord is to read the spcificed ECG recor

# Extract the signal data
signal = record.p_signal[:, 0]  # Ensure we're using the correct channel

# Plot the signal
plt.figure(figsize=(12, 6))
plt.plot(signal[:1050])  # Plotting the first 3 second with each second 360 sample 
plt.title("ECG Signal from Record 100 (First 3 seconds)")
plt.xlabel("Sample Number")
plt.ylabel("Amplitude (mV)")
plt.show()