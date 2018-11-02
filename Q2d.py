# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

lam1 = 1
lam2 = 1
lam12 = 0.01
num_samples = 10000

# here n,l are parameters no of samples and lambda
def generate_samples(n,l):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,(1,n))
    temp = 1-uniform
    exp = -1*(1/l)*np.log(temp) 
    return exp 

# compute the sample prob
def compute_prob(a1,a2,x1,x2): # a1 and a2 are no's and x1,x2 are sample arrays
    count = 0.0
    total = float(x1.shape[1]*x2.shape[1])
    for i in range (0,x1.shape[1]):
        for j in range (0,x2.shape[1]):
            if(x1[0,i]>a1 and x2[0,j]>a2):
                count = count + 1
    
    return (count/total)

def func_prob(a1,a2,l1,l2,l12):
    maxi = max(a1,a2)
    temp = np.exp(-1*l1*a1 -1*l2*a2 -1*l12*maxi)
    return temp

y1 = generate_samples(num_samples,lam1)
y2 = generate_samples(num_samples,lam2)
y12= generate_samples(num_samples,lam12)
x1 = np.minimum(y1,y12)
x2 = np.minimum(y2,y12)

# compute mean and var of x1, x2
mean_x1 = np.mean(x1)
var_x1 = np.var(x1, ddof=1)
mean_x2 = np.mean(x2)
var_x2 = np.var(x2, ddof=1)
print(mean_x1, mean_x2, var_x1, var_x2)
print(compute_prob(0.5,0.8,x1,x2))
print(func_prob(0.5,0.8,lam1,lam2,lam12))
