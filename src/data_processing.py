def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.
    
    Args:
        file_path (str): The path to the CSV file.
        
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
    import pandas as pd
    return pd.read_csv(file_path)