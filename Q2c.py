# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# used e^-x as f1
num_samples = 10000
c = 10
# here n is no of samples
def desired_pmf(x):
    temp = np.sqrt(2/np.pi)*np.exp(-x*x*0.5)
    return temp

def generate_samples(n,c):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,(1,n))
    exp = -1*(1/l)*np.log(uniform) 
    # shuffle elements in exp
    exp = np.random.shuffle(exp)
    for i in range (0,n):
        u_sample = uniform[0,i]
        exp_sample = exp[0,i]
        exp_value = np.exp(-1*exp[0,i])
        fun_sample = desired_pmf(exp_sample)
        while():

    return  

# calculation of the sample mean and variance
mean_list = []
var_list = []
num_list = []

sample = generate_samples(i,lam) 
mean = np.mean(sample)
var = np.var(sample,ddof=1)

