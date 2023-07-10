import numpy as np

from settings import*

def heat_spread(k):

    # tau
    ts = h**2 / (2*k)
    tau = ts/2
    time_steps = int(TIME // tau)

    # temperature array
    Temp = np.zeros([N, time_steps])
    Temp[:,0] = T_i
    Temp[0,:] = T_1
    Temp[-1,:] = T_2
    
    for time in range(1, time_steps):
        conv_count = 0
        for i in range(1,N-1):
            # change temperature
            Temp[i, time] += Temp[i, time - 1] + 0.5*tau/ts*(Temp[i+1, time-1] + Temp[i-1, time-1] - 2*Temp[i, time-1])
            
            # convergence
            if (Temp[i, time] - Temp[i, time - 1]) / Temp[i, time] < 1e-4*k**0.08:
                conv_count += 1

        if conv_count == N-2:
            break
    
    # delete zeros
    Temp = Temp[:,:time]

    return Temp, tau, time*tau