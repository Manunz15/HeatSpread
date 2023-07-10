# materials [m^2/s]
k = {
    'Steel': 4.25e-6,
    'Gold': 127e-6,
    'Aluminium': 97e-6,    
    'Oak Wood': 0.13e-6,
    'Bricks': 0.52e-6,
    'Glass': 0.34e-6,
    'Air': 22.4e-6,
    'Water': 0.14e-6,
    'Ice': 1.2e-6
}

sorted_k = {key: value for key, value in sorted(k.items(), key=lambda x:x[1])}

# width [m]
L = 0.01
N = 100
h = L / N

# time [s]
TIME = 60
conv_times = []

# temperatures [°C]
T_i = 27
T_1 = 5
T_2 = 50