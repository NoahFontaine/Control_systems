import numpy as np
import matplotlib.pyplot as plt

# Define the return ratio
def L(s):
    return 1/(s**3+s**2+2*s+1)

# Return Re and Im parts of L(jw)
def Re_Im(w):
    L_jw = L(1j*w)
    return L_jw.real, L_jw.imag

min = 0
max = 5
dw = 1e-3
omega = np.arange(min, max, dw)

Re, Im = Re_Im(omega)

fig, ax = plt.subplots()
# Set font to Times New Roman
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
# Center axis
plt.gca().spines[:].set_position('zero')
# Limit axis values
plt.xlim([-2, 2])
plt.ylim([-2, 2])
ax.set_aspect(1)
#Titles
plt.title("Nyquist plot of $\mathdefault{L(j\omega)}$", font="Times New Roman", fontweight="bold", fontsize = 11, loc = "right")
plt.xlabel("$\mathdefault{\mathbb{R}(L(j\omega))}$", font="Times New Roman", loc="right")
plt.ylabel("$\mathdefault{\mathbb{I}(L(j\omega))}$", font="Times New Roman", loc="top", rotation=0)
# Plot points
ax.plot(Re, Im, "blue")
ax.arrow(Re[int(max/(4*dw))], Im[int(max/(4*dw))], Re[int(max/(4*dw))+6]-Re[int(max/(4*dw))], Im[int(max/(4*dw))+6]-Im[int(max/(4*dw))], width=0.015, color="blue")
ax.arrow(Re[int(max/(7*dw))], Im[int(max/(7*dw))], Re[int(max/(7*dw))+20]-Re[int(max/(7*dw))], Im[int(max/(7*dw))+20]-Im[int(max/(7*dw))], width=0.015, color="blue")
plt.show()