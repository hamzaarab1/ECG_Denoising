import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import pandas as pd  # For creating a table of R-peak coordinates

def detect_r_peaks(file_path, samples_to_plot=1000):
    # Load the ECG record
    record = wfdb.rdrecord(file_path)
    ecg_signal = record.p_signal[:, 0]  # Assuming channel 0 contains the raw signal

    # Detect R-peaks using find_peaks from SciPy
    peaks, _ = find_peaks(ecg_signal, height=0.6, distance=200)  # Adjust height and distance as needed

    # Create a DataFrame to store R-peak information
    r_peak_table = pd.DataFrame({
        'R-Peak': [f'R{i+1}' for i in range(len(peaks))],  # R1, R2, R3, etc.
        'Index (Sample)': peaks,  # The index (sample number) of each R-peak
        'Amplitude (mV)': ecg_signal[peaks]  # The amplitude (mV) of each R-peak
    })

    # Display the table of R-peak coordinates
    print(r_peak_table)

    # Plot the ECG signal with R-peaks labeled
    plt.figure(figsize=(10, 4))
    
    # Modify the plot to display up to the number of samples specified by `samples_to_plot`
    plt.plot(ecg_signal[:samples_to_plot], label='Raw ECG Signal', color='blue')

    # Mark and label the R-peaks on the graph
    for r_peak in peaks:
        if r_peak < samples_to_plot:  # Only mark peaks within the displayed range
            plt.text(r_peak, ecg_signal[r_peak], 'R', fontsize=12, color='red', ha='center')

    # Add labels and grid
    plt.title(f'ECG Signal with R-Peaks (Showing {samples_to_plot} samples)')
    plt.xlabel('Time (samples)')
    plt.ylabel('ECG (mV)')
    plt.legend()
    plt.grid()

    # Show the plot
    plt.show()
