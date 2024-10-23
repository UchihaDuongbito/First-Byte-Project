import matplotlib.pyplot as plt
import pandas as pd

# Load the cleaned dataset
cleaned_pulsegear_data = pd.read_csv('data/cleaned_pulsegear.csv')

# Visualizing the relationship between fitness goals and hours spent at gym in PulseGear data
plt.figure(figsize=(10, 6))
pulsegear_grouped = cleaned_pulsegear_data.groupby('Fitness Goal')['Hours at Gym (per week)'].mean()
pulsegear_grouped.plot(kind='bar')
plt.title('Average Hours at Gym per Week by Fitness Goal (PulseGear)')
plt.ylabel('Average Hours at Gym per Week')
plt.xlabel('Fitness Goal')
plt.xticks(rotation=15)
plt.show()

# Visualizing the relationship between Average Spend on Apparel ($/year) and hours spent at gym in PulseGear data
plt.figure(figsize=(10, 6))
pulsegear_gym_vs_spend = cleaned_pulsegear_data.groupby('Hours at Gym (per week)')['Average Spend on Apparel ($/year)'].mean()
pulsegear_gym_vs_spend.plot(kind='line', marker='o', color='blue')
plt.title('Average Spend on Apparel ($/year) by Hours at Gym per Week (PulseGear)')
plt.ylabel('Average Spend on Apparel ($/year)')
plt.xlabel('Hours at Gym (per week)')
plt.show()