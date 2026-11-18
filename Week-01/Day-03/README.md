
# Day 03 – Machine Learning Fundamentals

## Project: SMS Spam Classification

### Objective
Build a machine learning model to classify SMS messages as spam or ham (normal messages).

### Dataset
- Source: SMS Spam Collection Dataset (Kaggle/UCI)
- Original records: 5,572
- Records after cleaning: 5,169
- Selected sample: 500 messages
- Classes: 250 spam and 250 ham

### Tools and Libraries
- Google Colab
- Python
- pandas
- scikit-learn
- matplotlib

### Methodology
1. Loaded and explored the dataset.
2. Removed unnecessary columns, missing values, and duplicates.
3. Selected a balanced sample of 500 messages.
4. Split the dataset into 80% training and 20% testing.
5. Used TF-IDF for text feature extraction.
6. Trained a Multinomial Naive Bayes classifier.
7. Evaluated the model using classification metrics.
8. Tested predictions on new messages.

### Evaluation Results

| Metric | Score |
|---|---|
| Accuracy | 90% |
| Precision (Spam) | 90% |
| Recall (Spam) | 90% |
| F1 Score (Spam) | 90% |

### Confusion Matrix
- Correctly classified ham: 45
- Correctly classified spam: 45
- Ham incorrectly classified as spam: 5
- Spam incorrectly classified as ham: 5

### Limitations
The model was trained using only 500 balanced messages. Its performance may differ on real-world data. Some normal messages were incorrectly classified as spam.

### Files
- `Day_03_Spam_Classifier.ipynb` – Model training and evaluation
- `spam.csv` – Original dataset

### Conclusion
Successfully developed and evaluated a basic SMS spam classification model using Python and scikit-learn.
