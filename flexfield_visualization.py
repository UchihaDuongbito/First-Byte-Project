import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned FlexField Fitness dataset
cleaned_flexfield_fitness_data = pd.read_csv('data/cleaned_flexfield_fitness.csv')

# Visualization 1: Fitness Goal vs. Hours at Gym (per week)
plt.figure(figsize=(10, 6))
flexfield_fitness_vs_gym = cleaned_flexfield_fitness_data.groupby('Fitness Goal')['Hours at Gym (per week)'].mean()
flexfield_fitness_vs_gym.plot(kind='bar', color='blue')
plt.title('Average Hours at Gym per Week by Fitness Goal (FlexField Fitness)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 2: Fitness Goal vs. Gym Membership Length (years)
plt.figure(figsize=(10, 6))
flexfield_fitness_vs_membership = cleaned_flexfield_fitness_data.groupby('Fitness Goal')['Gym Membership Length (years)'].mean()
flexfield_fitness_vs_membership.plot(kind='bar', color='green')
plt.title('Average Gym Membership Length (Years) by Fitness Goal (FlexField Fitness)')
plt.ylabel('Average Gym Membership Length (Years)')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 3: Fitness Goal vs. Calorie Intake
plt.figure(figsize=(10, 6))
flexfield_fitness_vs_calorie = cleaned_flexfield_fitness_data.groupby('Fitness Goal')['Calorie Intake'].mean()
flexfield_fitness_vs_calorie.plot(kind='bar', color='orange')
plt.title('Average Calorie Intake by Fitness Goal (FlexField Fitness)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualization 4: Hours at Gym (per week) vs. Gym Membership Length (years)
plt.figure(figsize=(10, 6))
flexfield_gym_vs_membership = cleaned_flexfield_fitness_data.groupby('Hours at Gym (per week)')['Gym Membership Length (years)'].mean()
flexfield_gym_vs_membership.plot(kind='line', marker='o', color='purple')
plt.title('Average Gym Membership Length (Years) by Hours at Gym per Week (FlexField Fitness)')
plt.ylabel('Average Gym Membership Length (Years)')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 5: Hours at Gym (per week) vs. Calorie Intake
plt.figure(figsize=(10, 6))
flexfield_gym_vs_calorie = cleaned_flexfield_fitness_data.groupby('Hours at Gym (per week)')['Calorie Intake'].mean()
flexfield_gym_vs_calorie.plot(kind='line', marker='o', color='red')
plt.title('Average Calorie Intake by Hours at Gym per Week (FlexField Fitness)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Hours at Gym (per week)')
plt.show()

# Visualization 6: Gym Membership Length (years) vs. Calorie Intake
plt.figure(figsize=(10, 6))
flexfield_membership_vs_calorie = cleaned_flexfield_fitness_data.groupby('Gym Membership Length (years)')['Calorie Intake'].mean()
flexfield_membership_vs_calorie.plot(kind='line', marker='o', color='cyan')
plt.title('Average Calorie Intake by Gym Membership Length (Years) (FlexField Fitness)')
plt.ylabel('Average Calorie Intake')
plt.xlabel('Gym Membership Length (years)')
plt.show()
