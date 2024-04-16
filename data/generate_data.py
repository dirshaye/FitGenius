import pandas as pd
import numpy as np

# Generating synthetic data
np.random.seed(42)  

# Define energy levels (0 to 100) 
energy_levels = np.random.randint(0, 101, size=100) 

# Define time of day (morning, afternoon, evening)
times_of_day = np.random.choice(['morning', 'afternoon', 'evening'], size=100) 

# Define stress levels (low, moderate, high)
stress_levels = np.random.choice(['low', 'moderate', 'high'], size=100)

# Define fitness preferences (cardio, strength training, yoga)
fitness_preferences = np.random.choice(['cardio', 'strength training', 'yoga'], size=100)

# Create DataFrame
fitness_data = pd.DataFrame({
    'energy_level': energy_levels,
    'time_of_day': times_of_day,
    'stress_level': stress_levels,
    'fitness_preference': fitness_preferences
})

# Save DataFrame to CSV
fitness_data.to_csv('data/fitness_data.csv', index=False)
