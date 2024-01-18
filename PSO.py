import random
from math import sin, cos

# Define the objective function that we want to optimize (replace this with your own function)
def objective_function(x, y):
    return x**2 * sin(x)**2 + cos(y)**2

# Define the PSO parameters
# num_particles = 30
# max_iterations = 100
c1 = 2.0  # Cognitive parameter
c2 = 2.0  # Social parameter
w = 0.7   # Inertia weight
# search_space = (-5.0, 5.0)  # Search space limits for both dimensions

class Particle:
    def __init__(self, search_space):
        self.position = [random.uniform(*search_space), random.uniform(*search_space)]
        self.velocity = [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.best_position = [self.position[0], self.position[1]]
        self.best_value = objective_function(self.position[0], self.position[1])

def pso(num_particles=30, max_iterations=100, search_space=(-5.0, 5.0)):
    particles = [Particle(search_space) for _ in range(num_particles)]
    global_w_best_position = particles[0].best_position     # List type
    global_w_best_value = particles[0].best_value           # Float type

    for iteration in range(max_iterations):
        for particle in particles:
            # Update the particle's velocity
            for d in range(2):
                r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
                particle.velocity[d] = (
                    w * particle.velocity[d] +
                    c1 * r1 * (particle.best_position[d] - particle.position[d]) +
                    c2 * r2 * (global_w_best_position[d] - particle.position[d])
                )
            
            # Update the particle's position
            new_position = [(particle.position[d] + particle.velocity[d]) for d in range(2)]

            if search_space[0] <= new_position[0] <= search_space[1] and search_space[0] <= new_position[1] <= search_space[1]:
                particle.position = [new_position[0], new_position[1]]
                current_value = objective_function(new_position[0], new_position[1])

                # Update the particle's best position
                if current_value < particle.best_value:
                    particle.best_position[0] = new_position[0]
                    particle.best_position[1] = new_position[1]
                    particle.best_value = current_value

                # Update the global best position
                if current_value < global_w_best_value:
                    global_w_best_position[0] = new_position[0]
                    global_w_best_position[1] = new_position[1]
                    global_w_best_value = current_value

    return global_w_best_position, global_w_best_value

if __name__ == '__main__':
    best_position, best_value = pso()
    print(f"Best solution found at ({round(best_position[0], 2)},{round(best_position[1], 2)}), when f(x) = {round(best_value, 2)}")