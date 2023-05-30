from sklearn.model_selection import GridSearchCV
from pykrige.rk import Krige

'''This file is supposed to be used for ML (machine learning), or to find the best possible settings for an
interpolation. However, since it takes a very long time on larger datasets (and that's primarily what is input),
it is not necessary or even economical to have this run in the field. The option to use this has been removed from the 
GUI and is suggested it remain so, however this file is still here in case the use of ML seems viable.'''

def cv(df):
    # the kriging parameters to predict
    param_dict = {
        # "method": ["ordinary"],
        "variogram_model": ["linear", "power", "gaussian", "spherical", "exponential"],
        "nlags": [6, 8, 10, 15, 20],
        "exact_values": [True, False]
    }
    # the estimator object to be used to predict the best kriging
    estimator = GridSearchCV(Krige(), param_dict, verbose=False, return_train_score=True)
    # grid definition
    df_np = df.to_numpy()
    X = df_np[:, 0:2]
    y = df_np[:, 2]
    # grid searcher
    estimator.fit(X=X, y=y)
    if hasattr(estimator, "best_score_"):
        print("best_score R² = {:.3f}".format(estimator.best_score_))
        print("best_params = ", estimator.best_params_)
