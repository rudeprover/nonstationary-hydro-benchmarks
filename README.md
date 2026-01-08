# Benchmarking Machine Learning and Statistical Models for Non-Stationary Hydro-Climatic Time Series

## Overview
This repository provides a **reproducible benchmarking framework** for evaluating statistical and machine-learning models on **non-stationary hydro-climatic time series**, with a particular focus on **extreme events and out-of-distribution (OOD) behavior**.

The central motivation is not architectural novelty, but to **systematically assess model robustness and generalizability** under distributional shifts—conditions that commonly arise due to climate variability, long-term change, and land-surface alterations.

**Version 1 (current)** focuses on establishing **diagnostic baselines** and understanding how classical assumptions fail before introducing more complex models.

---

## Key Objectives
- Benchmark **classical statistical baselines** against future machine-learning models
- Explicitly evaluate performance under **non-stationary train–test splits**
- Assess model behavior during **hydro-climatic extremes**, not only mean conditions
- Provide a **transparent, extensible baseline** for subsequent ML, hybrid, and physics-aware models

---

## Current Scope (v1)
The current version of the repository focuses on:

- Construction of drought indices (SPI-3 and SPI-6)
- Diagnosis of **distributional non-stationarity** using KDE-based analysis
- Evaluation of **persistence baselines** under strict temporal generalization
- Evaluation of **stationary parametric models (AR(1))** trained on historical data
- Multi-gauge replication to assess robustness across locations
- Explicit analysis of **mean vs extreme-event error behavior**

These steps establish **lower-bound and failure-mode benchmarks** that any advanced model must exceed.

---

## Datasets
The benchmarking workflow is demonstrated using **publicly available hydro-climatic datasets**, such as:

- CAMELS-style hydrologic datasets (meteorological forcings and gauge-wise observations)
- Climate time series used for drought and extreme-event analysis

The codebase is **dataset-agnostic** and can be adapted to other regional or global environmental datasets.

---

## Data Organization Philosophy
This repository follows a **CAMELS-style gauge-centric design**:

- Spatial data (gauge locations, basin boundaries) are used only for documentation and selection
- All modeling and evaluation are performed on **independent gauge-wise time series**
- No spatial joins of daily time series to shapefiles are performed

Each gauge is treated as an **independent non-stationary time-series experiment**.  
The primary key linking all datasets is `gauge_id`.

---

## Models Included

### Statistical Baselines (v1)
- Persistence baseline (last-value prediction)
- Stationary AR(1) model trained on historical data

These baselines are intentionally simple and serve to:
- Expose failure modes under non-stationarity
- Establish lower-bound performance for future models

### Machine Learning (planned extensions)
- LSTM-based time-series forecasting models (PyTorch)
- Non-stationary and regime-aware architectures

---

## Evaluation Focus
Evaluation emphasizes **robustness and generalization**, not only overall error minimization.  
Metrics and diagnostics include:

- Standard metrics (RMSE, MAE)
- **Extreme-focused evaluation** (e.g., SPI < −1.5)
- Performance under **distribution shift** between training and testing periods
- Diagnostic plots illustrating systematic bias during extremes

---

## Repository Structure
```text
.
├── README.md
├── data/
│   ├── README.md
│   ├── gauges.txt
│   ├── forcings/
│   └── indices/
├── notebooks/
│   ├── 01_spi_construction.ipynb
│   ├── 02_nonstationarity_diagnostics.ipynb
│   ├── 03_persistence_baseline.ipynb
│   ├── 04_ar1_baseline.ipynb
│   └── 05_multi_gauge_replication.ipynb
├── src/
│   ├── models/
│   │   └── baselines.py
│   ├── evaluation/
│   │   ├── metrics.py
│   │   └── extremes.py
│   └── splits/
│       └── nonstationary.py
└── environment.yml
```


## Benchmarking Workflow

The notebooks follow a **diagnostic-first workflow**:

1. Construction of drought indices  
2. Detection of distributional non-stationarity  
3. Persistence baseline under strict temporal splits  
4. Stationary AR(1) baseline trained on historical data  
5. Replication across gauges  
6. Comparative evaluation with emphasis on extremes  
7. Interpretation of failure modes and generalizability limits  

---

## Philosophy

This repository prioritizes **clarity, reproducibility, and failure analysis** over model complexity.

Before introducing advanced ML models, the framework explicitly asks:

- Which assumptions fail under non-stationarity?
- Which simple models remain robust, and why?
- What must a more complex model demonstrably improve?

The project is intended as a foundation for:

- Non-stationary and regime-aware ML models  
- Hybrid physics–ML approaches  
- Explainable analysis of model behavior in hydro-climatic systems  

---

## License

Released for research and educational use.  
Please cite appropriately if used in academic work.
