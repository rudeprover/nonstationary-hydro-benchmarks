Benchmarking Machine Learning and Statistical Models for Non-Stationary Hydro-Climatic Time Series
Overview

This repository provides a reproducible benchmarking framework for comparing machine learning and traditional statistical models on non-stationary hydro-climatic time series, with a focus on extreme events and out-of-distribution behavior. The primary goal is not to propose a novel architecture, but to systematically evaluate model generalizability under changing climatic and land-surface conditions.

The workflow is designed to reflect challenges commonly encountered in hydrology and climate science, where historical stationarity assumptions break down and robust prediction of extremes is critical for risk assessment and early warning.

Key Objectives

Benchmark deep learning time-series models (implemented in PyTorch) against classical statistical baselines (e.g., ARIMA)

Evaluate model performance under non-stationary conditions

Focus explicitly on hydro-climatic extremes rather than average behavior

Provide a transparent, extensible baseline for hybrid and physics-aware modeling

Dataset

The benchmarking workflow is demonstrated using publicly available hydro-climatic datasets, such as:

CAMELS-style hydrologic time series (meteorological forcings and streamflow)

Climate extreme indices derived from reanalysis or observational products

The code is dataset-agnostic and can be adapted to other regional or global datasets.

Models Included

Machine Learning

LSTM-based time-series forecasting model (PyTorch)

Statistical Baselines

ARIMA / seasonal ARIMA

Persistence baseline (last-value or climatology)

Evaluation Focus

Rather than optimizing overall error alone, evaluation emphasizes:

Performance on extreme events (upper/lower quantiles)

Robustness across different climatic regimes

Behavior under distribution shift between training and test periods

Example metrics include:

RMSE / MAE (overall skill)

Quantile-based errors

Extreme event detection skill (e.g., hit rate, false alarm rate)

Repository Structure

.
├── data/                  # Preprocessed example datasets (or loaders)
├── models/
│   ├── lstm.py             # PyTorch LSTM model
│   └── baselines.py        # ARIMA and persistence baselines
├── evaluation/
│   ├── metrics.py          # Standard and extreme-focused metrics
│   └── plots.py            # Diagnostic plots
├── notebooks/
│   └── benchmark.ipynb     # End-to-end benchmarking notebook
└── README.md


Philosophy

This repository prioritizes clarity, reproducibility, and critical evaluation over model complexity. It is intended as a foundation for future work on:

Hybrid ML–process models

Non-stationary trend-aware architectures

Explainable and causal analysis of model behavior
