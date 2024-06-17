import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_data(num_rows, seed):
    """
    Generate a DataFrame with apartment size and cost data.

    Parameters:
    - num_rows: int, number of rows of data to generate
    - seed: int, random seed for reproducibility

    Returns:
    - data: DataFrame with columns 'Size' and 'Cost'
    """
    np.random.seed(seed)

    sizes = np.random.randint(500, 1500, size=num_rows)
    
    base_cost = 50000
    cost_per_sqft = 300
    noise = np.random.normal(0, 20000, num_rows)

    costs = base_cost + (cost_per_sqft * sizes) + noise
    costs = np.round(costs, 2)

    data = pd.DataFrame({
        'Size': sizes,
        'Cost': costs
    })
    
    data.to_csv('apartment_cost_vs_size.csv', index=False)
    return data

# Example usage
if __name__ == "__main__":
    num_rows = 100
    seed = 42
    data = create_data(num_rows, seed)
    print(data.head())

