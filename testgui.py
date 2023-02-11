import librosa
import librosa.display
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the audio file
filename = r'C:\Users\cleme\Desktop\OldSongs\voicing.wav'
y, sr = librosa.load(filename)

# Compute the spectrogram
S = librosa.stft(y)

# Create the GUI window
window = Tk()
window.title("Spectrogram Viewer")

# Create the spectrogram plot
fig, ax = plt.subplots()
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max), sr=sr, y_axis='log', x_axis='time')

# Create a Tkinter canvas to display the plot
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# Create a label and entry widget to allow changing the number of samples
sample_label = Label(window, text="Number of Samples:")
sample_label.pack(side=LEFT)
sample_entry = Entry(window)
sample_entry.pack(side=LEFT)

# Create a function to update the spectrogram plot
def update_spectrogram():
    num_samples = int(sample_entry.get())
    fig, ax = plt.subplots()
    librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y, n_fft=num_samples), ref=np.max), sr=sr, y_axis='log', x_axis='time')
    canvas.figure = fig
    canvas.draw()

# Create a button to trigger the update function
update_button = Button(window, text="Update", command=update_spectrogram)
update_button.pack(side=LEFT)

# Start the GUI event loop
window.mainloop()