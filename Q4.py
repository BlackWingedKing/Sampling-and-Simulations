# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

lam = 0.5
mu = 0.5
num_steps = 10000

# here n,l are parameters no of samples and lambda
def generate_bernoulli(n,l):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,(1,n))
    exp = -1*(1/l)*np.log(uniform) 
    return exp  