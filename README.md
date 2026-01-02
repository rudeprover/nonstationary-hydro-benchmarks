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
