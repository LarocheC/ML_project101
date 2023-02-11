#%%


import tkinter as tk
import tkinter.filedialog
import matplotlib.pyplot as plt
import librosa 
import librosa.display

import numpy as np
import wave

#%%
def plot_spectrogram(filename):
    # Load the audio file
    y, sr = librosa.load(filename)

    # Compute the spectrogram
    S = librosa.stft(y)

    # Plot the spectrogram
    librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), sr=sr, y_axis='log', x_axis='time')
    plt.axis('tight')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()


#%%

# Create the GUI
root = tk.Tk()
root.title('Spectrogram Viewer')

# Add a file chooser
file_chooser = tk.filedialog.Open(root, filetypes=[('Audio Files', '.wav .mp3 .ogg')])

# Add a button to plot the spectrogram
plot_button = tk.Button(root, text='Plot Spectrogram', command=lambda: plot_spectrogram(file_chooser.show()))
plot_button.pack()

# Start the GUI
root.mainloop()
