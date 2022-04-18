import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data(filename):
    df = pd.read_excel(filename,sheet_name = 'simulated data')
    df.drop(0, inplace = True)
    return df

def clean_data(df):
    df.drop(["CPAP, FiO2", "CPAP, pressure level","CPAP, initial FiO2","CPAP, initial pressure level"], axis=1 , inplace=True)
    #Interface has two enumeration. Populate N/A as a third class.
    df["Interface"].fillna("N/A", inplace=True)
    df["HFNC, initial flow"].fillna(df["HFNC, initial flow"].mean(), inplace=True)
    df["HFNC, initial FiO2"].fillna(df["HFNC, initial FiO2"].mean(), inplace=True)
    df["HFNC, flow"].fillna(df["HFNC, flow"].mean(), inplace=True)
    return df


def main():
    df = load_data('Field names_COVID intubation (project 1) 20220404 with simulated data.xlsx')
    df = clean_data(df)
    print(df.describe())


if __name__ == '__main__':
    main()
