import numpy as np
import matplotlib.pyplot as plt

# Define parameters
A0 = 1  # initial action or output
delta = 0.2  # feedback adjustment coefficient (increased for sharper changes)
time = np.linspace(0, 20, 200)  # time range (more points for smoother curves)

# Generate feedback with a steeper exponential decay
feedback_stabilized = np.sin(time) * np.exp(-0.2 * time)  # Sharper decay for higher sharpness

# Calculate action with the sharper feedback
action_stabilized = A0 * (1 + delta * feedback_stabilized)

# Plot the graph
plt.figure(figsize=(12, 8))

# Plot the stabilized action line
plt.plot(time, action_stabilized, label="Action (A(t))", color='blue', linewidth=2)

# Plot the stabilized feedback line
plt.plot(time, feedback_stabilized, label="Feedback (F(t))", color='orange', linestyle='--', linewidth=1.5, alpha=0.8)

# Add labels, title, and styling
plt.title("Dynamic Feedback Loop with Sharpened Stabilization", fontsize=16, fontweight='bold')
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Action/Feedback", fontsize=14)

# Add grid, legend, and stabilization annotations
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
plt.axhline(y=0, color='black', linewidth=0.8, alpha=0.6)  # Baseline
plt.legend(fontsize=12, loc='upper right')

# Add annotation for "Sharp Stabilization" below the line
plt.annotate("Sharp Stabilization", xy=(18, action_stabilized[-1]), xytext=(15, action_stabilized[-1] - 0.3),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5), fontsize=12)

# Add annotation for "Steep Feedback Decay"
plt.annotate("Steep Feedback Decay", xy=(18, feedback_stabilized[-1]), xytext=(15, feedback_stabilized[-1] - 0.2),
             arrowprops=dict(facecolor='orange', arrowstyle='->', lw=1.5), fontsize=12, color='orange')

plt.show()
