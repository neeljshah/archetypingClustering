import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. HANDLE EMPTY DATA
if dataset.empty:
    fig, ax = plt.subplots(figsize=(5, 4.7))
    fig.patch.set_facecolor('#141414')
    ax.set_facecolor('#141414')
    plt.text(0, 200, "SELECT PLAYER", color='grey', ha='center')
    plt.axis('off')
    plt.show()
else:
    # 2. PREPARE DATA
    df = dataset.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    avg_stats = df[numeric_cols].mean().fillna(0)

    # 3. DEFINE DISPLACEMENT ANCHORS (Amplified for movement)
    # We move the 3pt anchors further out to "stretch" the visual
    anchors = {
        'Restricted Area': [0, 0],             # The Base
        'In the Paint': [0, 80],
        'MidRange': [0, 180],
        'Left Corner Three': [-240, 50],
        'Right Corner Three': [240, 50],
        'Above the Break Threes': [0, 380]     # High vertical pull
    }

    # 4. CALCULATE DISPLACED HUB (Using Exponentiated Weights)
    # Raising weights to power of 1.5 makes small differences cause LARGE movement
    cx, cy = 0, 0
    total_weight = 0
    for zone, coord in anchors.items():
        w = avg_stats.get(zone, 0)
        amplified_w = w ** 1.5 
        cx += coord[0] * amplified_w
        cy += coord[1] * amplified_w
        total_weight += amplified_w

    if total_weight > 0:
        cx /= total_weight
        cy /= total_weight
    else:
        cx, cy = 0, 0

    # 5. SETUP PLOT
    fig, ax = plt.subplots(figsize=(5, 4.7))
    fig.patch.set_facecolor('#141414')
    ax.set_facecolor('#141414')

    # 6. DRAW TACTICAL GRID (Faint background lines)
    for r in [100, 200, 300, 400]:
        circle = plt.Circle((0, 0), r, color='white', fill=False, lw=0.5, alpha=0.1, linestyle='--')
        ax.add_patch(circle)

    # 7. DRAW THE VERSATILITY FIELD (Entropy Ripples)
    entropy = avg_stats.get('ENTROPY_SCORE', 0.5)
    # More versatile = more ripples and larger glow
    ripple_colors = ['#00FFCC', '#00CCFF', '#FFD700'] # Cyan to Gold
    for i in range(1, 5):
        ripple_size = (entropy * 800) * (i * 0.5)
        plt.scatter(cx, cy, s=ripple_size, color=ripple_colors[i%3], alpha=0.1 / i, zorder=1)

    # 8. THE TACTical PULSE (The Core)
    # Pulse color shifts from Blue (Interior) to Neon Green (Perimeter)
    pulse_color = '#00FFCC' if cy > 150 else '#FF4B4B'
    if cy > 150 and abs(cx) < 50: pulse_color = '#FFD700' # Gold for Mid-range/Pure skill
    
    plt.scatter(cx, cy, s=250, color=pulse_color, edgecolors='white', lw=2, zorder=5)
    plt.scatter(cx, cy, s=600, color=pulse_color, alpha=0.3, zorder=4)

    # 9. ANCHOR LABELS
    for zone, coord in anchors.items():
        val = int(avg_stats.get(zone, 0) * 100)
        if val > 5: # Only label zones with impact
            plt.text(coord[0], coord[1], f"{val}%", color='white', alpha=0.4, fontsize=8, ha='center')

    # 10. FORMATTING
    plt.xlim(-280, 280)
    plt.ylim(-50, 480)
    plt.axis('off')
    
    # Text Analysis
    status = "ELITE VERSATILITY" if entropy > 1.4 else "SPECIALIZED THREAT"
    plt.text(-260, 440, f"TACTICAL MODE: {status}", color='white', fontsize=10, fontweight='bold')
    plt.text(-260, 415, f"COMPLEXITY SCORE: {entropy:.2f}", color=pulse_color, fontsize=9)

    plt.show()
