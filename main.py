from plot import*

for material in list(sorted_k):
    Temp, tau, conv_time = heat_spread(k = k[material])

    conv_times.append(conv_time)

    plot_surf(Temp = Temp, tau = tau, title = material)
    plot_cuts(Temp = Temp, tau = tau, title = material)

plot_conv_times(conv_times = conv_times, k = sorted_k)