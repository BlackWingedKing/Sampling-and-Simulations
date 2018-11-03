# this is required for analytical analysis of the system
# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

n_max = 100

sum_list = []
for i in range (5,n_max):
    sum_sublist = []
    for k in range (1,i):
        sum = 0.0
        for l in range (1,i-k):
            sum = sum + (k/(i*(l+k-1)))
        a = 1.0 - sum
        sum_sublist.append(a)
    print(sum_sublist)
    sum_subarray  = np.asarray(sum_sublist)
    k = np.argmin(sum_subarray) + 1
    sum_list.append(k)

sum_array = np.asarray(sum_list)
num_array = np.arange(5,n_max).reshape(n_max-5)
plt.plot(num_array,sum_array, color = "blue",label = 'analytical value')
plt.legend()
plt.show()
