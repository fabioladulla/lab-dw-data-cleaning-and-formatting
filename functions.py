
import pandas as pd

def clean_gender_column(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This function will take a Pandas DataFrame as an input and it will replace the values in
    the "gender" column in such a way that any gender which is not Male or Female will be 
    replaced by "U" otherwise the genders will be either "F" or "M"

    Inputs:
    df: Pandas DataFrame

    Outputs:
    A pandas DataFrame with the values in the "gender" column cleaned.
    '''

    df2 = df.copy()

    if "gender" not in df2.columns:
        return df2
    else:
        df2['gender'] = df2['gender'].astype(str)
        df2['gender'] = df2['gender'].apply(lambda x: x[0].upper() if x[0].upper() in ['M', 'F'] else "U")
        
    return df2

def convert_data_type(val):
    """
    Convert the object to an integer
     - Check if value is NaN
     - Convert to string
     - Remove '0'
     - Remove '/'
     - Convert to int type
    """
    if pd.isna(val):
        return val
    val = str(val)
    new_value = val.replace('0','').replace('/', '')
    return int(float(new_value))
