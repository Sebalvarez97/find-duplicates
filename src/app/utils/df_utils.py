import pandas as pd

def read_csv_to_df(route: str) -> pd.DataFrame:
    """Read csv file to panda DataFrame."""
    return pd.read_csv(route)

def print_df_data(df: pd.DataFrame) -> None:
    """Print DataFrame data."""
    print("First 5 rows of the DataFrame:")
    print(df.head())
    
# Save results to CSV
def save_results_to_csv(results, file_name):
    results_df = pd.DataFrame(results)  
    results_df.to_csv(file_name, index=False) 