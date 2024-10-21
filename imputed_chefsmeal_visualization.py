import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the imputed Chef's Meal dataset
imputed_chefsmeal_data = pd.read_csv('data/imputed_chefsmeal.csv')

# Visualization 1: Fitness Goal vs. Hours at Gym (per week)
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_gym = imputed_chefsmeal_data.groupby('Fitness Goal')['Hours at Gym (per week)'].mean()
chefsmeal_fitness_vs_gym.plot(kind='bar', color='orange')
plt.title('Average Hours at Gym per Week by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 2: Fitness Goal vs. Calorie Intake
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_calorie = imputed_chefsmeal_data.groupby('Fitness Goal')['Calorie Intake'].mean()
chefsmeal_fitness_vs_calorie.plot(kind='bar', color='green')
plt.title('Average Calorie Intake by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 3: Fitness Goal vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_spend = imputed_chefsmeal_data.groupby('Fitness Goal')['Average Spend per Meal Order'].mean()
chefsmeal_fitness_vs_spend.plot(kind='bar', color='blue')
plt.title('Average Spend per Meal Order by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 4: Fitness Goal vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_diet = pd.crosstab(imputed_chefsmeal_data['Fitness Goal'], imputed_chefsmeal_data['Dietary Preferences'])
chefsmeal_fitness_vs_diet.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
plt.title('Dietary Preferences by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 5: Hours at Gym (per week) vs. Calorie Intake
plt.figure(figsize=(10, 6))
chefsmeal_gym_vs_calorie = imputed_chefsmeal_data.groupby('Hours at Gym (per week)')['Calorie Intake'].mean()
chefsmeal_gym_vs_calorie.plot(kind='line', marker='o', color='purple')
plt.title('Average Calorie Intake by Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 6: Hours at Gym (per week) vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_gym_vs_spend = imputed_chefsmeal_data.groupby('Hours at Gym (per week)')['Average Spend per Meal Order'].mean()
chefsmeal_gym_vs_spend.plot(kind='line', marker='o', color='red')
plt.title('Average Spend per Meal Order by Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 7: Hours at Gym (per week) vs. Dietary Preferences
# Bin 'Hours at Gym (per week)' into categories
gym_bins = pd.cut(imputed_chefsmeal_data['Hours at Gym (per week)'], bins=np.arange(0, 20, 2))
gym_vs_diet = pd.crosstab(gym_bins, imputed_chefsmeal_data['Dietary Preferences'])

# Plotting the data
plt.figure(figsize=(12, 8))
gym_vs_diet.plot(kind='bar', stacked=True, colormap='Set3', ax=plt.gca())
plt.title('Dietary Preferences by Binned Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Binned Hours at Gym (per week)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 8: Calorie Intake vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_calorie_vs_spend = imputed_chefsmeal_data.groupby('Calorie Intake')['Average Spend per Meal Order'].mean()
chefsmeal_calorie_vs_spend.plot(kind='line', marker='o', color='brown')
plt.title('Average Spend per Meal Order by Calorie Intake (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Calorie Intake')
plt.show()

# Visualization 9: Calorie Intake vs. Dietary Preferences
# Bin 'Calorie Intake' into categories
calorie_bins = pd.cut(imputed_chefsmeal_data['Calorie Intake'], bins=np.arange(0, 5000, 500))
calorie_vs_diet = pd.crosstab(calorie_bins, imputed_chefsmeal_data['Dietary Preferences'])

# Plotting the data
plt.figure(figsize=(12, 8))
calorie_vs_diet.plot(kind='bar', stacked=True, colormap='tab20', ax=plt.gca())
plt.title('Dietary Preferences by Binned Calorie Intake (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Binned Calorie Intake')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 10: Average Spend per Meal Order vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_spend_vs_diet = imputed_chefsmeal_data.groupby('Dietary Preferences')['Average Spend per Meal Order'].mean()
chefsmeal_spend_vs_diet.plot(kind='bar', color='cyan')
plt.title('Average Spend per Meal Order by Dietary Preferences (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Dietary Preferences')
plt.xticks(rotation=15)
plt.show()
