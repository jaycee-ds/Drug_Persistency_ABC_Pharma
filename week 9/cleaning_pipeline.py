"""
This is the pipeline function in which all of us will be coding the transformations needed
for each variable bucket.
"""

import pandas as pd
import numpy as np 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def cleaning(input_file_path, output_file_name):

    data = pd.read_excel(str(input_file_path), sheet_name=1)

    # transformation for variables with Y and N
    data.replace(to_replace={'Y': 1, 'N': 0}, inplace=True)

    # Clinical Factors
    # # for Ntm_Speciality: group rare categories as OTHER

    data['Ntm_Speciality'] = data['Ntm_Speciality'].mask(
        data['Ntm_Speciality'].map(data['Ntm_Speciality'].value_counts(normalize=True)) < 0.01, 'OTHER')

    # Elimination of variables with more than 40% missing values
    data = data.drop(columns=['Risk_Segment_During_Rx',
                              'Tscore_Bucket_During_Rx',
                              'Change_T_Score',
                              'Change_Risk_Segment'])

    # Transformation for variables with ">-2.5" and "<=-2.5"
    data.replace(to_replace={'>-2.5': 1, '<=-2.5': 0}, inplace=True)

    # Transformation for variables with "VLR_LR" and "HR_VHR"
    data.replace(to_replace={'VLR_LR': 1, 'HR_VHR': 0}, inplace=True)

    # replacing the missing values into actual null values. "Unknown" => "NULL"
    data.replace(
        ["Other/Unknown", "Unknown"],
        np.nan
    )

    # replacing all the null values with the mode of the column 
    for column in data.columns:
        data[column].fillna(data[column].mode()[0], inplace=True)

    # transforming the Age_Bucket variable to numaric. 
    data.replace(to_replace={
        ">75": 0,
        "65-75": 1,
        "55-65": 2,
        "<55": 3
    },
        inplace=True)

    # output file
    data.to_csv(str(output_file_name), index=False)




def altClearning(input_file_path, output_file_name):

    data = pd.read_excel(str(input_file_path), sheet_name=1)

    # Elimination of variables with more than 40% missing values
    data = data.drop(columns = ['Risk_Segment_During_Rx',
                                    'Tscore_Bucket_During_Rx',
                                    'Change_T_Score',
                                    'Change_Risk_Segment'])

    # raplacing the missing values into actual null values. "Unknown" => "NULL" 
    data.replace(
        ["Other/Unknown", "Unknown"],
        np.nan
    )

    # splitting the descriptive variabels from the target variable 
    features = data.iloc[:,2:]
    target = data.Persistency_Flag

    # transformations 
    imputer = SimpleImputer(strategy= "most_frequent")
    label_encoder = LabelEncoder()
    ohe = OneHotEncoder()

    # fitting transformations 
    imputer.fit(features)
    label_encoder.fit(target)
    ohe.fit(features)

    # transform 
    features = imputer.fit_transform(features)
    features = ohe.fit_transform(features).toarray()
    target = label_encoder.fit_transform(target)

    # returning the features and the labels
    return X, Y
