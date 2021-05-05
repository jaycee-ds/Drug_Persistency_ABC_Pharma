"""
This is the pipeline function in which all of us will be coding the transformations needed
for each variables buckets.
"""

import pandas as pd
import numpy as np 

def cleaning(input_file_path, output_file_name):

    data = pd.read_excel(str(input_file_path), sheet_name=1)

    # transformation for variables with Y and N
    data.replace(to_replace={'Y': 1, 'N': 0}, inplace=True)

    """
    Guys, write your code in between. The output file code (below) is the end of the function :)
    """
    # Elimination of variables with more than 40% missing values
    data = data.drop(columns = ['Risk_Segment_During_Rx',
                                    'Tscore_Bucket_During_Rx',
                                    'Change_T_Score',
                                    'Change_Risk_Segment'])

    # Transformation for variables with ">-2.5" and "<=-2.5"
    data.replace(to_replace={'>-2.5': 1, '<=-2.5': 0}, inplace=True)

    # Transformation for variables with "VLR_LR" and "HR_VHR"
    data.replace(to_replace={'VLR_LR': 1, 'HR_VHR': 0}, inplace=True)

    # raplacing the missing values into actual null values. "Unknown" => "NULL" 
    data.replace(
        ["Other/Unknown", "Unknown"],
        np.nan
    )

    # replacing all the null values with the mode of the column 
    for column in data.columns:
        data[column].fillna(data[column].mode()[0], inplace= True)


    # transforming the Age_Bucket variable to numaric. 
    data.replace(to_replace={
        ">75": 0,
        "65-75": 1,
        "55-65": 2,
        "<55": 3
    },
    inplace= True)


    # output file
    data.to_csv(str(output_file_name), index=False)