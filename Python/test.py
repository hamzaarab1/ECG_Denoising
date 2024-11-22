import wfdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from noise_generator import generate_60hz_noise
from snr_calculator import calculate_snr
from prd_calculator import calculate_prd
from rmse_calculator import calculate_rmse
from lowpass_filter import lowpass_filter

results = []# An empty list to store results

# Define the ranges of records to process
ranges = [range(100, 106), range(200, 206)]  # Specify the record ranges

for record_range in ranges:
    for record_id in record_range:
        record_name = f'mit-bih-arrhythmia-database-1.0.0/{record_id}'

        try:
            # Load the ECG record
            record = wfdb.rdrecord(record_name, sampfrom=0, channels=[0])
        except FileNotFoundError: #if a file doesn't exist
            continue

        # Extract the signal data
        original_signal = record.p_signal[:, 0]

        # Generate noise and add it to the signal
        sampling_rate = 360
        frequency = 60
        amplitude = 0.0985
        harmonics = None 
        noise = generate_60hz_noise(len(original_signal), sampling_rate, frequency, amplitude, harmonics)
        noisy_signal = np.array(original_signal) + np.array(noise)

        # Calculate metrics
        input_snr = calculate_snr(np.array(original_signal), np.array(noisy_signal), np.zeros_like(original_signal))
        denoised_signal_lp = lowpass_filter(noisy_signal)
        improved_snr = calculate_snr(np.array(original_signal), np.array(noisy_signal), np.array(denoised_signal_lp))
        prd_value = calculate_prd(np.array(original_signal), np.array(denoised_signal_lp))
        rmse_value = calculate_rmse(np.array(original_signal), np.array(denoised_signal_lp))

        # Store the results
        results.append({
            "ECG Record": record_id,
            "Input SNR (dB)": f"{input_snr:.2f}",
            "Improved SNR (dB)": f"{improved_snr:.2f}",
            "PRD": f"{prd_value:.4f}",
            "RMSE": f"{rmse_value:.4f}"
        })

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Display the table as text in the console
print("\nLowpass Filter")
print(df)

# Save the table as a CSV file (excel file)
df.to_csv("ecg_results.csv", index=False)

# Render the table as an image using matplotlib
fig, ax = plt.subplots(figsize=(10, 4))  # Adjust size as needed
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# Save the table as an image
plt.savefig("ecg_results_table.png", bbox_inches='tight', dpi=300)
plt.show()
