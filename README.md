# Food Delivery Time Prediction

## Problem Statement
Accurate delivery time prediction is critical for food delivery platforms. 
Delayed deliveries reduce customer satisfaction and affect ratings and retention.

This project builds a machine learning model to predict delivery time (in minutes)
based on operational and rider-related features.

## Dataset Overview
The dataset includes:

- Restaurant & delivery coordinates
- Delivery partner details (age, ratings)
- Type of order
- Type of vehicle
- Target: Delivery Time_taken(min)


## Feature Engineering
- Calculated distance (km) using Haversine formula
- Removed unrealistic distance outliers (> 50 km)
- Dropped latitude & longitude after distance calculation
- Applied one-hot encoding for categorical variables
- Performed 80-20 train-test split


## Models Tested
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor (Final Model)


## Final Model Performance
Gradient Boosting Regressor:

- MAE: 5.68 minutes
- RMSE: 7.24 minutes
- 5-Fold Cross Validation MAE: 5.68 minutes

The model shows stable and reliable performance.


## Deployment
The trained model is saved as:

delivery_time_model.pkl

It can be deployed using Flask or FastAPI
to provide real-time delivery time predictions.


## Key Insight
Distance is the most important factor influencing delivery time,
followed by delivery partner ratings.
