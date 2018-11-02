# import needed modules
import numpy as np
import matplotlib 
from matplotlib import pyplot as plt
# parameters 
m = 10000
k = 10
mu = 0.7
mu1 = 1-mu

# compute the joint pmf 
def joint_pmf(sample):
    # sample has np arrays so 
    # here we convert the values into integers assuming 
    # they are in 2 base
    count = np.zeros((1,2**sample.shape[1]))
    for i in range (0,sample.shape[0]):
        listy = sample[i].tolist()
        stringy = ''.join(str(e) for e in listy)
        index = int(stringy,2)
        count[0,index]+=1
    prob = count/sample.shape[0]
    return prob

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
pmf = (joint_pmf(bernoulli)).reshape(2**k)
print(pmf)
print(np.mean(pmf)*(2**k))
indp = (indp_pmf(bernoulli)).reshape(2**k)
print(indp)
print(np.mean(indp)*(2**k))
num_array = np.arange(2**k).reshape(2**k)

# plotting the pmf's
plt.plot(num_array,pmf,color = "blue",label = 'joint pmf simulated')
plt.plot(num_array,indp, color = "red",label = 'joint pmf independence')
plt.legend()
plt.show()

# by having a look at the plots independece property is verified
