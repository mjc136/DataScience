<h1>Titanic Survival Predictor</h1>

<h2>Data Source</h2>
<p>I got my data from the seaborn Titanic dataset.</p>
<p>The dataset contains information about passengers on the Titanic, including whether they survived or not. The dataset includes a variety of features such as age, sex, class, and ticket fare, among others.</p>
<p>I got the dataset running this command "sns.load_dataset('titanic')"</p>
<br />

<h2>Pre-Processing</h2>
<p>I split the data into 70/30 for training and testing.</p>
<p>The data was cleaned by handling missing values, converting categorical variables into numerical ones, and normalising the data when necessary.</p>
<p>I used the following steps for data preparation:</p>
<ul>
    <li>Imputed missing values for Age using the median.</li>
    <li>Converted categorical features like 'Sex' and 'class' into numerical values using Label Encoding.</li>
    <li>Dropped unnecessary columns that weren’t essential or ones that did all the work for me so i could demostrate my skills for the prediction model.</li>
</ul>

<h2>Data Understanding and Visualisation</h2>
<p>To visualise the data, I created a tree diagram to understand the distribution of key features such as age, fare, and class.</p>
<p>I noticed the following key points:</p>
<ul>
    <li>More passengers survived in higher classes.</li>
    <li>A higher percentage of women and children survived compared to men.</li>
    <li>The majority of passengers were younger than 40 years old.</li>
</ul>

<h2>Algorithms</h2>
<p>I chose to use a <strong>Decision Tree Classifier</strong> for predicting survival on the Titanic. This model is ideal for handling both categorical and numerical data, which is common in the Titanic dataset. I used the <code>entropy</code> criterion to evaluate splits and set the maximum depth of the tree to 5 to prevent overfitting.</p>
<p>The decision tree model was trained on features such as sex, age group, class, and family size. After fitting the model, I evaluated its performance using accuracy, a classification report, and a confusion matrix.</p>

<p>I also created a sample prediction for a passenger and showed the confidence of the model in making that prediction. The following features were used for the sample:</p>
<ul>
    <li>Sex: Female (2)</li>
    <li>Age group: Young Adult (3)</li>
    <li>Class: 3rd</li>
    <li>Family size: 2</li>
</ul>
<p>The prediction result indicates whether the passenger survived or not, along with the model's confidence in that prediction.</p>

<h2>Online Resources</h2>
<p>I used the following documentation for reference:</p>
<ul>
    <li><a href="https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">Scikit-learn - Decision Tree Classifier</a></li>
    <li><a href="https://pandas.pydata.org/docs/">Pandas Documentation</a></li>
    <li><a href="https://matplotlib.org/stable/contents.html">Matplotlib Documentation</a></li>
</ul>

<h2>Tools Used</h2>
<p>Python was the programming language I used as I am most comfortable with it.</p>
<p>I used the following Python libraries:</p>
<ul>
    <li><strong>Pandas</strong> for data manipulation and preprocessing</li>
    <li><strong>NumPy</strong> for numerical computations</li>
    <li><strong>Matplotlib</strong> for data visualisation and creating the decision tree plot</li>
    <li><strong>Scikit-learn</strong> for the Decision Tree model, training, and evaluation</li>
</ul>
<p>I developed the project using <strong>Jupyter Notebook</strong> for its interactive nature and <strong>GitHub</strong> for version control.</p>