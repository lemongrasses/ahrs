import numpy as np
import math
def qnorm(q: np.ndarray, num: int) -> np.ndarray:
    temp = np.multiply(q,q)
    n = np.empty((num))
    x = np.empty((num))
    y = np.empty((num))
    z = np.empty((num))
    w = np.empty((num))
    Q = np.empty((num,4))
    for i in range(num):
        n[i] = np.sqrt(np.sum(temp[i]))
        x[i] = q[i][0] / n[i]
        y[i] = q[i][1] / n[i]
        z[i] = q[i][2] / n[i]
        w[i] = q[i][3] / n[i]
        Q[i] = [x[i],y[i],z[i],w[i]]
    return Q
def q2eulerd(Q: np.ndarray, num: int) -> np.ndarray:
    q = qnorm(Q,num)
    tmp = np.subtract(np.multiply(np.multiply(q[:,1],q[:,3]),2),np.multiply(np.multiply(q[:,0],q[:,2]),2))
    tmp[np.where(tmp > 1)] = 1
    tmp[np.where(tmp < -1)] = -1
    yaw = np.empty((num))
    pitch = np.empty((num))
    raw = np.empty((num))
    euler = np.empty((num,3))
    for i in range(num):
        pitch[i] = -np.arcsin(tmp[i])
        if pitch[i] >= math.pi/2:
            yaw[i] = -2 * np.arctan2(q[i][1],q[i][0])
            raw[i] = 0
        elif pitch[i] <= -math.pi/2:
            yaw[i] = 2 * np.arctan2(q[i][1],q[i][0])
            raw[i] = 0
        else:
            yaw[i] = np.arctan2((q[i][0] * q[i][3] *2 + q[i][1] * q[i][2] * 2),(q[i][0]*q[i][0]*2 - 1 + q[i][1] * q[i][1] * 2))
            raw[i] = np.arctan2((q[i][0] * q[i][1] *2 + q[i][2] * q[i][3] * 2),(q[i][0]*q[i][0]*2 - 1 + q[i][3] * q[i][3] * 2))
        euler[i] = [yaw[i]*180/math.pi, pitch[i]*180/math.pi, raw[i]*180/math.pi]
    return euler