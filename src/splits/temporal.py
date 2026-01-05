def split_pre_post(spi_df, split_year):
    """
    Non-stationary split: train on early period, test on later period.
    """
    train = spi_df[spi_df.index.year <= split_year]
    test = spi_df[spi_df.index.year > split_year]
    return train, test
