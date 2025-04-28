import pandas as pd

def load_data(filepath):
    """
    Loads a CSV file and returns a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File {filepath} is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
