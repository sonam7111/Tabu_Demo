import time
import random
import matplotlib.pyplot as plt

def generate_unique_design_costs(max_adder, max_multiplier):
    """Generates a dictionary of unique resource configurations and costs."""
    costs = set()
    design_costs = {}
    config_number = 1  # Initialize a counter for numbering
    while len(design_costs) < max_adder * max_multiplier:
        cost = random.uniform(0, 1)
        if cost not in costs:
            costs.add(cost)
            config = (random.randint(1, max_adder), random.randint(1, max_multiplier))
            while config in design_costs:  # Ensure unique configurations
                config = (random.randint(1, max_adder), random.randint(1, max_multiplier))
            design_costs[config] = cost

            # Print numbered configuration and cost
            print(f"Configuration {config_number}: {config}, Cost: {cost:.4f}")
            config_number += 1  # Increment the counter

    return design_costs

def compute_design_cost(resource_config):
    return design_costs.get(resource_config)

def generate_random_configuration():
    min_adder = 1
    max_adder = 10
    min_multiplier = 1
    max_multiplier = 10
    return (random.randint(min_adder, max_adder), random.randint(min_multiplier, max_multiplier))

def tabu_search(tabu_list_size=10, max_iterations=1000):
    current_config = generate_random_configuration()
    current_cost = compute_design_cost(current_config)

    best_config = current_config
    best_cost = current_cost

    tabu_list = []

    cost_history = []
    iteration_history = []

    for iteration in range(max_iterations):
        neighbor_config = generate_random_configuration()
        neighbor_cost = compute_design_cost(neighbor_config)

        if neighbor_config in tabu_list or neighbor_cost >= current_cost:
            continue

        current_config = neighbor_config
        current_cost = neighbor_cost

        if current_cost < best_cost:
            best_config = current_config
            best_cost = current_cost

        tabu_list.append(neighbor_config)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        cost_history.append(current_cost)
        iteration_history.append(iteration)

    return best_config, best_cost, cost_history, iteration_history

stTime = time.time()

# Generate unique resource configurations and costs
design_costs = generate_unique_design_costs(10, 10)

# Find the resource configuration with the minimum design cost and get cost history
best_configuration, min_cost, cost_history, iteration_history = tabu_search()
end = time.time()

plt.plot(iteration_history, cost_history)
plt.xlabel("Iteration")
plt.ylabel("Design Cost")
plt.title("Tabu Search Optimization")
plt.grid(True)
plt.show()

print("Best Resource Configuration:", best_configuration)
print("Minimum Design Cost:", min_cost)
print("Computation Time:", end - stTime)
