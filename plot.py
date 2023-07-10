import matplotlib.pyplot as plt
from matplotlib import cm
import pandas as pd

from heat_spread import*

colors = ['red', 'orange', 'gold', 
          'lawngreen', 'aquamarine', 'deepskyblue', 
          'blue', 'indigo', 'darkviolet']

# plots temperature over time
def plot_surf(Temp, tau, title):

    N = Temp.shape[0]
    time_steps = Temp.shape[1]

    # X, Y arrays
    X = range(N)
    Y = range(time_steps)
    X, Y = np.meshgrid(Y, X)

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    surf = ax.plot_surface(X*tau, Y*h*100, Temp, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    # colorbar
    cbar =fig.colorbar(surf, shrink=0.5, aspect=5)
    cbar.set_label('°C', rotation=0, loc = 'top')

    # labels
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Width [cm]')
    ax.set_title(title + '\tk = {:.2f}e-6 $m^2/s$'.format(k[title]*1e6))

    plt.show()

# plots temperature in some instants
def plot_cuts(Temp, tau, title):

    x = np.linspace(0, L*100, N)

    for i in range(len(colors)):
        t = i*((Temp.shape[1]-1)//(len(colors)-1))
        y = Temp[:, t]
        plt.plot(x, y, label = '{:.2f} s'.format(t*tau), c = colors[i])

    plt.title(title + '\tk = {:.2f}e-6 $m^2/s$'.format(k[title]*1e6))
    plt.xlabel('Width [cm]')
    plt.ylabel('Temperature [°C]')
    plt.legend()
    plt.show()

# plots time to converge
def plot_conv_times(conv_times):

    # x = np.linspace(0,130,1500)
    # y = 5/x
    # plt.plot(x,y, '--', c = 'red', label = '$t = 5/k$', zorder = 0)

    DF_conv = pd.DataFrame({'Material':[],'k':[],'Time':[]})

    for i in range(len(conv_times)):
        DF_conv.loc[len(DF_conv)] = [list(sorted_k.keys())[i], list(sorted_k.values())[i], conv_times[i]]
        plt.scatter(list(sorted_k.values())[i]*10**6, conv_times[i], label = list(sorted_k.keys())[i], c = colors[i%len(colors)])

    DF_conv.to_csv('Convergence times.csv', index = False)

    plt.xlabel('k [$10^6m^2/t$]')
    plt.ylabel('Convergence time [s]')
    plt.legend()
    plt.title('Convergence times per material')
    plt.show()
