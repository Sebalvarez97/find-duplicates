import os
from utils.df_utils import read_csv_to_df, save_results_to_csv
from utils.row_utils import row_compare

route = os.getcwd() + "/src/app/data/sample_data.csv"

print("Reading file from route:", route)
df = read_csv_to_df(route)

# Create a results matrix
results = []

# Check each row
for index, row in df.iterrows():
    # Check other rows
    for i, r in df.iterrows():
        if i == index:
            continue
        row_score = row_compare(row, r)
        if row_score > 0:
            results.append({
                'ContactID Source': row['contactID'],  
                'ContactID Match': r['contactID'],     
                'Accuracy': row_score, 
            })

# Save results
save_results_to_csv(results, "results.csv")
print("Results saved to results.csv")
    
