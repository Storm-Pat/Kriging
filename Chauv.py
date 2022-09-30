import scipy as sp
def chauv(df):
    print("Cleaning junk values.")
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
    for i in df.iloc[:,2]:
        #computing z score
        zscore = z(i)
        #applying z score to 1-erf to produce a probability
        p = sp.special.erfc(zscore)
        #cheking the probablity function output against the boundry
        if p < P:
            dirty.append(i)
            df_clean = df_clean[df_clean.Depth_m != i]
            df_clean = df_clean.reset_index(drop=True)
    print("These are the dirty values:")
    print(dirty)
    while True:
        y_n=input("Would you like to discard the dirty values[y/n]?")
        if y_n.lower()=="yes" or y_n.lower()=="y":
            print("Discarding dirty values.")
            #writing out dataframe
            df_clean.to_csv("Outputs/clean_data.csv")
            return df_clean
        elif y_n.lower()=="no" or y_n.lower()=="n":
            print("Keeping dirty values.")
            #writing it out again
            df.to_csv('Outputs/raw_data.csv')
            return df
        else:
            print("Enter yes/no or y/n")
            continue






