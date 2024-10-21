import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned CoreBoost dataset
cleaned_coreboost_data = pd.read_csv('data/cleaned_coreboost.csv')

# Visualization 1: Fitness Goal vs. Average Weekly Consumption (Bottles)
plt.figure(figsize=(10, 6))
coreboost_fitness_vs_consumption = cleaned_coreboost_data.groupby('Fitness Goal')['Average Weekly Consumption (Bottles)'].mean()
coreboost_fitness_vs_consumption.plot(kind='bar', color='orange')
plt.title('Average Weekly Consumption (Bottles) by Fitness Goal (CoreBoost)')
plt.ylabel('Average Weekly Consumption (Bottles)')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 2: Hours at Gym (per week) vs. Preferred Sports Drink Type
plt.figure(figsize=(10, 6))
coreboost_gym_vs_drink = cleaned_coreboost_data.groupby('Preferred Sports Drink Type')['Hours at Gym (per week)'].mean()
coreboost_gym_vs_drink.plot(kind='bar', color='green')
plt.title('Average Hours at Gym per Week by Preferred Sports Drink Type (CoreBoost)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Preferred Sports Drink Type')
plt.xticks(rotation=15)
plt.show()

# Visualization 3: Hours at Gym (per week) vs. Average Weekly Consumption (Bottles)
plt.figure(figsize=(10, 6))
coreboost_gym_vs_consumption = cleaned_coreboost_data.groupby('Hours at Gym (per week)')['Average Weekly Consumption (Bottles)'].mean()
coreboost_gym_vs_consumption.plot(kind='line', marker='o', color='blue')
plt.title('Average Weekly Consumption (Bottles) by Hours at Gym per Week (CoreBoost)')
plt.ylabel('Average Weekly Consumption (Bottles)')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 4: Fitness Goal vs. Hours at Gym (per week)
plt.figure(figsize=(10, 6))
coreboost_fitness_vs_gym = cleaned_coreboost_data.groupby('Fitness Goal')['Hours at Gym (per week)'].mean()
coreboost_fitness_vs_gym.plot(kind='bar', color='purple')
plt.title('Average Hours at Gym per Week by Fitness Goal (CoreBoost)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 5: Preferred Sports Drink Type vs. Average Weekly Consumption (Bottles)
plt.figure(figsize=(10, 6))
coreboost_drink_vs_consumption = cleaned_coreboost_data.groupby('Preferred Sports Drink Type')['Average Weekly Consumption (Bottles)'].mean()
coreboost_drink_vs_consumption.plot(kind='bar', color='red')
plt.title('Average Weekly Consumption (Bottles) by Preferred Sports Drink Type (CoreBoost)')
plt.ylabel('Average Weekly Consumption (Bottles)')
plt.xlabel('Preferred Sports Drink Type')
plt.xticks(rotation=15)
plt.show()

# Visualization 6: Preferred Sports Drink Type vs. Fitness Goal
plt.figure(figsize=(10, 6))
coreboost_drink_vs_fitness = pd.crosstab(cleaned_coreboost_data['Preferred Sports Drink Type'], cleaned_coreboost_data['Fitness Goal'])
coreboost_drink_vs_fitness.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='tab20')
plt.title('Preferred Sports Drink Type vs. Fitness Goal (CoreBoost)')
plt.ylabel('Count of Customers')
plt.xlabel('Preferred Sports Drink Type')
plt.xticks(rotation=15)
plt.show()


