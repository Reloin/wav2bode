from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

#read wave frequency response 
sr, data = wavfile.read('D:\Downloads\THU\电电实验\实验三\q2-1.wav')

#removing blank before sweep, actually could be ignored
n = 1
while abs(data[n][0]) < 10:
    n = n+1
data = data[n:]
n = data.shape[0]

#using scipy to convert sweep into complex signal form
w, h = signal.freqz(data[:,1], data[:,0])
x = w * sr * 1.0 / (2 * np.pi)
y = 20 * np.log10(abs(h))

#plotting raw data
plt.figure(1, figsize=(10, 5))
plt.plot(data)
plt.title("")
plt.xlabel("Time")
plt.ylabel("Amplitude from sound card")
plt.grid(which='both', linestyle='-', color='grey')

#plotting amplitude
plt.figure(2, figsize=(10, 5))
plt.semilogx(x,y)
plt.ylim([-20,20]) #limiting y-axis for 
plt.title("Frequency response of circuit 1")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude (dB)")
plt.axhline(-3, color = "red", linestyle = 'dashed')
plt.grid(which='both', linestyle='-', color='grey')
plt.show()
#plotting phase shift
angles = np.unwrap(np.angle(h))
plt.figure(3, figsize=(10, 5))
plt.semilogx(x,angles*180/np.pi)
plt.ylim([-200,200])
plt.title("Frequency response of circuit 1")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (deg)")
plt.grid(which='both', linestyle='-', color='grey')
plt.show()