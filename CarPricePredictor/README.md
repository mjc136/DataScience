<h1>Vehicle Price Prediction</h1>

<h2>Project Overview</h2>
<p>
    This project builds a predictive model using a <strong>Random Forest Regressor</strong> to estimate vehicle prices based on various attributes. 
    The dataset includes information such as vehicle make, model, year, odometer readings, and condition. 
    The model is trained and evaluated to understand key factors influencing vehicle pricing and provide accurate predictions.
</p>

<h2>Data Source</h2>
<p>
    The project initially attempted to use a dataset from 
    <a href="https://zenodo.org/records/10457828">Zenodo</a>. However, the dataset was found to be unsuitable due to issues such as poor data quality and incomplete records. 
    As a result, the dataset from <a href="https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/data">Kaggle</a> was used instead, providing more reliable and comprehensive information for building the model.
</p>


<h2>Key Features</h2>
<ul>
    <li><strong>Data Handling:</strong>
        <ul>
            <li>Dynamically downloads the dataset using <code>kagglehub</code> for reproducibility.</li>
            <li>Drops irrelevant columns (e.g., <code>vin</code>, <code>trim</code>) and handles missing values.</li>
        </ul>
    </li>
    <li><strong>Feature Engineering:</strong>
        <ul>
            <li>Converts continuous variables like mileage and year into categorical groups.</li>
            <li>Encodes categorical features such as make, model, and fuel type using <code>LabelEncoder</code>.</li>
            <li>Groups rare vehicle colours into an "Other" category.</li>
        </ul>
    </li>
    <li><strong>Model Training:</strong>
        <ul>
            <li>Splits the dataset into training (70%) and testing (30%) subsets.</li>
            <li>Trains a Random Forest Regressor with optimised hyperparameters using <code>GridSearchCV</code>.</li>
        </ul>
    </li>
    <li><strong>Model Evaluation:</strong>
        <ul>
            <li>Evaluates model performance using Mean Squared Error (MSE) and R-squared (R²).</li>
            <li>Visualises feature importance to identify key factors in price prediction.</li>
        </ul>
    </li>
</ul>

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

<h2>Results and Insights</h2>
<p>
    The Random Forest Regressor accurately predicts vehicle prices with low Mean Squared Error and high R-squared values. 
    Feature importance analysis highlights key contributors like vehicle age, mileage, and condition.
</p>

<h2>Future Enhancements</h2>
<ul>
    <li>Experiment with advanced models for improved accuracy.</li>
</ul>
