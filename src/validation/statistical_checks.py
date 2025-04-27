# statistical_checks.py
def validate_gi_inputs(df):
    """Implements IQR validation from search result [5]"""
    q1 = df.quantile(0.25)
    q3 = df.quantile(0.75)
    iqr = q3 - q1
    return df[~((df < (q1 - 1.5 * iqr)) | (df > (q3 + 1.5 * iqr))).any(axis=1)]
