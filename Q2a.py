# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

lam = 2
num_samples = 10000

# here n,l are parameters no of samples and lambda
def generate_samples(n,l):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,(1,n))
    exp = -1*(1/l)*np.log(uniform) 
    return exp 

# calculation of the sample mean and variance
mean_list = []
var_list = []
num_list = []
sample_list=[]
for i in range (1,num_samples):
    print('iteration no. == ', i)
    sample = generate_samples(i,lam) 
    mean = np.mean(sample)
    var = np.var(sample,ddof=1)
    mean_list.append(mean)
    var_list.append(var)
    num_list.append(i)
    sample_list.append(sample)

# we need to plot the sample mean and variance
mean_array = np.asarray(mean_list)
var_array = np.asarray(var_list)
num_array = np.asarray(num_list)
# sample_array =np.asarray(sample_list)
mean_array.astype(float)
var_array.astype(float)
mean_exact=mean_array-1/lam
var_exact=var_array-1/lam**2
var_exact=np.abs(var_exact)
k1=np.argmin(var_exact[1:-1]) + 1
sizy = len(sample_list[k1])
arey = sample_list[k1][0]
print(arey.shape)
print(arey)
#plt.hist(arey,100,density=1,color="yellow",label="best pdf")
plt.plot(num_array,mean_array,color = "blue",label="mean")
plt.plot(num_array,var_array, color = "red",label="var")
plt.legend()
plt.show()
