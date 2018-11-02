
# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# used e^-x as f1
num_samples = 100000
c = 1.32

# here n is no of samples
def desired_pmf(x):
    temp = np.sqrt(2/np.pi)*np.exp(-x*x*0.5)
    return temp


def generate_samples(n,c):
	# generate a random array of n
	i=0
	total= 0.0
	accprob=0.0
	a_list=[]
	#desired_list=[]
	while(i<n):
		u = np.random.uniform(0.0,1.0)
		u1= np.random.uniform(0.0,1.0)
		exp = -1*(1/1)*np.log(u) 
		t1=desired_pmf(exp)/(np.exp(-1*exp)*c)
		if(u1<t1):
			#desired_list.append(desired_pmf(exp))
			a_list.append(exp)
			i=i+1
		total=total+1
	accprob=n/total
	a_array = np.asarray(a_list)
	#d_array=np.asarray(desired_list)
	return accprob,a_array



# calculation of the sample mean and variance
#mean_list = []
#var_list = []
#num_list = []

prob, sample= generate_samples(num_samples,c) 
x=np.arange(0,4.5,0.1)
y=desired_pmf(x)
plt.hist(sample,100,density=1)
plt.plot(x,desired_pmf(x),color='red')
plt.show()
#plt.hist()
# mean = np.mean(sample)
# var = np.var(sample,ddof=1)
print(prob)
