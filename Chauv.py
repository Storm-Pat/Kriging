import pandas as pd
import scipy as sp
def chauv(df):
    #defining boundry p value
    P = 1/(2*len(df))
    #initialzing what will be clean data_frame
    df_clean = df
    #dirt array uwu
    dirty = []
    #mean value
    mean = df.iloc[:,2].mean()
    #standard deviation
    sigma = df.iloc[:,2].std()
    #z score function
    z = lambda i: abs(i - mean) / sigma
    print(len(df_clean))
    for i in df.iloc[:,2]:
        #computing z score
        zscore = z(i)
        #applying z score to 1-erf to produce a probability
        p = sp.special.erfc(zscore)
        #cheking the probablity function output against the boundry
        if p < P:
            dirty.append(i)
            df_clean = df_clean[df_clean.Depth_m != i]
    print("These are the dirty values:")
    print(dirty)
    print("Would you like to keep these values?")
    #user input most likley through the gui
    #flow control would be implimented here for choosing wheter or not we return the filtered values






