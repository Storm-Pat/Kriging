import scipy as sp
import Main


def chauv(df):
    csv_gui = None
    shp_gui = None
    mach_learn = None
    lags_true_gui = None
    exval = None
    krigtype = None
    dirt = None

    CSV, SHP, ML, lags_true, EXV, dropdown, dirtval = Main.guidrop(csv_gui, shp_gui, mach_learn, lags_true_gui, exval,
                                                              krigtype, dirt)
    # defining boundary p value
    P = 1 / (2 * len(df))
    # initializing what will be clean data_frame
    df_clean = df
    # dirty array
    dirty = []
    # mean value
    mean = df.iloc[:, 2].mean()
    # standard deviation
    sigma = df.iloc[:, 2].std()
    # z score function
    z = lambda i: abs(i - mean) / sigma
    for i in df.iloc[:, 2]:
        # computing z score
        zscore = z(i)
        # applying z score to 1-erf to produce a probability
        p = sp.special.erfc(zscore)
        # checking the probability function output against the boundary
        if p < P:
            dirty.append(i)
            df_clean = df_clean[df_clean.Depth_m != i]
            df_clean = df_clean.reset_index(drop=True)

    while True:
        y_n = dirtval
        # setting local variable to the variable received from the gui
        if y_n:
            # writing out dataframe
            df_clean.to_csv("output_files/clean_data.csv")
            return df_clean
        elif y_n is False:
            # writing it out again
            df.to_csv('output_files/raw_data.csv')
            return df
        else:
            continue
