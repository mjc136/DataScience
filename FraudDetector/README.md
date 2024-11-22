<h1>Online Payment Fraud Detection</h1>

<h2>Project Overview</h2>
<p>
    This project leverages a Decision Tree Classifier to detect fraudulent transactions within an online payment dataset. 
    The model is trained and evaluated on a dataset containing detailed transaction records, focusing on identifying patterns that indicate fraudulent behaviour.
</p>

<h2>Key Features</h2>
<ul>
    <li>Pre-processes transaction data, including converting transaction types to numerical values.</li>
    <li>Uses a Decision Tree Classifier to classify transactions as fraudulent or non-fraudulent.</li>
    <li>Evaluates the model using accuracy, classification report, and confusion matrix.</li>
    <li>Visualises the decision tree structure for interpretability.</li>
</ul>

<h2>Data Source</h2>
<p>
    The dataset contains records of online transactions with features such as transaction type, amount, origin, and destination. 
    It also includes labels for fraud detection, indicating whether a transaction was fraudulent (<code>isFraud</code>).
    The dataset was from <a href="https://www.kaggle.com/datasets/jainilcoder/online-payment-fraud-detection">Kaggle</a>
</p>

<h2>Pre-Processing</h2>
<ul>
    <li>Mapped transaction types (<code>type</code>) to numerical values for machine learning compatibility.</li>
    <li>Dropped unnecessary columns like <code>nameOrig</code> and <code>nameDest</code> to focus on relevant features.</li>
</ul>

<h2>Model Training and Evaluation</h2>
<ul>
    <li>Split the dataset into training (70%) and testing (30%) subsets for model validation.</li>
    <li>Trained a Decision Tree Classifier with the following hyperparameters:
        <ul>
            <li>Maximum depth: 10</li>
            <li>Minimum samples per split: 10</li>
            <li>Minimum samples per leaf: 5</li>
            <li>Class weight: Balanced</li>
        </ul>
    </li>
    <li>Evaluated the model's performance using:
        <ul>
            <li>Accuracy score</li>
            <li>Classification report</li>
            <li>Confusion matrix</li>
        </ul>
    </li>
</ul>

<h2>Visualisation</h2>
<p>
    The decision tree structure is visualised to provide insights into the model's decision-making process. 
    The plot displays feature splits, decision outcomes, and class distributions at each node.
</p>

<h2>Tools and Libraries Used</h2>
<ul>
    <li><strong>Programming Language:</strong> Python</li>
    <li><strong>Libraries:</strong>
        <ul>
            <li>Pandas</li>
            <li>Scikit-learn</li>
            <li>Matplotlib</li>
        </ul>
    </li>
</ul>

<h2>Results and Observations</h2>
<p>
    The Decision Tree Classifier demonstrated the ability to accurately distinguish between fraudulent and non-fraudulent transactions. 
    The confusion matrix and classification report highlight the model's performance, including precision, recall, and F1-score for each class.
</p>

<h2>Future Enhancements</h2>
<ul>
    <li>Experiment with more advanced models such as Random Forest</li>
    <li>Add additional visualisations to explore feature importance.</li>
</ul>

