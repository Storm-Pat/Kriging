from sklearn.model_selection import GridSearchCV
import numpy as np
from pykrige.rk import Krige

def cv(df):
    #the kriging parameters to predict
    param_dict = {
        #"method": ["ordinary"],
        "variogram_model": ["linear", "power", "gaussian", "spherical","exponential"],
        "nlags": [6,8,10,15,20],
        "weight": [True, False],
        "pseudo_inv": [True,False],
        "exact_values": [True,False]
    }
    #the estimator object to be used to predict the best kriging
    estimator=GridSearchCV(Krige(),param_dict,verbose=False,return_train_score=True)
    #grid definition
    df_np = df.to_numpy()
    X=df_np[:,0:2]
    y=df_np[:,2]
    #grid searcher
    print("Finding best hyperparameters out of 4368 combinations!")
    estimator.fit(X=X,y=y)
    #printing best params
    if hasattr(estimator, "best_score_"):
        print("best_score R² = {:.3f}".format(estimator.best_score_))
        print("best_params = ", estimator.best_params_)
