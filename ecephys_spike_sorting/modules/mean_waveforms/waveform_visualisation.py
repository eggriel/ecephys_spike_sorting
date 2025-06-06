import numpy as np
import matplotlib.pyplot as plt

def plot_mean_2d_waveform(mean_2d_waveform, title="Mean 2D Waveform", time_axis=None):
    """
    Plot the mean 2D waveform: each channel's waveform over time.

    Parameters:
    - mean_2d_waveform: np.ndarray of shape (n_channels, n_timepoints)
    - title: Optional title for the plot
    - time_axis: Optional 1D array of time values (same length as n_timepoints)
    """
    n_channels, n_timepoints = mean_2d_waveform.shape

    if time_axis is None:
        time_axis = np.arange(n_timepoints)

    plt.figure(figsize=(12, 6))
    for ch in range(n_channels):
        plt.plot(time_axis, mean_2d_waveform[ch, :] + ch * 1000, label=f'Channel {ch}')
        # Offset each waveform vertically for clarity (adjust 100 as needed)

    plt.xlabel("Time (samples)")
    plt.ylabel("Amplitude + Channel offset")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()