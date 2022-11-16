import numpy as np
import random


def sparse():
    # this is part one of the matrix evaluation of the IVER3 dataset
    X = random.randint(1, 10)
    Y = random.randint(1, 10)
    print(X)
    print(Y)
    # TODO this will have to be remade to have the input be read from a file
    A = np.random.standard_exponential(size=(X, Y))
    A[A < 0.9] = 0
    Asum = sum(A > 0.9)
    # TODO instead of excluding points below a certain value, we would be receiving cells with no value meaning this
    #  statement isn't necessary
    B = sum(Asum)
    C = np.sum(A)
    # TODO the average is the value that will be used for the larger matrix
    print(A)
    print("The total amount of nonzero elements in the matrix is: ", B)
    print("The sum of all elements is: ", C)
    D = C / B
    print("The average value in the sparse matrix is: ", D)
    return D


# TODO once all the sparse matrices are completed, they will need to be input into a larger grid to interpolate them

def large():
    global bigun
    iterate = input("How many times do you want the small matrix to run?: ")
    iterate = int(iterate)
    # TODO this will also be automated when the code is implemented, the file input will determine the iterations
    for x in range(iterate):
        print(sparse())
        # this will run the sparse matrix for a defined amount of sequences
        # TODO now the value returned by sparse will have to be input into a larger matrix, probably within the loop


large()
