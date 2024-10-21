import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned Chef's Meal dataset
cleaned_chefsmeal_data = pd.read_csv('data/cleaned_chefsmeal.csv')

# Visualization 1: Fitness Goal vs. Hours at Gym (per week)
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_gym = cleaned_chefsmeal_data.groupby('Fitness Goal')['Hours at Gym (per week)'].mean()
chefsmeal_fitness_vs_gym.plot(kind='bar', color='orange')
plt.title('Average Hours at Gym per Week by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=45)
plt.show()

# Visualization 2: Fitness Goal vs. Calorie Intake
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_calorie = cleaned_chefsmeal_data.groupby('Fitness Goal')['Calorie Intake'].mean()
chefsmeal_fitness_vs_calorie.plot(kind='bar', color='green')
plt.title('Average Calorie Intake by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=45)
plt.show()

# Visualization 3: Fitness Goal vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_spend = cleaned_chefsmeal_data.groupby('Fitness Goal')['Average Spend per Meal Order'].mean()
chefsmeal_fitness_vs_spend.plot(kind='bar', color='blue')
plt.title('Average Spend per Meal Order by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=45)
plt.show()

# Visualization 4: Fitness Goal vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_fitness_vs_diet = pd.crosstab(cleaned_chefsmeal_data['Fitness Goal'], cleaned_chefsmeal_data['Dietary Preferences'])
chefsmeal_fitness_vs_diet.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
plt.title('Dietary Preferences by Fitness Goal (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=45)
plt.show()

# Visualization 5: Hours at Gym (per week) vs. Calorie Intake
plt.figure(figsize=(10, 6))
chefsmeal_gym_vs_calorie = cleaned_chefsmeal_data.groupby('Hours at Gym (per week)')['Calorie Intake'].mean()
chefsmeal_gym_vs_calorie.plot(kind='line', marker='o', color='purple')
plt.title('Average Calorie Intake by Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 6: Hours at Gym (per week) vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_gym_vs_spend = cleaned_chefsmeal_data.groupby('Hours at Gym (per week)')['Average Spend per Meal Order'].mean()
chefsmeal_gym_vs_spend.plot(kind='line', marker='o', color='red')
plt.title('Average Spend per Meal Order by Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 7: Hours at Gym (per week) vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_gym_vs_diet = pd.crosstab(cleaned_chefsmeal_data['Hours at Gym (per week)'], cleaned_chefsmeal_data['Dietary Preferences'])
chefsmeal_gym_vs_diet.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
plt.title('Dietary Preferences by Hours at Gym per Week (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Hours at Gym (per week)')
plt.xticks(rotation=45)
plt.show()

# Visualization 8: Calorie Intake vs. Average Spend per Meal Order
plt.figure(figsize=(10, 6))
chefsmeal_calorie_vs_spend = cleaned_chefsmeal_data.groupby('Calorie Intake')['Average Spend per Meal Order'].mean()
chefsmeal_calorie_vs_spend.plot(kind='line', marker='o', color='brown')
plt.title('Average Spend per Meal Order by Calorie Intake (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Calorie Intake')
plt.show()

# Visualization 9: Calorie Intake vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_calorie_vs_diet = pd.crosstab(cleaned_chefsmeal_data['Calorie Intake'], cleaned_chefsmeal_data['Dietary Preferences'])
chefsmeal_calorie_vs_diet.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab10')
plt.title('Dietary Preferences by Calorie Intake (Chef\'s Meal)')
plt.ylabel('Count of Customers')
plt.xlabel('Calorie Intake')
plt.xticks(rotation=45)
plt.show()

# Visualization 10: Average Spend per Meal Order vs. Dietary Preferences
plt.figure(figsize=(10, 6))
chefsmeal_spend_vs_diet = cleaned_chefsmeal_data.groupby('Dietary Preferences')['Average Spend per Meal Order'].mean()
chefsmeal_spend_vs_diet.plot(kind='bar', color='cyan')
plt.title('Average Spend per Meal Order by Dietary Preferences (Chef\'s Meal)')
plt.ylabel('Average Spend per Meal Order ($)')
plt.xlabel('Dietary Preferences')
plt.xticks(rotation=45)
plt.show()