# Change Log

## 29/01/2025
- Started log after creating a rough model using the dataset from [Mendeley Data](https://data.mendeley.com/datasets/z9zw7nt5h2/1). At this point, the accuracy is at 75%, so I'm going to do more preprocessing to improve this.

## 30/01/2025
- Changed dataset to [Johns Hopkins University Sentiment Dataset](https://www.cs.jhu.edu/~mdredze/datasets/sentiment/) as it was larger, but the accuracy is still only 78%. I tried using GridSearchCV and removing certain characters such as extra whitespace and special characters from the text, but it has not made much of an impact. 
- I also tried using SMOTE (Synthetic Minority Over-sampling Technique), which is a technique used to balance an imbalanced dataset by creating synthetic (new) data points for the minority class. I stopped using it as it was very expensive and didn't make any noticeable improvements.

## 04/02/2025
- Started markdown for each of the cells.
