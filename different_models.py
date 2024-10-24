# Import Necessary Libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from lightgbm import LGBMRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load the Dataset
# Replace 'your_data.csv' with the path to your actual dataset
data = pd.read_csv('data/cleaned_all.csv')

# Define the features and target
features = ['Calorie Intake', 'Dietary Preferences', 'Average Spend per Meal Order',
            'Preferred Sports Drink Type', 'Average Weekly Consumption (Bottles)', 'Average Spend on Apparel ($/year)',
            'Type of Apparel Purchased', 'Primary Apparel Purchase Channel']

# Use either 'Gym Membership Length (years)' or 'Hours at Gym (per week)' as the target
target = 'Hours at Gym (per week)'  # or 'Hours at Gym (per week)'

# Splitting numerical and categorical features
numerical_features = ['Calorie Intake', 'Average Spend per Meal Order', 
                      'Average Weekly Consumption (Bottles)', 'Average Spend on Apparel ($/year)']

categorical_features = ['Dietary Preferences', 'Preferred Sports Drink Type', 
                        'Type of Apparel Purchased', 'Primary Apparel Purchase Channel']

# Preprocessing pipelines for both numerical and categorical data
preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), numerical_features),
    ('cat', OneHotEncoder(), categorical_features)
])

# Split the data into training and testing sets
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the Models

# Linear Regression
lr_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('linearregression', LinearRegression())
])

# LightGBM
lgbm_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('lgbmregressor', LGBMRegressor())
])

lgbm_params = {
    'lgbmregressor__learning_rate': [0.01, 0.05, 0.1],
    'lgbmregressor__n_estimators': [100, 200, 500]
}

lgbm_search = GridSearchCV(lgbm_pipeline, param_grid=lgbm_params, cv=5)

# Support Vector Machine (SVR)
svr_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('svr', SVR())
])

svr_params = {
    'svr__C': [0.1, 1, 10],
    'svr__epsilon': [0.1, 0.2, 0.5]
}

svr_search = GridSearchCV(svr_pipeline, param_grid=svr_params, cv=5)

# Random Forest
rf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('rf', RandomForestRegressor())
])

rf_params = {
    'rf__n_estimators': [100, 200],
    'rf__max_depth': [10, 20, None]
}

rf_search = GridSearchCV(rf_pipeline, param_grid=rf_params, cv=5)

# Gradient Boosting
gb_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('gb', GradientBoostingRegressor())
])

gb_params = {
    'gb__learning_rate': [0.01, 0.05, 0.1],
    'gb__n_estimators': [100, 200]
}

gb_search = GridSearchCV(gb_pipeline, param_grid=gb_params, cv=5)

# XGBoost
xgb_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('xgb', XGBRegressor())
])

xgb_params = {
    'xgb__learning_rate': [0.01, 0.05, 0.1],
    'xgb__n_estimators': [100, 200],
    'xgb__max_depth': [3, 5, 7]
}

xgb_search = GridSearchCV(xgb_pipeline, param_grid=xgb_params, cv=5)

# Train the Models and Evaluate

# Linear Regression
lr_pipeline.fit(X_train, y_train)
y_pred_lr = lr_pipeline.predict(X_test)
mae_lr = mean_absolute_error(y_test, y_pred_lr)
r2_lr = r2_score(y_test, y_pred_lr)
print(f"Linear Regression - MAE: {mae_lr}, R² Score: {r2_lr}")

# LightGBM
#lgbm_search.fit(X_train, y_train)
#y_pred_lgbm = lgbm_search.best_estimator_.predict(X_test)
#mae_lgbm = mean_absolute_error(y_test, y_pred_lgbm)
#r2_lgbm = r2_score(y_test, y_pred_lgbm)
#print(f"LightGBM - Best Parameters: {lgbm_search.best_params_}, MAE: {mae_lgbm}, R² Score: {r2_lgbm}")

# Support Vector Machine (SVR)
svr_search.fit(X_train, y_train)
y_pred_svr = svr_search.best_estimator_.predict(X_test)
mae_svr = mean_absolute_error(y_test, y_pred_svr)
r2_svr = r2_score(y_test, y_pred_svr)
print(f"Support Vector Machine - Best Parameters: {svr_search.best_params_}, MAE: {mae_svr}, R² Score: {r2_svr}")

# Random Forest
rf_search.fit(X_train, y_train)
y_pred_rf = rf_search.best_estimator_.predict(X_test)
mae_rf = mean_absolute_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
print(f"Random Forest - Best Parameters: {rf_search.best_params_}, MAE: {mae_rf}, R² Score: {r2_rf}")

# Gradient Boosting
gb_search.fit(X_train, y_train)
y_pred_gb = gb_search.best_estimator_.predict(X_test)
mae_gb = mean_absolute_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)
print(f"Gradient Boosting - Best Parameters: {gb_search.best_params_}, MAE: {mae_gb}, R² Score: {r2_gb}")

# XGBoost
xgb_search.fit(X_train, y_train)
y_pred_xgb = xgb_search.best_estimator_.predict(X_test)
mae_xgb = mean_absolute_error(y_test, y_pred_xgb)
r2_xgb = r2_score(y_test, y_pred_xgb)
print(f"XGBoost - Best Parameters: {xgb_search.best_params_}, MAE: {mae_xgb}, R² Score: {r2_xgb}")
