import pandas as pd

# Load the datasets
pulsegear_data = pd.read_csv('data/pulsegear.csv')
coreboost_data = pd.read_csv('data/coreboost.csv')
chefsmeal_data = pd.read_csv('data/chefsmeal.csv')
flexfield_fitness_data = pd.read_csv('data/flexfield_fitness.csv')

# Checking for columns with missing values
print("Missing values in PulseGear dataset:\n", pulsegear_data.isna().sum())
print("Missing values in CoreBoost dataset:\n", coreboost_data.isna().sum())
print("Missing values in Chef's Meal dataset:\n", chefsmeal_data.isna().sum())
print("Missing values in FlexField Fitness dataset:\n", flexfield_fitness_data.isna().sum())

# Cleaning the data: Removing rows with missing values in columns that have NaN values
cleaned_pulsegear_data = pulsegear_data.dropna(subset=['Hours at Gym (per week)', 'Type of Apparel Purchased'])
cleaned_coreboost_data = coreboost_data.dropna(subset=['Hours at Gym (per week)', 'Preferred Sports Drink Type'])
cleaned_chefsmeal_data = chefsmeal_data.dropna(subset=['Hours at Gym (per week)', 'Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order'])
cleaned_flexfield_fitness_data = flexfield_fitness_data.dropna(subset=['Hours at Gym (per week)', 'Calorie Intake'])

# Optionally, save the cleaned datasets to new files
cleaned_pulsegear_data.to_csv('data/cleaned_pulsegear.csv', index=False)
cleaned_coreboost_data.to_csv('data/cleaned_coreboost.csv', index=False)
cleaned_chefsmeal_data.to_csv('data/cleaned_chefsmeal.csv', index=False)
cleaned_flexfield_fitness_data.to_csv('data/cleaned_flexfield_fitness.csv', index=False)

# Display the first few rows of the cleaned data
print("Cleaned PulseGear Data:\n", cleaned_pulsegear_data.head())
print("Cleaned CoreBoost Data:\n", cleaned_coreboost_data.head())
print("Cleaned Chef's Meal Data:\n", cleaned_chefsmeal_data.head())
print("Cleaned FlexField Fitness Data:\n", cleaned_flexfield_fitness_data.head())
