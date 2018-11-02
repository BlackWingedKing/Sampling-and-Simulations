# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

lam = 0.6
mu = 0.4
num_steps = 100
samples = 10000


sam_in = []
sam_out = []
sam_q = []
# here n,m are parameters no of samples and mean
def generate_bernoulli(m):
    # generate a random array of n
    uniform = np.random.uniform(0.0,1.0,1)
    bernoulli = np.where(uniform > (1.0-m), 1, 0) 
    return bernoulli[0]  

# now simulate the queue system
for sam in range (0,samples): 
    # initialise the packets
    num_packets = 0
    in_list = []
    out_list = []
    q_list = []
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
    
    sam_in.append(in_list)
    sam_out.append(out_list)
    sam_q.append(q_list)

# plotting the ensemble quantities 
time_instant = 7
n = 8 # take care before giving the value of n and time coz nth may not arrive

# for finding the ensemble average
wn_list = []
qt_list = []

for i in range (0,len(sam_in)):
    # convert each one into np array and do the computation
    wn_list.append(sam_out[i][n] - sam_in[i][n])
    qt_list.append(sam_q[i][time_instant])

wn_array = np.asarray(wn_list)
qt_array = np.asarray(qt_list)
# now we got those arrays
# generate ensemble averages
wn_ensemble = []
qt_ensemble = []

for i in range (1,samples+1):
    wn_ensemble.append(np.mean(wn_array[0:i]))
    qt_ensemble.append(np.mean(qt_array[0:i]))

wn_ensemble = np.asarray(wn_ensemble)
qt_ensemble = np.asarray(qt_ensemble)
# plot the ensembles
ensemblen = np.arange(samples)
plt.plot(ensemblen,wn_ensemble,color = "blue",label = 'wn_ensemble')
plt.plot(ensemblen,qt_ensemble, color = "red",label = 'qt_ensemble')
plt.legend()
plt.show()