import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define the transfer function, where s is a complex number
def G(s):
    return s/(s**3+s**2+2*s+1)

# Define maximum values of ||G(s)||, Re(s), and Im(s)
max = 2
re_max = 2
im_max = 2

# Data for Re(s) = omega and Im(s) = jw
omega = np.arange(-re_max, re_max, 0.01)
jw = 1j*np.arange(-im_max, im_max, 0.01)
omega, jw = np.meshgrid(omega, jw)

# Data for ||G(s)||
t_func = abs(G(omega+jw))

# Remove all ||G(s)|| outside range defined
for i in range(len(t_func)):
    for j in range((len(t_func[i]))):
        if t_func[i][j] > max:
            t_func[i][j] = max

# Plot
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
# Set font to Times New Roman
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman"]
# Set limits to the axis
ax.set_xlim([-re_max, re_max])
ax.set_ylim([-im_max, im_max])
ax.set_zlim([0, max])
# Titles, axis and ticks (to make cleaner)
ax.set_title("Plot of $\mathdefault{||G(s)||}$ on a linear scale in complex space", font="Times New Roman", fontweight="bold", fontsize = 11)
ax.set_xlabel("$\mathdefault{\mathbb{R}(s)}$", font="Times New Roman")
ax.set_ylabel("$\mathdefault{\mathbb{I}(s)}$", font="Times New Roman")
ax.set_zlabel("$\mathdefault{||G(s)||}$", font="Times New Roman")
x_ticks = np.linspace(-re_max, re_max, 5)
y_ticks = np.linspace(-im_max, im_max, 5)
z_ticks = np.linspace(0, max, 5)
ax.set_xticks(x_ticks)
ax.set_yticks(y_ticks)
ax.set_zticks(z_ticks)
ax.set_xticklabels(x_ticks, rotation=0, font="Times New Roman")
ax.set_yticklabels(y_ticks, rotation=0, font="Times New Roman")
ax.set_zticklabels(z_ticks, rotation=0, font="Times New Roman")
# Plot graph and legend
plot = ax.plot_surface(omega, jw.imag, t_func, vmin = 0,  vmax = max, cmap = cm.RdBu)
fig.colorbar(plot, shrink=0.4, aspect=10, label='$\mathdefault{||G(s)||}$')
plt.show()