# Scouting Engine: Advanced Baseball Analytics Suite

**Organization:** Guelph Royals (CBL)
**Status:** In Development / Active Research

---

## Overview

The **Scouting Engine** is an end-to-end machine learning and analytics platform designed to convert raw broadcast-tracked pitch data into actionable insights for player development and in-game strategy.

Developed in collaboration with the Guelph Royals, this system automates the workflow from manual data collection to advanced modeling and visualization. The platform enables coaching staff to evaluate pitch effectiveness, identify hitter weaknesses, and support data-driven decision-making.

---

## Key Outcomes

* Developed a supervised learning model to estimate swing-and-miss (whiff) probability at the pitch level
* Built an unsupervised clustering pipeline to quantify pitch tunneling and deception
* Delivered an interactive dashboard used for exploratory analysis and scouting insights
* Established a reproducible ETL pipeline for ingesting and standardizing manually tracked data

---

## Tech Stack

| Layer          | Technology                                                           |
| -------------- | -------------------------------------------------------------------- |
| Backend        | Python 3.11, Pandas, NumPy, Scikit-Learn, XGBoost, Google Sheets API |
| Frontend       | Streamlit, Plotly, Matplotlib                                        |
| Infrastructure | GitHub Actions, Streamlit Cloud, Dotenv                              |

---

## System Architecture

1. **Data Ingestion**

   * Manual pitch tracking data collected from broadcast footage
   * Automated retrieval via Google Sheets API

2. **Data Preprocessing**

   * Cleaning and validation of raw inputs
   * Coordinate normalization to a standardized strike zone
   * Feature engineering for model input

3. **Modeling Layer**

   * Supervised learning for whiff probability prediction
   * Unsupervised clustering for pitch tunneling analysis

4. **Visualization Layer**

   * Streamlit dashboard for interactive exploration
   * Heatmaps, trajectory plots, and player-level filtering

---

## Core Features

### Predictive Whiff Modeling

* Supervised learning models (Random Forest, XGBoost)
* Predicts probability of a swing-and-miss using:

  * Pitch type
  * Location (x, y coordinates)
* Evaluated using:

  * Log-Loss
  * AUC-ROC

---

### Pitch Tunneling Analysis

* K-Means clustering applied to pitch trajectories and release points
* Quantifies similarity between pitch types early in flight
* Provides a proxy measure of pitcher deception

---

### Interactive Scouting Dashboard

* Built with Streamlit for accessibility and usability
* Features include:

  * Strike zone heatmaps
  * Pitch trajectory visualizations
  * Player and pitch-type filters

---

### Automated ETL Pipeline

* Python-based ingestion and transformation workflows
* Integration with Google Sheets API
* Ensures consistent formatting and reproducibility

---

## Feature Engineering

Key inputs to the modeling pipeline include:

* Pitch location (normalized coordinates)
* Pitch type
* Release point (if available)
* Velocity and movement differentials (if available)

These features enable the model to capture both spatial and contextual factors influencing swing-and-miss outcomes.

---

## Model Evaluation

Models are evaluated using a structured validation approach:

* Train/test split to prevent data leakage
* Classification metrics:

  * Log-Loss for probabilistic accuracy
  * AUC-ROC for discrimination performance

Future iterations will incorporate cross-validation and temporal validation strategies.

---

## Data Considerations

* Data is manually tracked from broadcast footage and may include measurement noise
* Camera angle variability necessitates coordinate normalization
* Sample sizes may be limited depending on player and game availability

---

## Project Structure

```plaintext
Scouting-Engine/
├── data/               # Raw and processed tracking data
├── models/             # Serialized ML models (.pkl files)
├── notebooks/          # EDA and prototyping
├── src/                # Core logic (ETL, preprocessing, ML)
├── app.py              # Streamlit application entry point
├── .env.example        # Environment variable template
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/[Your-Username]/Scouting-Engine.git
cd Scouting-Engine
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```plaintext
GOOGLE_SHEETS_ID=your_sheet_id_here
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## Future Work

* Integration of pitch sequencing models
* Batter-specific and situational modeling
* Real-time data ingestion and processing
* Enhanced model interpretability (e.g., SHAP values)
* Deployment of model endpoints via API

---

## License and Acknowledgments

This project is developed for the Guelph Royals Baseball Club. Data is intended for internal scouting and player development purposes.

Special thanks to the coaching staff and Baseball Operations department for their collaboration and domain expertise.

---

## Author

**[Your Name]**
Baseball Analytics Developer
