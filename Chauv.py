import scipy as sp
import os

home_dir = os.path.expanduser('~')
parent_directory = 'Field-Interp-Tool'
directory1 = 'output_files'
path0 = os.path.join(home_dir, 'Documents')
path1 = os.path.join(path0, parent_directory)
path2 = os.path.join(path1, directory1)


def chauv(df, dirtval):
    # defining boundary p value
    P = 1 / (2 * len(df))
    # initializing what will be clean data_frame
    df_clean = df
    # dirty array
    dirty = []
    # mean value
    mean = df.mean()
    # standard deviation
    sigma = df.std()
    # z score function
    z = lambda i: abs(i - mean) / sigma
    for i in df:
        # computing z score
        zscore = z(i)
        # applying z score to 1-erf to produce a probability
        p = sp.special.erfc(zscore)
        # checking the probability function output against the boundary
        if p < P:
            dirty.append(i)
            df_clean = df_clean[df_clean != i]
            df_clean = df_clean.reset_index(drop=True)

    while True:
        y_n = dirtval
        # setting local variable to the variable received from the gui
        if y_n:
            # writing out dataframe
            path3 = os.path.join(path2, "clean_data.csv")
            df_clean.to_csv(path3)
            return df_clean
        elif y_n is False:
            # writing it out again
            path4 = os.path.join(path2, "raw_data.csv")
            df.to_csv(path4)
            return df
        else:
            continue
