# Benchmarking Machine Learning and Statistical Models for Non-Stationary Hydro-Climatic Time Series

## Overview
This repository provides a **reproducible benchmarking framework** for evaluating machine learning and classical statistical models on **non-stationary hydro-climatic time series**, with a particular focus on **extreme events and out-of-distribution (OOD) behavior**.  
The aim is not to introduce a novel architecture, but to **systematically assess model generalizability** under changing climatic and land-surface conditions—a key challenge in flood risk assessment and early warning.

The workflow is designed to reflect real-world hydro-climatic settings, where assumptions of stationarity often break down and robust prediction of extremes is critical.

---

## Key Objectives
- Benchmark **deep learning time-series models** (implemented in PyTorch) against **traditional statistical baselines** (e.g., ARIMA)
- Evaluate model performance under **non-stationary conditions**
- Focus explicitly on **extreme events**, rather than only mean behavior
- Provide a **transparent, extensible baseline** for future hybrid and physics-aware modeling

---

## Datasets
The benchmarking workflow is demonstrated using **publicly available hydro-climatic datasets**, such as:
- CAMELS-style hydrologic datasets (meteorological forcings and streamflow)
- Observational or reanalysis-based climate time series for extreme-event analysis

The codebase is dataset-agnostic and can be adapted to other regional or global environmental datasets.

---

## Models Included

### Machine Learning
- LSTM-based time-series forecasting model (PyTorch)

### Statistical Baselines
- ARIMA / seasonal ARIMA
- Persistence baseline (e.g., last-value or climatology)

---

## Evaluation Focus
Evaluation emphasizes **robustness and generalization**, not only overall error minimization.  
Metrics and diagnostics focus on:

- Standard performance metrics (RMSE, MAE)
- **Extreme-focused evaluation** (e.g., upper/lower quantiles)
- Skill under **distribution shift** between training and testing periods
- Diagnostic plots highlighting model behavior during extreme events

---
## Repository Structure

.
├── data/                  # Example data loaders or preprocessed samples
├── models/
│   ├── lstm.py             # PyTorch LSTM model
│   └── baselines.py        # ARIMA and persistence baselines
├── evaluation/
│   ├── metrics.py          # Standard and extreme-focused metrics
│   └── plots.py            # Diagnostic and comparison plots
├── notebooks/
│   └── benchmark.ipynb     # End-to-end benchmarking notebook
└── README.md


---

## Benchmarking Workflow
The main notebook (`benchmark.ipynb`) follows a clear, reproducible structure:
1. Problem definition and motivation
2. Data preparation and non-stationary train/test split
3. Statistical baselines
4. PyTorch model training
5. Evaluation with emphasis on extremes and OOD behavior
6. Diagnostic plots and comparative analysis
7. Discussion of generalizability and limitations

---

## Philosophy
This repository prioritizes **clarity, reproducibility, and critical evaluation** over model complexity.  
It is intended as a foundation for:
- Hybrid ML–process modeling
- Trend-aware and non-stationary architectures
- Explainable and causal analysis of model behavior in environmental systems

---

## License
This project is released for research and educational use. Please cite appropriately if used in academic work.
