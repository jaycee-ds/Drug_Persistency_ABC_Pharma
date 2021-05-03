"""
Handling categorical values: Y and N are replaced with 1 and 0, respectively.
"""

import pandas as pd

data = pd.read_excel('Drug_Persistency_ABC_Pharma/Healthcare_dataset.xlsx', sheet_name=1)
subset = data.iloc[:, 24:]

# This is the transformation needed - subset must be replaced with the correct parameter in the function
subset.replace(to_replace={"Y": 1, "N": 0}, inplace=True)
