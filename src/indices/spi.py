import pandas as pd
import numpy as np
from scipy.stats import gamma, norm

def compute_spi(precip, scale):
    """
    Compute SPI for a given accumulation scale (months).
    Handles zero precipitation correctly.
    """

    # Build datetime index
    dates = pd.to_datetime(
        dict(year=precip.year, month=precip.month, day=precip.day)
    )
    ts = pd.Series(precip["prcp(mm/day)"].values, index=dates)

    # Monthly aggregation (use ME instead of deprecated M)
    monthly = ts.resample("ME").sum()

    # Rolling accumulation
    acc = monthly.rolling(scale).sum().dropna()

    # Separate zero and non-zero values
    zero_mask = acc == 0
    nonzero = acc[~zero_mask]

    # Probability of zero precipitation
    q = zero_mask.mean()

    # Fit Gamma to non-zero data only
    shape, loc, scale_param = gamma.fit(nonzero, floc=0)

    # Gamma CDF for non-zero values
    G = gamma.cdf(nonzero, shape, loc=loc, scale=scale_param)

    # Adjusted CDF
    H = q + (1 - q) * G

    # Convert to standard normal (SPI)
    spi_nonzero = norm.ppf(H)

    # Reconstruct full SPI series
    spi = pd.Series(index=acc.index, dtype=float)
    spi.loc[~zero_mask] = spi_nonzero
    spi.loc[zero_mask] = norm.ppf(q)  # SPI value for zero-precip cases

    return spi.to_frame(name=f"SPI_{scale}")
