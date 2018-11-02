# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

mu = 1 # mean of the gaussian
sigma = 4.0 #variance of the gaussian
num_samples = 10000 #num of samples

def generate_samples(n,sigma,mu):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,(1,n))
    uniform1= np.random.uniform(0.0,1.0,(1,n))
    R = np.sqrt(-2*np.log(1-uniform))
    theta = 2*np.pi*uniform1
    normal = R*np.cos(theta) 
    gaussian = np.sqrt(sigma)*normal + mu
    #print(gaussian)
    return gaussian

# calculation of the sample mean and variance
mean_list = []
var_list = []
num_list = []
for i in range (1,num_samples):
    print('iteration no. == ', i)
    sample = generate_samples(i,sigma,mu) 
    mean = np.mean(sample)
    var = np.var(sample,ddof=1)
    mean_list.append(mean)
    var_list.append(var)
    num_list.append(i)

# we need to plot the sample mean and variance
mean_array = np.asarray(mean_list)
var_array = np.asarray(var_list)
num_array = np.asarray(num_list)
plt.plot(num_array,mean_array,color = "blue",label="mean")
plt.plot(num_array,var_array, color = "red",label="var")
plt.legend()
plt.show()