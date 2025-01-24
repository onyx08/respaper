import numpy as np
import matplotlib.pyplot as plt

# Parameters for the equation
U0 = 1.0  # Initial support level
lambda_ = 0.5  # Rate of reduction in support
time_steps = np.linspace(0, 10, 100)  # Continuous time from 0 to 10
steps = np.arange(0, 11, 1)  # Discrete time steps from 0 to 10

# Equation for support reduction over time
support_levels = U0 * np.exp(-lambda_ * time_steps) * 100  # Continuous support as percentage
support_levels_steps = U0 * np.exp(-lambda_ * steps) * 100  # Step-wise support as percentage

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.step(steps, support_levels_steps, label='Step-wise Support Reduction', color='orange', linewidth=2, where='post')
plt.plot(time_steps, support_levels, label='Continuous Support Reduction', color='blue', linestyle='--', linewidth=1.5)
plt.title('Reduction in Support Over Time (100% to 0%)', fontsize=14)
plt.xlabel('Time (t)', fontsize=12)
plt.ylabel('Support Level (% U(t))', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

# Save the graph as a high-DPI PNG
plt.savefig("graph.png", dpi=300)  # Adjust DPI (300 is standard for high quality)
plt.show()
