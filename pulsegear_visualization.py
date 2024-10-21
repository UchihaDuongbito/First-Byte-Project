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
plt.xticks(rotation=45)
plt.show()
