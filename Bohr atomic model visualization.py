import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to calculate electron positions based on the electron configuration
def calculate_electron_positions():
    electron_positions = []
    # Add positions for each shell according to the electron configuration of xenon
    shell_electrons = [0, 2, 8, 18, 32, 18, 6]
    shell_radii = [0, 1, 2, 3, 4, 5, 6]
    for shell, num_electrons in zip(shell_radii, shell_electrons):
        orbitals_per_shell = min(num_electrons, 84 - len(electron_positions))
        for i in range(orbitals_per_shell):
            angle = 2 * np.pi * i / orbitals_per_shell
            x = shell * np.cos(angle)
            y = shell * np.sin(angle)
            electron_positions.append((x, y))
            if len(electron_positions) == 84:
                break
    return np.array(electron_positions)

# Simulation parameters
electron_positions = calculate_electron_positions()
num_electrons = len(electron_positions)
num_frames = 200  # Number of animation frames
frame_interval = 100  # Interval between frames in milliseconds

# Create figure and axes with a black background
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_facecolor('black')
ax.set_xlim(-7, 7)
ax.set_ylim(-7, 7)

# Create nucleus with label Xe
nucleus = plt.Circle((0, 0), 0.5, color='red', zorder=10, label='Atomic Nucleus')
ax.add_artist(nucleus)
ax.text(0, 0, 'Xe', color='white', ha='center', va='center')

# Create electron representations
electrons = [plt.Circle((0, 0), 0.2, color='blue') for _ in range(num_electrons)]
for electron in electrons:
    ax.add_artist(electron)

# Create orbital lines for electrons (dotted lines)
orbital_lines = [plt.Circle((0, 0), r, color='white', fill=False, linestyle='dotted') for r in range(1, 7)]
for line in orbital_lines:
    ax.add_artist(line)

# Function to update electron positions and orbital lines for each frame
def update(frame):
    global electron_positions
    # Update electron positions
    angle = 2 * np.pi * frame / num_frames
    rotated_positions = electron_positions.dot([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    for electron, pos in zip(electrons, rotated_positions):
        electron.set_center(pos)
    return electrons + orbital_lines

plt.title("Bhor Atomic Model of Pollonium $Po_{209}^{84}$", font='times new roman', fontsize = '16', fontweight='bold')
ax.legend(handles=[electrons[0], nucleus], labels=['Electron', "Atom's Nucleus"], loc='upper right', fontsize='large')
# Create animation
ani = FuncAnimation(fig, update, frames=num_frames, interval=frame_interval, blit=True)
# Save the animation
# ani.save('xenon_electron_orbit_animation.mp4', writer='ffmpeg', fps=30)
plt.show()