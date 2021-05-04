"""
This is the pipeline function in which all of us will be coding the transformations needed
for each variables buckets.
"""

def cleaning(input_file_path, output_file_name):

    import pandas as pd
    data = pd.read_excel(str(input_file_path), sheet_name=1)