# 🧬 Behavioral Archetyping
### Part 4 of the Basketball Intelligence Suite

> **Clustering players by *how* they play — not just how much — to reveal functional identity beyond box score labels.**

---

## 📸 Dashboard Preview

![Behavioral Archetyping Dashboard](demo.gif)

> *Interactive Power BI dashboard — filter by Team and Player to explore shot profiles, entropy, and tactical classification.*

https://github.com/user-attachments/assets/826387bd-2d60-445d-a724-c76f3babdf90


---


## 🔍 What This Project Does

"Shooting guard" means nothing. Is he a pull-up creator? A catch-and-shoot specialist? A paint finisher who can stretch to midrange? The **Behavioral Archetyping** model uses unsupervised machine learning to answer that question — grouping players by their actual shot behavior rather than their listed position.

The result is a set of **functional archetypes** (Above the Break, Left Tree, MidRange, Paint, RA, Right Three) that reveal *how* a player operates, plus an **Entropy Score** and **Tactical Mode** that classify how predictable or versatile their game is.

---

## 📊 Dashboard Breakdown

### Sum of Offensive Value — Scatter Plot
- **X-axis:** Total Shot volume across the season
- **Y-axis:** Offensive Value — net expected value generated per shot above baseline
- **Color-coded by Archetype:** Each cluster color represents a distinct shot profile
- Players clustered in the **top-right** = high-volume, high-value archetypes (elite contributors)
- Outliers reveal players whose archetype is mismatched with their role

### Shot Selection — Radar Chart
- A polygon radar spanning 6 court zones: Right Corner 3, Mid-Range, In The Paint, Restricted Area, Left Corner 3, Above the Break 3
- **Shape of the polygon = the player's shot signature**
- A wide, balanced polygon = versatile scorer; a spiked polygon = hyper-specialized
- Updates dynamically per player selection

### Entropy Percent
- A spatial entropy score measuring **shot unpredictability**
- Low entropy = a player who always goes to the same spot (easy to scout)
- High entropy = a player who attacks from everywhere (defensive nightmare)
- Displayed as a visual half-court bubble map — larger, central bubble = higher entropy concentration

### Versatility Map
- A compact court scatter showing shot distribution across all zones
- Accompanied by two key callouts:
  - **Tactical Mode** — e.g., *"Elite Versatility"*, *"Paint Specialist"*, *"Corner 3 Sniper"*
  - **Complexity Score** — a single float (e.g., 1.59) encoding how multi-dimensional the player's offensive game is

---

## ⚙️ Tech Stack

| Tool | Usage |
|---|---|
| **Python (Scikit-Learn)** | K-Means clustering, PCA dimensionality reduction |
| **Python (Pandas, NumPy)** | Shot zone feature engineering, entropy calculation |
| **Power BI** | Dashboard, radar chart, DAX archetype labeling |
| **NBA Stats API** | Shot-level coordinate and zone data |

---

## 🧠 Key Insight

> **Amir Coffey** (Brooklyn Nets era) shows a **Complexity Score of 1.59** and a **Tactical Mode of Elite Versatility** — meaning his shot selection is genuinely hard to predict and defend. Contrast this with a player like a classic rim-runner whose radar chart spikes only toward the paint and RA zones, making their game far easier to scheme against.

---

## 🧮 Clustering Methodology

```
Step 1: Feature Engineering
  - Shot zone frequency vectors (6 zones per player)
  - FG% per zone, shot volume normalization

Step 2: Dimensionality Reduction
  - PCA → reduce to 2 principal components for visualization

Step 3: K-Means Clustering
  - K = 6 archetypes (tuned via elbow method + silhouette score)
  - Archetype labels assigned post-hoc via centroid interpretation

Step 4: Entropy Scoring
  - Shannon entropy applied to shot zone distribution vector
  - Normalized to 0–1 scale (0 = fully predictable, 1 = fully random)
```

---

## 🚀 How to Use

1. Clone the repo and open the `.pbix` file in Power BI Desktop
2. Select a **Team** from the dropdown, then drill into individual **Players**
3. The Radar Chart, Entropy Map, and Versatility Map all update per selection
4. Use the Offensive Value scatter to compare archetypes league-wide
5. Cross-reference Tactical Mode + Complexity Score for roster construction insights

---

## 📁 Repository Structure

```
Player-Archetypes/
├── data/
│   └── shot_zones_cleaned.csv
├── notebooks/
│   └── clustering_pipeline.ipynb
├── dashboard/
│   └── BehavioralArchetyping.pbix
└── README.md
```

---

## 🔗 Part of the Basketball Intelligence Suite

| Part | Project | Focus |
|---|---|---|
| **1** | Spatial Efficiency Engine | Shot quality & creation mapping |
| **2** | Momentum Volatility Index | Game-flow & run detection |
| **3** | Defensive Gravity Model | Off-ball spatial influence |
| **4** | Behavioral Archetyping *(you are here)* | Player segmentation & style |
