import time
import random
import matplotlib.pyplot as plt

# Define known design costs for different resource configurations
design_costs = {
    (1, 1): 0.618,
    (1, 2): 0.5399,
    (1, 3): 0.5580,
    (1, 4): 0.648,
    (1, 5): 0.5399,
    (2, 1): 0.640,
    (2, 2): 0.5628,
    (2, 3): 0.581,
    (2, 4): 0.671,
    (2, 5): 0.690,
}

stTime = time.time()

# Function to compute design cost for a given resource configuration
def compute_design_cost(resource_config):
    return design_costs.get(resource_config)

# Function to generate a random resource configuration within the specified range
def generate_random_configuration():
    min_adder = 1
    max_adder = 2
    min_multiplier = 1
    max_multiplier = 5
    return (random.randint(min_adder, max_adder), random.randint(min_multiplier, max_multiplier))

# Tabu Search function to find minimum design cost
def tabu_search():
    # Initialize the current configuration with a random point within the specified range
    current_config = generate_random_configuration()
    current_cost = compute_design_cost(current_config)

    best_config = current_config
    best_cost = current_cost

    tabu_list = []
    max_tabu_size = 10

    max_iterations = 1000

    # Lists to store the cost and iteration for graph plotting
    cost_history = []
    iteration_history = []

    for iteration in range(max_iterations):
        # Generate a neighboring configuration using a uniform distribution
        neighbor_config = (
            random.randint(1, 2),
            random.randint(1, 5),
        )
        neighbor_cost = compute_design_cost(neighbor_config)

        # If the neighbor is in the tabu list, skip this iteration
        if neighbor_config in tabu_list:
            continue

        # Update the tabu list
        tabu_list.append(neighbor_config)
        if len(tabu_list) > max_tabu_size:
            tabu_list.pop(0)

        # Update the current configuration if the neighbor is better
        if neighbor_cost < current_cost:
            current_config = neighbor_config
            current_cost = neighbor_cost

            # Update the best configuration if necessary
            if current_cost < best_cost:
                best_config = current_config
                best_cost = current_cost

        # Record cost and iteration for plotting
        cost_history.append(current_cost)
        iteration_history.append(iteration)

    return best_config, best_cost, cost_history, iteration_history

# Find the resource configuration with the minimum design cost and get cost history
best_configuration, min_cost, cost_history, iteration_history = tabu_search()
end = time.time()

# Plot the cost history
plt.plot(iteration_history, cost_history)
plt.xlabel("Iteration")
plt.ylabel("Design Cost")
plt.title("Tabu Search Optimization")
plt.grid(True)
plt.show()

print("Best Resource Configuration:", best_configuration)
print("Minimum Design Cost:", min_cost)
print("Computation Time:", end - stTime)
