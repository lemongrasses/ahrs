import numpy as np
from ahrs.filters import EKF
from ahrs.filters import Madgwick
from ahrs.common.orientation import *
import matplotlib
import matplotlib.pyplot as plt
import quan2euler_self
matplotlib.use('TkAgg')
file = np.loadtxt("data.txt")
index = max(file[:,0])
time = file[:,1]
acc_data = np.empty((index.astype(int),3))
acc_data[:,0] = file[:,2]
acc_data[:,1] = file[:,3]
acc_data[:,2] = file[:,4]
gyr_data = np.empty((index.astype(int),3))
gyr_data[:,0] = file[:,5]
gyr_data[:,1] = file[:,6]
gyr_data[:,2] = file[:,7]
mag_data = np.empty((index.astype(int),3))
mag_data[:,0] = file[:,8]
mag_data[:,1] = file[:,9]
mag_data[:,2] = file[:,10]

ekf = EKF()
Q = np.zeros((index.astype(int),4))
Q[0] = am2q(acc_data[0],mag_data[0],'NED')

for t in range(1, index.astype(int)):
    Q[t] = ekf.update(Q[t-1], gyr_data[t], acc_data[t], mag_data[t])

ea = quan2euler_self.q2eulerd(Q,index.astype(int))
print(ea)

# fig, axs = plt.subplots(3)
# axs[0].plot(time,acc_data[:,0])
# axs[1].plot(time,acc_data[:,1])
# axs[2].plot(time,acc_data[:,2])

# plt.show()