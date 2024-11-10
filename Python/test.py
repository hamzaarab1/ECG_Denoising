
import wfdb
import matplotlib.pyplot as plt
from detect_r_peaks import detect_r_peaks
from fft import fft_analysis
from bandstop_filter import apply_bandstop_filter

# Load the ECG record
file_path = 'C:/Users/hamza/Desktop/Library Desktop/Python311/rec_1'
record = wfdb.rdrecord(file_path)
samples = 3000

# Assume channel 0 is the raw, unfiltered signal
raw_signal = record.p_signal[:, 0]
detect_r_peaks('C:/Users/hamza/Desktop/Library Desktop/Python311/rec_1', samples)
fft_analysis(raw_signal, sampling_rate=500, samples_to_plot=samples)


# Apply the bandstop filter to your ECG signal
filtered_signal = apply_bandstop_filter(raw_signal, sampling_rate=500, notch_freq=50, quality_factor=30, samples_to_plot=samples)

# Optionally, you can run the FFT analysis on the filtered signal
fft_analysis(filtered_signal, sampling_rate=500, samples_to_plot=samples)


 







# Plot the raw ECG signal
# plt.figure(figsize=(10, 4))
# plt.plot(raw_signal[:1100], label='Raw ECG Signal', color='blue')
# plt.title('Raw ECG Signal (Zoomed)')
# plt.xlabel('Time (samples)')
# plt.ylabel('ECG (mV)')
# plt.legend()
# plt.grid()
# plt.show()

# Now, call the function from detect_r_peaks.py to detect R-peaks



# # Plot the filtered ECG signal separately
# plt.figure(figsize=(10, 4))
#filtered_signal = record.p_signal[:, 0]  # Assuming channel 0 is used for filtering
# plt.plot(filtered_signal[:1000], label='Filtered ECG Signal', color='orange')
# plt.title('Filtered ECG Signal (Zoomed)')
# plt.xlabel('Time (samples)')
# plt.ylabel('ECG (mV)')
# plt.legend()
# plt.grid()
# plt.show()

# #Plotting both at the same time 
# import wfdb
# import matplotlib.pyplot as plt
# # Load the ECG record
# record = wfdb.rdrecord('C:/Python311/rec_1')
# # plot both
# plt.figure(figsize=(10, 4))
# plt.plot(record.p_signal[:600], label='Raw ECG Signal')
# # Add plot details
# plt.title('Raw ECG Signal (Zoomed)')
# plt.xlabel('Time (samples)')
# plt.ylabel('ECG (mV)')
# plt.legend()
# plt.grid()
# # Show the plot
# plt.show()
