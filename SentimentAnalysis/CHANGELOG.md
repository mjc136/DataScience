# Change Log

## 29/01/2025
started log after make rough model using dataset from https://data.mendeley.com/datasets/z9zw7nt5h2/1
at this point accuracy is at 75 so im going to do more pre processing to fix this

## 30/01/2025
change dataset to https://www.cs.jhu.edu/~mdredze/datasets/sentiment/ as was more large but
accuracy is still only 78
i tried using GridSearchCV and taking certain characters such as extra whitespace and special characters out of text but has not made much of an impact
I also tried using SMOTE (Synthetic Minority Over-sampling Technique), which is a technique used to balance an imbalanced dataset by creating synthetic (new) data points for the minority class. I stopped using it as it was very expensive and didn't make any noticeable improvements.

## 04/02/2025
started markdown