import pandas as pd
from pathlib import Path

MERGE_ON = 'PROSPECTID'


def read_excel_data(data_path: Path) -> pd.DataFrame:
    df = pd.read_excel(data_path)
    return df


def merge_data(data_left: pd.DataFrame,data_right: pd.DataFrame,how: str,merge_on: str) -> pd.DataFrame:
    final_df = pd.merge(left=data_left,right=data_right,
                        how=how,on=merge_on)
    return final_df


def save_data(df: pd.DataFrame,save_path: Path) -> None:
    df.to_csv(save_path,index=False)
    
    

def main():
    current_path = Path(__file__)
    root_path = current_path.parent.parent.parent
    data_load_path = root_path / "data" / "data-dump"
    data_save_path = data_load_path.parent / "raw" 
    data_save_path.mkdir(exist_ok=True)
    
    # read the first df
    df1_filename = "case_study1.xlsx" 
    df1 = read_excel_data(data_load_path / df1_filename)
    # read the second df
    df2_filename = "case_study2.xlsx"
    df2 = read_excel_data(data_load_path / df2_filename)
    # merge the two dataframes
    merged_df = merge_data(data_left=df1,data_right=df2,
                           how='inner',merge_on=MERGE_ON)
    # save the dataframe
    save_data(df=merged_df,save_path=data_save_path / "data.csv")
    
    
if __name__ == "__main__":
    main()