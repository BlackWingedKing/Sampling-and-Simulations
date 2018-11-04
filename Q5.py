# modules required
# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

num_samples = 1000
n_max = 100

# generate num_samples x n uniform samples
def generate_uniform(m,n):
    uniform = np.random.uniform(0.0,1.0,(m,n))
    return uniform

p_list = []
q_list = []
total_list = []
k_list = []
for i in range (5,n_max):
    uniform = generate_uniform(num_samples,i)
    p_sublist = []
    q_sublist = []
    total_sublist = []
    for k in range (1,i):
        # not choosing anyone ie if the max value is in k
        k_val = np.zeros((num_samples,1)) + k-1
        max_index = np.argmax(uniform,axis = 1).reshape(num_samples,1)
        ones = (max_index <= k_val)
        # ie the entry is 1 if the max value lies till k-1
        q = np.mean(ones) # this is the p(not choosing)
        q_sublist.append(q)
        
        # find the max entry of the array ie
        max_arg = np.argmax(uniform,axis=1).reshape(num_samples,1)
        max_k = np.max(uniform[:,0:k],axis=1).reshape(num_samples,1)
        p = uniform > max_k
        p.astype(float)
        p = np.argmax(p,axis=1).reshape(num_samples,-1)
        p = (p==max_arg)
        p[ones>0.0]=0 # extra condition this is most needed
        mean_p = np.mean(p)
        # p = 1-p # this is prob of error!
        # total = p+q
        total = 1-mean_p
        p_sublist.append(total-q)
        total_sublist.append(total)

    total_subarray = np.asarray(total_sublist)
    index = np.argmin(total_subarray)
    p_list.append(p_sublist[index])
    q_list.append(q_sublist[index])
    total_list.append(total_subarray[index])
    k_list.append(index+1)

total_array = np.asarray(total_list)
p_array = np.asarray(p_list)
q_array = np.asarray(q_list)
k_array = np.asarray(k_list)
num_array = np.arange(5,n_max).reshape(n_max-5)
print(total_subarray)
plt.plot(num_array,p_array, color = "green",label = 'p')
plt.plot(num_array,k_array, color = "red",label = 'k')
plt.plot(num_array,q_array, color = "blue",label = 'q')
plt.legend()
plt.show()
