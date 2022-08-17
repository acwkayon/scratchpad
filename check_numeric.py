# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import os
import sys
import click

import pandas as pd
import numpy as np

from mlhub.pkg import get_cmd_cwd

# Ensure paths are relative to the user's cwd.

os.chdir(get_cmd_cwd())

# Setup comman line argument

@click.command()

@click.argument("filename",
                default=sys.stdin,
                type=click.File('r')) 

def cli(filename):
    '''Check a csv file to ensure that all values are numeric. 
    Example of use is for ensure csv is correctly formatted to be used for training a Kmeans model '''
    
    df = pd.read_csv(filename)
    
    # df = pd.DataFrame({'col' : [1,2, 10, 10, 10], 
    #                     'col2': [10, 10, 30, 40 ,50],
    #                     'col3': [1,2,3,4,5.0]})
    # print(df)
    
    


    if not all(df.apply(lambda col: pd.to_numeric(col, errors='coerce').notnull().all())) == True:
        print( "Not numeric")
    else:
        print("All numeric")
    # if all(df.apply(lambda col: pd.to_numeric(col, errors='coerce').notnull().all())) == True:
    #     print( "All numeric")
        

if __name__ == "__main__":
    cli(prog_name="check_numeric")