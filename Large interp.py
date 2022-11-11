import numpy as np


def sparse():
    # this is part one of the matrix evaluation of the IVER3 dataset
    X = input("How many rows: ")
    Y = input("How many columns: ")
    # TODO this will have to be remade to have the input be read from a file
    X = int(X)
    Y = int(Y)
    A = np.random.standard_exponential(size=(X, Y))
    A[A < 0.9] = 0
    Asum = sum(A > 0.9)
    B = sum(Asum)
    C = np.sum(A)
    print(A)
    print("The total amount of nonzero elements in the matrix is: ", B)
    print("The sum of all elements is: ", C)
    D = C / B
    print("The average value in the sparse matrix is: ", D)
    # TODO this will have to be a loop with unknown iterations since we will have an unknown number of points


# TODO once all the sparse matrices are completed, they will need to be input into a larger grid to interpolate them

sparse()
