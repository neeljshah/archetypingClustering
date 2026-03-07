import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Prepare the data - we remove ARCHETYPE_CLUSTER and ENTROPY_SCORE to plot only %
cols_to_plot = [c for c in dataset.columns if c not in ['ARCHETYPE_CLUSTER', 'ENTROPY_SCORE', 'TOTAL_FGA', 'PLAYER_NAME']]
plot_data = dataset[cols_to_plot].mean()

labels = plot_data.index.tolist()
stats = plot_data.values.tolist()

# Close the circle
num_vars = len(labels)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
stats += stats[:1]
angles += angles[:1]
labels += labels[:1]

# Create the Radar Plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw the shape
ax.fill(angles, stats, color='#FFD700', alpha=0.4) # Gold fill
ax.plot(angles, stats, color='#FFD700', linewidth=2) # Gold border

# Styling
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels[:-1], fontsize=9, color='white', fontweight='bold')

# Dark Theme aesthetics
fig.patch.set_facecolor('#141414')
ax.set_facecolor('#141414')
ax.spines['polar'].set_color('grey')
ax.grid(color='grey', linestyle='--', alpha=0.5)

plt.show()
