# Change Log

## 05/02/2025

Started K nearest neighbour training model on heart attack data to make predictions
found dataset and printed the head

https://www.kaggle.com/datasets/ankushpanday1/heart-attack-risk-predictions

## 06/02/2025

trying different n of neighbours only achieving 50% accuracy
and removing a lot of the columns.
Tried using 'euclidean', 'manhattan', 'chebyshev' as different parameters along with a few different number of neighbours all not really making a difference in the accuracy 

## 10/02/2025

Making groups for columns numerical columns like age
Trying Mutual Information (MI) for Feature Selection to only use important features

## 11/02/2025

set up gridsearch using 'n_neighbors': [3, 5, 10, 15], 'metric': ['manhattan', 'euclidean'] and 'weights': ['uniform', 'distance'] as parameters

## 18/02/2025

Added SMOTE (Synthetic Minority Over-sampling Technique) to the pipeline to test its effect on the model's performance. However, since the dataset is not imbalanced, SMOTE had no significant impact on the accuracy or the overall performance of the model. Continued to explore other methods to improve the model's predictive power.

## 25/02/2025

Attempted to shift the focus from predicting the binary outcome of a heart attack to calculating the risk score for each individual. This involved modifying the target variable and adjusting the evaluation metrics accordingly. Despite these changes, the model's accuracy remained close to random guessing, indicating that further feature engineering and model tuning are necessary.

## 03/03/2025

used HalvingGridSearchCV to shorten run time as it was 3 hours long with regular cvsearch due to the dataset being large

combined high and medium risk as the model suffered with class seperation and reintroduced smote as this caused imbalance






