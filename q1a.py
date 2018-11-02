# import needed modules
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt
# parameters 
m = 10000
k = 5 
mu = 0.2
mu1 = 1-mu

# compute the joint pmf 
def joint_pmf(sample):
    # sample has np arrays so 
    # here we convert the values into integers assuming 
    # they are in 2 base
    #count = np.zeros((1,2**sample.shape[1]))
    joint = np.zeros((sample.shape[0],1))
    count = np.zeros((sample.shape[0],1))
    #count = np.sum(sample,axis=1)
    for j in range (0,sample.shape[0]):
        for i in range (0,sample.shape[1]):
            joint[j,0]+=sample[j,i]*2**i
            count[j,0]+=sample[j,i]
    return joint,count

def indp_pmf(sample):
    # to verify independence
    # first calculate the mean's of each RV
    r = sample.shape[1]
    indp = np.zeros((1,2**sample.shape[1]))
    means = np.mean(bernoulli, axis =0)
    notmeans = 1.0 - means
    for i in range(0,2**sample.shape[1]):
        stringy = np.binary_repr(i,width = r)
        value = 1.0
        for j in range (0,r):
            if(int(stringy[j]) == 1):
                value = value*means[j]
            else:
                value = value*notmeans[j]
        indp[0,i] = value
    return indp

# generate a random array of N = m x k
uniform = np.random.uniform(0.0,1.0,(m,k))
bernoulli = np.where(uniform > mu1, 1, 0)
mean = np.mean(bernoulli)
print(mean)
# to compute pmf
pmf,no1s = (joint_pmf(bernoulli))
print(pmf)
print(np.mean(pmf)*(2**k))
indp = (indp_pmf(bernoulli)).reshape(32)
print(indp)
print(np.mean(indp)*(2**k))
num_array = np.arange(2**k).reshape(32)

# plotting the pmf's
plt.hist(pmf,32,density=1,label="joint_pmf")
plt.plot(num_array,indp, color = "red",label="indp_pmf")
plt.hist(no1s,5,density=1,color="yellow",label="no of 1's")
plt.show()

# by having a look at the plots independece property is verified