# modules required
import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# global variabless
lam = 0.6
mu = 0.8
num_steps = 1000

# initialise the packets
num_packets = 0

in_list = []
out_list = []
q_list = []

# here n,m are parameters no of samples and mean
def generate_bernoulli(m):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,1)
    bernoulli = np.where(uniform > (1.0-m), 1, 0) 
    return bernoulli[0]  

for i in range (0,num_steps):
    # each is a timestep
    a = generate_bernoulli(lam)
    if(a>0):
        # arrival
        num_packets = num_packets + 1
        in_list.append(i)

    if(num_packets>0):
        b = generate_bernoulli(mu)
        if(b>0):
            # departure
            num_packets = num_packets - 1
            out_list.append(i)
    q_list.append(num_packets)

went = len(out_list)
print(went)
# convert the qt and w to array
q_array = np.asarray(q_list)
in_array = np.asarray(in_list)
out_array = np.asarray(out_list)
num_array = np.arange(went)

wait = out_array - in_array[0:went]

# plotting the everything
# plt.plot(num_array,q_array,color = "blue")
plt.plot(num_array,wait, color = "red")