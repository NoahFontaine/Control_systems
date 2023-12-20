import numpy as np
import matplotlib.pyplot as plt

# Define the return ratio
def L(s):
    return 100/(s**3+s**2+2*s+1)

# Return magnitude of L(jw)
def Gain(w):
    L_jw = L(1j*w)
    return 20*np.log10(abs(L_jw))

# Return phase of l(jw)
def Phase(w):
    L_jw = L(1j*w)
    return np.angle(L_jw, deg=True)

min = -1
max = 2 #10e2 rad/s
number = 100
omega = np.logspace(min, max, number)

A = Gain(omega)
angle = Phase(omega)

print(omega)

fig = plt.figure()
# Set font to Times New Roman
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
# ax is gain, ay is phase
ax = fig.add_subplot(2, 1, 1)
ay = fig.add_subplot(2, 1, 2)
#Titles
ax.set_title("Bode plot of the gain of $\mathdefault{L(j\omega)}$", font="Times New Roman", fontweight="bold", fontsize = 11)
ay.set_title("Bode plot of the phase of $\mathdefault{L(j\omega)}$", font="Times New Roman", fontweight="bold", fontsize = 11)
# Center dB axis
ax.spines[['top', 'right']].set_visible(False)
ax.spines[['bottom']].set_position('center')
ay.spines[['top', 'right']].set_visible(False)
ay.spines[['bottom']].set_position('center')
# Limit axis values
ax.set_xscale("log")
ax.set_xlabel("Frequency $\mathdefault{\omega}$ (rad.s$\mathdefault{^{-1}})$", font="Times New Roman")
ax.set_ylabel("$\mathdefault{||L(j\omega)||}$ (dB)", font="Times New Roman")
ay.set_xscale("log")
ay.set_xlabel("Frequency $\mathdefault{\omega}$ (rad.s$\mathdefault{^{-1}})$", loc = "right", font="Times New Roman")
ay.set_ylabel("$\mathdefault{\phi}$ $\mathdefault{(L(j\omega))}$ (degrees)", font="Times New Roman")
# Plot graphs
ax.plot(omega, A, "blue")
ay.plot(omega, angle, "red")
plt.show()
