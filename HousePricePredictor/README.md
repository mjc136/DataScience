<h1>House Price Predictor</h1>

<h2>Project Overview</h2>
<p>
    House Price Predictor is a Python-based application that forecasts average house prices in the UK. 
    Users can select specific regions to filter data, view scatter plot visualisations, and predict prices 
    using a linear regression model.
</p>

<h2>Key Features</h2>
<ul>
    <li>Filter historical house price data by region (1995–2024).</li>
    <li>Visualise trends using scatter plots.</li>
    <li>Predict future house prices with linear regression.</li>
    <li>Highlight the impact of major economic events on house prices.</li>
</ul>

<h2>Data Source</h2>
<p>
    The dataset was obtained from UK government datasets, containing over 141,000 rows spanning from 1995 to 2024. 
    <a href="https://www.gov.uk/government/statistical-data-sets/uk-house-price-index-data-downloads-january-2024" target="_blank">
        Dataset link
    </a>
</p>

<h2>Pre-Processing</h2>
<ul>
    <li>Data is split 70/30 for training and testing.</li>
    <li>Region-based filtering ensures predictions are specific to the selected area.</li>
</ul>

<h2>Data Understanding and Visualisation</h2>
<p>
    Scatter plots were created to visualise trends. Notable observations include:
</p>
<ul>
    <li>A significant drop in 2008 during the financial crisis.</li>
    <li>A minor dip in 2020 due to the COVID-19 pandemic.</li>
</ul>

<h2>Algorithms</h2>
<p>
    Linear regression was chosen for its simplicity and suitability for capturing steady increases in house prices over time.
</p>
<p>
    The slope of the regression line indicates the average annual increase in house prices within the selected region.
</p>

<h2>Tools Used</h2>
<ul>
    <li><strong>Programming Language:</strong> Python</li>
    <li><strong>Libraries:</strong> Pandas, NumPy, Matplotlib, ipywidgets</li>
    <li><strong>Development Environment:</strong> Jupyter Notebook</li>
    <li><strong>Version Control:</strong> GitHub</li>
</ul>

<h2>Results and Observations</h2>
<p>
    The linear regression model highlights steady growth in house prices over time. 
    Economic downturns, such as the 2008 market crash and the 2020 pandemic, caused noticeable drops.
</p>
<p>
    The slope of the regression line provides an estimate of the average annual growth in house prices for the selected region.
</p>

<h2>Future Enhancements</h2>
<ul>
    <li>Add advanced machine learning models (e.g., Random Forest, Gradient Boosting).</li>
    <li>Include additional datasets for deeper insights.</li>
    <li>Develop a standalone web application for better accessibility.</li>
</ul>

<h2>Online Resources</h2>
<ul>
    <li><a href="https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html" target="_blank">Matplotlib Documentation</a></li>
    <li><a href="https://numpy.org/doc/" target="_blank">NumPy Documentation</a></li>
    <li><a href="https://pandas.pydata.org/docs/" target="_blank">Pandas Documentation</a></li>
</ul>


