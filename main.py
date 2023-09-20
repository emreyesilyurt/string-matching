import pandas as pd
from src.fuzzy_matching import compere_matcher

if __name__ == "__main__":
    # Load data from CSV files
    df1 = pd.read_csv("data/source_data.csv")
    df2 = pd.read_csv("data/target_data.csv")

    # Specify the columns to match
    column_to_match1 = df1["Name"]
    column_to_match2 = df2["Product_Name"]

    # Define column names for the result
    result_columns = ["Source_Name", "Target_Product_Name", "Matching_Score"]

    # Perform fuzzy matching
    result_df = compere_matcher(column_to_match1, column_to_match2, result_columns)

    # Save the matching results to a CSV file
    result_df.to_csv("matching_results.csv", index=False)

    print("Fuzzy matching completed. Matching results saved to 'matching_results.csv'.")
