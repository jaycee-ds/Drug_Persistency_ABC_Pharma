"""
This is the pipeline function in which all of us will be coding the transformations needed
for each variables buckets.
"""

def cleaning(input_file_path, output_file_name):

    import pandas as pd
    data = pd.read_excel(str(input_file_path), sheet_name=1)

    # transformation for variables with Y and N
    data.replace(to_replace={'Y': 1, 'N': 0}, inplace=True)

    """
    Guys, write your code in between. The output file code (below) is the end of the function :)
    """

    # output file
    data.to_csv(str(output_file_name), index=False)