# import needed modules
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

time = 15
# initialise all as zero vectors
x = np.zeros(time)
y = np.zeros(time)
w = np.random.normal(0.0,1,time)
v = np.random.normal(0.0,np.sqrt(0.1),time)
# the matrices
f = np.asarray([[2.5,-2.0,0.7],[1,0.0,0.0],[0.0,1,0.0]])
h = np.asarray([[1,0.0,0.0],[0.0,1,0.0],[0.0,0.0,1]])
# now initialise them 
# asssuming x[-1] and x[0] as zeros
x[0] = 0.0
x[1] = 0.0
x[2] = w[1]
y[0] = v[0]
y[1] = v[1]
y[2] = v[2]

state_vector = np.zeros((time,3))
obs_vector = np.zeros((time,3))
pred_vector = np.zeros((time,3))
v_vector = np.zeros((time,3))
w_vector = np.zeros((time,3))
q_vector = np.zeros((time,3,3))
r_vector = np.zeros((time,3,3))
sigma = np.zeros((time,3,3))
k = np.zeros((time,3,3))

# pred_vector[0] = [0,0,0]
# pred_vector[1] = [0,0,0]
pred_vector[2] = [x[2],0,0]
state_vector[2] = np.array([x[2], x[1], x[0]])
obs_vector[2] = np.array([y[2], y[1], y[0]])


# generate all the noises...
for t in range (2,time):    
    v_vector[t] = np.array([v[t], v[t-1], v[t-2]])
    w_vector[t] = np.array([w[t],0.0,0.0])
    q_vector[t] = np.cov(w_vector[t],ddof=1)
    r_vector[t] = np.cov(v_vector[t],ddof=1)

sigma[2] = q_vector[2]

print('r_vectot..',r_vector[2])

for t in range (2,time-1):
    # forward step
    state_vector[t+1] = np.matmul(f,state_vector[t]) + w_vector[t]
    obs_vector[t] = np.matmul(h,state_vector[t]) + v_vector[t]
    
    # kalman gain update
    temp1 = np.matmul(np.matmul(f,sigma[t]),h)        
    temp2 = np.matmul(np.matmul(h,sigma[t]),h) + r_vector[t]
    temp2inv = np.linalg.pinv(temp2)
    k[t] = np.matmul(temp1,temp2inv)
    
    # prediction update
    innovation = obs_vector[t] - pred_vector[t]
    pred_vector[t+1] = np.matmul(f,pred_vector[t]) + np.matmul(k[t],innovation)
    
    # sigma update
    temp3 = np.matmul(sigma[t],h)
    temp4 = np.matmul(h,sigma[t])
    temp5 = sigma[t] - np.matmul(np.matmul(temp3,temp2inv),temp4)
    sigma[t+1] = np.matmul(np.matmul(f,temp5),f.T) + q_vector[t]

# now to plot 
z = [0,0]
pz = [0,0]
zy = [0,0]
for i in range (2,time-1):
    z.append(state_vector[i,0])
    pz.append(pred_vector[i,0])
    zy.append(obs_vector[i,0])

z = np.asarray(z)
pz = np.asarray(pz)
zy = np.asarray(zy)

# for plotting the kalman gain and the errors
kalman_mod = np.zeros(time-1)
for i in range (0,time-1):
    kalman_mod[i] = np.linalg.norm(k[i],ord=2)

kalman_mod.reshape(time-1,-1)
actual_error = z - pz
actual_error = np.multiply(actual_error,actual_error)

# pred_error = 

num = np.arange(0,time-1)
plt.plot(num,z,color = "blue",label = 'state x(t)')
plt.plot(num,pz, color = "red",label = 'predicted E(X(t+1)| y(t))')
plt.plot(num,zy,color = "yellow",label = 'observation y(t)')
plt.plot(num,kalman_mod,color = "black",label = 'kalman gain modulus')
plt.plot(num,actual_error,color = "green",label = 'actual error in the estimate mean square')
plt.legend()
plt.show()