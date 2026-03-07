import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 1. HANDLE EMPTY DATA
if dataset.empty:
    fig, ax = plt.subplots(figsize=(5, 4.7))
    fig.patch.set_facecolor('#141414')
    ax.set_facecolor('#141414')
    plt.text(0, 200, "SELECT A PLAYER", color='grey', ha='center')
    plt.axis('off')
    plt.show()
else:
    # 2. PREPARE DATA
    df = dataset.copy()
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    avg_stats = df[numeric_cols].mean().fillna(0)

    # 3. DEFINE ZONE ANCHORS
    # We place orbs at the core of each shooting zone
    zone_anchors = [
        {'name': 'Restricted Area', 'coord': [0, 15], 'color': '#FF4B4B'}, # Red (Rim)
        {'name': 'In the Paint', 'coord': [0, 90], 'color': '#FF8C00'}, # Orange (Paint)
        {'name': 'MidRange', 'coord': [0, 170], 'color': '#FFD700'}, # Gold (Mid)
        {'name': 'Left Corner Three', 'coord': [-225, 20], 'color': '#00FFCC'}, # Neon Green (3pt)
        {'name': 'Right Corner Three', 'coord': [225, 20], 'color': '#00FFCC'},
        {'name': 'Above the Break Threes', 'coord': [0, 270], 'color': '#00FFCC'}
    ]

    # 4. SETUP PLOT
    fig, ax = plt.subplots(figsize=(5, 4.7))
    fig.patch.set_facecolor('#141414')
    ax.set_facecolor('#141414')

    # 5. DRAW COURT LINES (Faint for "Glass" effect)
    plt.plot([-250, 250], [0, 0], color='white', lw=1, alpha=0.2) # Baseline
    three_arc = plt.Circle((0, 0), 237.5, color='white', fill=False, lw=1.5, alpha=0.1)
    ax.add_patch(three_arc)

    # 6. PLOT RADIANCE ORBS
    for anchor in zone_anchors:
        weight = avg_stats.get(anchor['name'], 0)
        
        if weight > 0.02: # Only show zones with > 2% usage
            # The "Core" of the orb
            plt.scatter(anchor['coord'][0], anchor['coord'][1], 
                        s=weight*5000, color=anchor['color'], alpha=0.7, edgecolors='white', lw=1, zorder=3)
            
            # The "Radiance/Glow" (Multiple layers for a neon effect)
            plt.scatter(anchor['coord'][0], anchor['coord'][1], 
                        s=weight*15000, color=anchor['color'], alpha=0.2, zorder=2)
            plt.scatter(anchor['coord'][0], anchor['coord'][1], 
                        s=weight*30000, color=anchor['color'], alpha=0.05, zorder=1)
            
            # Data Label (Percentage)
            plt.text(anchor['coord'][0], anchor['coord'][1]-40, f"{int(weight*100)}%", 
                     color='white', fontsize=8, ha='center', fontweight='bold', alpha=0.8)

    # 7. CONNECT ACTIVE ZONES (The "Bag" Lines)
    # Draws lines between any zones the player uses heavily (>15%)
    active_zones = [a for a in zone_anchors if avg_stats.get(a['name'], 0) > 0.15]
    for i in range(len(active_zones)):
        for j in range(i + 1, len(active_zones)):
            plt.plot([active_zones[i]['coord'][0], active_zones[j]['coord'][0]],
                     [active_zones[i]['coord'][1], active_zones[j]['coord'][1]],
                     color='white', alpha=0.1, lw=1, linestyle='--')

    # 8. FORMATTING
    plt.xlim(-250, 250)
    plt.ylim(-50, 450)
    plt.axis('off')
    
    # Header logic
    player_name = dataset['PLAYER_NAME'].iloc[0] if 'PLAYER_NAME' in dataset.columns else "Team Profile"
    plt.text(-240, 430, player_name.upper(), color='white', fontsize=12, fontweight='black')

    plt.show()
