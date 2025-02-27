from fuzzywuzzy import fuzz

# Score scale
# More than 100 its very high
# More than 50 its high
# More than 20 its medium
# Less than 25 its low

collumn_score_weights = {
    "contactID": 50,
    "name": 10,
    "name1": 10,
    "email": 50,
    "postalZip": 1,
    "address": 30,
}

# Compare two rows with the same collumns and return a score
def row_compare(row1, row2): 
    compareScore = 0
    # If the columns of the two rows are not the same, raise an error
    if not row1.index.equals(row2.index):
        raise ValueError("The columns of the two rows must be the same.")
    # Compare the values of each column
    for column in row1.index:        
        # Address is a special case, we use fuzzy matching
        if column == 'address':
            if isinstance(row1[column], str) and isinstance(row2[column], str):
                fuzzy_score = fuzz.ratio(row1[column].strip(), row2[column].strip())
                if fuzzy_score > 80:
                    compareScore += collumn_score_weights.get(column, 0)
                continue
        if isinstance(row1[column], str) and isinstance(row2[column], str):
            if row1[column].strip() == row2[column].strip():
                compareScore += collumn_score_weights.get(column, 0)
        elif row1[column] == row2[column]:
            compareScore += collumn_score_weights.get(column, 0)
    return compareScore
            
            