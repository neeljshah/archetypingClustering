# 👥 Behavioral Archetyping & Unsupervised Persona Clustering
> **Using K-Means Clustering and Principal Component Analysis (PCA) to move beyond categorical labels into behavioral-driven persona segments.**

![Python](https://img.shields.io/badge/Analytics-Python_3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Unsupervised_Learning-orange?style=for-the-badge)
![Clustering](https://img.shields.io/badge/Algorithm-K--Means-blue?style=for-the-badge)
![Business](https://img.shields.io/badge/Focus-Customer_Segmentation-green?style=for-the-badge)

---

## 📖 Executive Summary
In both sports and enterprise marketing, traditional labels (e.g., "Guard/Forward" or "Demographic Age/Gender") are often misleading. This project utilizes **Unsupervised Machine Learning** to categorize 500+ entities based on **functional behavior** rather than pre-defined positions. By implementing **K-Means Clustering** and **PCA**, I identified 7 distinct "Archetypes" that describe how a player actually impacts the game, providing a roadmap for optimized portfolio (roster) construction.

---

## 🛠️ Business Analytics Translation
This project demonstrates the exact same methodology used in **User Persona & Marketing Analytics**:
*   **Player Archetypes** $\rightarrow$ **Customer Personas** (e.g., "The Power User," "The Bargain Hunter").
*   **Box Score Stats** $\rightarrow$ **User Engagement Metrics** (Clicks, Time-on-Page, Spend).
*   **Position (G/F/C)** $\rightarrow$ **Broad Demographics** (Location, Age).
*   **Roster Optimization** $\rightarrow$ **Product Bundle Optimization / Target Marketing**.

---

## 🚀 Key Project Phases

### 1. Feature Engineering & Scaling 🏗️
* **The Problem:** Raw stats (Points, Rebounds) have different scales. A player with 30 PTS and 0.5 BLK will confuse the model.
* **Technical Skill:** **Standardization (StandardScaler)** and Creating "Efficiency Ratios" (e.g., Assist-to-Turnover, Points-per-Possession).
* **The Code:** [🔗 View Pre-processing Script](./Scripts/Feature_Engineering.py)

### 2. K-Means Clustering & The Elbow Method 🗺️
* **The Problem:** How many groups *actually* exist? Too many is confusing; too few is vague.
* **Technical Skill:** **Within-Cluster Sum of Squares (WCSS)**, Elbow Curve analysis, and **Silhouette Scoring** to find the "Mathematical Sweet Spot" for segmentation.
* **The Result:** Discovered 7 distinct archetypes, including "3&D Specialists," "Rim Protectors," and "Primary Facilitators."
* **Visual Representation:**
> ![Clustering Chart Placeholder](https://via.placeholder.com/800x400?text=Insert+K-Means+Scatter+Plot+Here)

### 3. Dimensionality Reduction (PCA) 📊
* **The Problem:** Humans cannot visualize 15 different stats (dimensions) at once.
* **Technical Skill:** **Principal Component Analysis (PCA)** to compress 15 features into 2 "Principal Components" that retain 85% of the data's variance.
* **The Insight:** Visualized the "Distance" between player types to identify which archetypes are the most unique versus the most interchangeable.

### 4. Roster Value-Gap Analysis (SQL) 🚚
* **The Problem:** Are we overpaying for "Common" archetypes while underfunding "Rare" ones?
* **Technical Skill:** SQL Window Functions and Joins to compare **Salary vs. Archetype Average Performance.**
* **The Code:** [🔗 View ROI SQL Logic](./SQL/Value_Gap_Analysis.sql)

---

## 🛠️ Technical Mastery Checklist
- [x] **Unsupervised Learning:** Implementing K-Means from scratch using Scikit-Learn.
- [x] **Feature Normalization:** Ensuring skewed data doesn't bias the clustering algorithm.
- [x] **Cluster Interpretation:** Assigning business "Personas" to mathematical clusters.
- [x] **Business Storytelling:** Converting "Cluster 4" into **"The Defensive Anchor Persona."**

---

## 📂 Project Structure
```text
├── SQL/
│   ├── Value_Gap_Analysis.sql      # Salary vs. Archetype performance
│   └── Cluster_Distribution.sql    # Frequency of personas in the market
├── Scripts/
│   ├── Feature_Engineering.py      # Scaling and Ratio creation
│   ├── Clustering_Engine.py        # K-Means and Silhouette logic
│   └── PCA_Visualizer.py           # Dimensionality reduction charts
├── Visuals/
│   ├── Elbow_Curve.png             # Optimization chart
│   └── Archetype_Clusters.png      # Final 2D Persona map
└── README.md
