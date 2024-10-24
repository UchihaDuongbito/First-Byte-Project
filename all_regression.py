import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.pipeline import make_pipeline

# Load the data
data = pd.read_csv('data/all.csv')

# Clean data
cleaned_data = data.dropna(subset=['Hours at Gym (per week)', 'Type of Apparel Purchased', 'Preferred Sports Drink Type', 'Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order'])
cleaned_data.to_csv('data/cleaned_all.csv', index=False)