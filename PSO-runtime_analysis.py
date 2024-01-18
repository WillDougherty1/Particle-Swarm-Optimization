import time

from PSO import pso

# // Parameters:
#   // number of particle
#   // number of iterations
#   // search space size

# Part 1: Variable: number of particles
num_particles = [i for i in range(1, 1000000, 50)]
max_iterations = 100                                # Constant Variable
search_space = (-5.0, 5.0)                          # Constant Varaible
runtime = []

# Collect Data
for n in num_particles:
    t_start = time.time()
    pso(n, max_iterations, search_space)
    runtime.append(time.time() - t_start)

# Export Data
with open('variable_n.csv', 'w') as fd:
    fd.write('time,particles\n')
    for i in range(len(num_particles)):
        output = str(runtime[i]) + ',' + str(num_particles[i]) + '\n'
        fd.write(output)



# Part 2: Variable: number of iterations
num_particles = 30                                  # Constant Variable
max_iterations = [i for i in range(1, 1000000, 50)]
search_space = (-5.0, 5.0)                          # Constant Varaible
runtime = []

# Collect Data
for i in max_iterations:
    t_start = time.time()
    pso(num_particles, i, search_space)
    runtime.append(time.time() - t_start)

# Export Data
with open('variable_iter.csv', 'w') as fd:
    fd.write('time,iterations\n')
    for i in range(len(max_iterations)):
        output = str(runtime[i]) + ',' + str(max_iterations[i]) + '\n'
        fd.write(output)



# Part 3: Variable: search space size
num_particles = 30                                  # Constant Variable
max_iterations = 100                                # Constant Varaible
search_space = [(-i, i) for i in range(1, 10000, 10)]
runtime = []

# Collect Data
for s in search_space:
    t_start = time.time()
    pso(num_particles, max_iterations, s)
    runtime.append(time.time() - t_start)

# Export Data
with open('variable_search-space.csv', 'w') as fd:
    fd.write('time,searcharea\n')
    for i in range(len(search_space)):
        output = str(runtime[i]) + ',' + str(search_space[i][0] ** 2) + '\n'
        fd.write(output)